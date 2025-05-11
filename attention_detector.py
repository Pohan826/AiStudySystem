import mediapipe as mp
import cv2

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5)

def detect_attention(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_detection.process(img_rgb)

    if result.detections:
        return True, "Focusing"
    else:
        return False, "Away or Distracted"
