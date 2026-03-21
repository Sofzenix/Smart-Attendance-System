import cv2
import numpy as np
import base64
import os

FACE_DATA_DIR = "face_data"
if not os.path.exists(FACE_DATA_DIR):
    os.makedirs(FACE_DATA_DIR)

CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# Using LBPH which doesn't require dlib/compilation
recognizer = cv2.face.LBPHFaceRecognizer_create()

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    if len(faces) == 0:
        return None
        
    # Take largest face
    faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
    (x, y, w, h) = faces[0]
    return gray[y:y+h, x:x+w]

def register_face(user_id, base64_img):
    img = data_uri_to_cv2_img(base64_img)
    face_roi = detect_face(img)
    
    if face_roi is None:
        return False
        
    cv2.imwrite(os.path.join(FACE_DATA_DIR, f"{user_id}.jpg"), face_roi)
    train_model()
    return True

def train_model():
    faces = []
    ids = []
    
    for filename in os.listdir(FACE_DATA_DIR):
        if filename.endswith(".jpg"):
            path = os.path.join(FACE_DATA_DIR, filename)
            
            try:
                user_id = int(os.path.splitext(filename)[0])
            except ValueError:
                continue
                
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            ids.append(user_id)
            
    if len(faces) > 0:
        recognizer.train(faces, np.array(ids))
        recognizer.write(os.path.join(FACE_DATA_DIR, "trainer.yml"))

# Load model if it exists
try:
    if os.path.exists(os.path.join(FACE_DATA_DIR, "trainer.yml")):
        recognizer.read(os.path.join(FACE_DATA_DIR, "trainer.yml"))
except Exception as e:
    print("Warning: Could not load LBPH trainer:", e)

def recognize_face(base64_img):
    if not os.path.exists(os.path.join(FACE_DATA_DIR, "trainer.yml")):
        return None 
        
    img = data_uri_to_cv2_img(base64_img)
    face_roi = detect_face(img)
    
    if face_roi is None:
        return None
        
    label, confidence = recognizer.predict(face_roi)
    
    # Lower distance (confidence value) refers to closer match
    if confidence < 85:  
        return label
    return None
