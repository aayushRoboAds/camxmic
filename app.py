import cv2
import mediapipe as mp
import talking_mic.mute as mute
import time

# Initialize MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

# OpenCV Video Capture
cap = cv2.VideoCapture(0)

# Store speaking state
speaking = False
last_called = 0

def mouth_open_ratio(landmarks, height, width):
    top_lip = landmarks[13]
    bottom_lip = landmarks[14]
    top = int(top_lip.y * height)
    bottom = int(bottom_lip.y * height)
    return abs(bottom - top)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        landmarks = face_landmarks.landmark

        ratio = mouth_open_ratio(landmarks, height, width)
        now = time.time()
        if ratio > 5 : # mouth opening vertical ratio threshold
            last_seen_time = now
            if not speaking:
                speaking = True
                mute.mute_microphone(False)  # Ensure mic is on
                print("🟢 MIC ON")

        elif speaking and (now - last_seen_time > 10): #timeout - 10 secs without speaking human
            mute.mute_microphone(True)
            speaking = False
            print("🔴 MIC OFF")
      
    else:
        
        if speaking:
            mute.mute_microphone(True)
            print("No face detected")
            print("🔴 Muted due to no face ")
            speaking=False

    cv2.imshow("Speaking Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
