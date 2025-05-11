import cv2
import time
from attention_detector import detect_attention
from cloud_storage import save_focus_log

cap = cv2.VideoCapture(0)
print("🎥 AI Study Monitor started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    status, message = detect_attention(frame)

    cv2.putText(frame, f'Status: {message}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # 顯示畫面
    cv2.imshow("Study Monitor", frame)

    # 儲存 log
    save_focus_log(status)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
