import cv2
import face_recognition
import os
import sqlite3
from datetime import datetime

# Load database connection
def get_connection():
    return sqlite3.connect("database/employees.db")

def mark_attendance(name):
    conn = get_connection()
    cur = conn.cursor()

    today = datetime.now().date()

    # Get employee id
    cur.execute("SELECT id FROM employees WHERE name = ?", (name,))
    result = cur.fetchone()

    if result:
        emp_id = result[0]

        # Check if already marked today
        cur.execute("SELECT * FROM attendance WHERE employee_id=? AND date=?", (emp_id, today))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO attendance (employee_id, date) VALUES (?, ?)", (emp_id, today))
            conn.commit()
            print(f"{name} marked present")
        else:
            print(f"{name} already marked today")

    conn.close()


def recognize_faces():

    path = "face_data"
    images = []
    classNames = []

    # Load images
    for file in os.listdir(path):
        img = cv2.imread(f"{path}/{file}")
        images.append(img)
        classNames.append(os.path.splitext(file)[0])

    # Encode faces
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        enc = face_recognition.face_encodings(img)
        if enc:
            encodeList.append(enc[0])

    print("Face recognition started...")

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        if not success:
            break

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeList, encodeFace)
            faceDis = face_recognition.face_distance(encodeList, encodeFace)

            if len(faceDis) > 0:
                matchIndex = faceDis.argmin()

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()

                    # Mark attendance
                    mark_attendance(name)

                    # Draw box
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

                    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.putText(img, name, (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.imshow("Face Recognition", img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
