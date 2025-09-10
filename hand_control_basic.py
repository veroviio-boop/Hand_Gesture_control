import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Start webcam
cap = cv2.VideoCapture(0)

# Get screen size
screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    if not success:
        break

    # Convert image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Index finger tip = landmark 8
            h, w, c = img.shape
            index_x = int(handLms.landmark[8].x * w)
            index_y = int(handLms.landmark[8].y * h)

            # Map webcam coords → screen coords
            #screen_x = screen_w * (handLms.landmark[8].x)
            screen_x = screen_w * (1 - handLms.landmark[8].x)

            screen_y = screen_h * (handLms.landmark[8].y)

            pyautogui.moveTo(screen_x, screen_y)

    # Show webcam feed
    cv2.imshow("Hand Tracking", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
