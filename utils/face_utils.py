import cv2
import numpy as np
import base64
import os

FACE_DATA_DIR = "face_data"
if not os.path.exists(FACE_DATA_DIR):
    os.makedirs(FACE_DATA_DIR)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Tighter parameters to avoid false positives on background patterns
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(80, 80))
    if len(faces) == 0:
        return None, None
        
    faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
    (x, y, w, h) = faces[0]
    face_roi_gray = gray[y:y+h, x:x+w]
    return face_roi_gray, (x, y, w, h)

TRAINER_FILE = os.path.join(FACE_DATA_DIR, "trainer.yml")

def register_face(user_id, base64_img):
    img = data_uri_to_cv2_img(base64_img)
    face_roi, _ = detect_face(img)
    
    if face_roi is None:
        return False
        
    faces = [face_roi]
    ids = np.array([user_id])
    
    # Check if a model exists to incrementally update, otherwise train a new one
    if os.path.exists(TRAINER_FILE):
        try:
            # Load existing
            recognizer.read(TRAINER_FILE)
            # Incrementally update the AI matrix without needing old photos!
            recognizer.update(faces, ids)
        except Exception as e:
            # Fallback if corrupted
            recognizer.train(faces, ids)
    else:
        # First time training
        recognizer.train(faces, ids)
        
    # Save mathematical embeddings to file. No .jpg is saved!
    recognizer.write(TRAINER_FILE)
    
    # Delete any lingering JPEGs for privacy assurance
    for filename in os.listdir(FACE_DATA_DIR):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            try:
                os.remove(os.path.join(FACE_DATA_DIR, filename))
            except:
                pass
                
    return True

try:
    if os.path.exists(TRAINER_FILE):
        recognizer.read(TRAINER_FILE)
except Exception as e:
    pass

def recognize_face_with_liveness(base64_img):
    """
    Returns: (user_id, has_eyes, confidence)
    """
    if not os.path.exists(os.path.join(FACE_DATA_DIR, "trainer.yml")):
        return None, False, 0
        
    img = data_uri_to_cv2_img(base64_img)
    face_roi, coords = detect_face(img)
    
    if face_roi is None:
        return None, False, 0
        
    # Eye detection for spoofing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (x, y, w, h) = coords
    # Eyes are usually in the top half of the face
    roi_color_eyes = gray[y:y + int(h/2), x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_color_eyes, 1.1, 3)
    has_eyes = len(eyes) > 0
        
    label, confidence = recognizer.predict(face_roi)
    
    # 85 is usually a decent threshold. Lower distance = better.
    if confidence < 85:  
        return label, has_eyes, confidence
    return None, has_eyes, confidence
