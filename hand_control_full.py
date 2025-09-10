import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import os

# Init mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Screen size
screen_w, screen_h = pyautogui.size()

# Smoothing setup
prev_x, prev_y = 0, 0
alpha = 0.2  # smoothing factor

cap = cv2.VideoCapture(1)  # change to 0 if using phone camera

def fingers_up(hand_landmarks, img_h, img_w):
    """ Detect which fingers are up (ignores thumb).
        Returns [index, middle, ring, pinky]
    """
    wrist = hand_landmarks.landmark[0]
    fingers = []

    tips = [8, 12, 16, 20]  # index, middle, ring, pinky
    for tip in tips:
        tip_point = hand_landmarks.landmark[tip]
        base_point = hand_landmarks.landmark[tip - 2]

        dist_tip_wrist = math.hypot(
            (tip_point.x - wrist.x) * img_w,
            (tip_point.y - wrist.y) * img_h
        )
        dist_base_wrist = math.hypot(
            (base_point.x - wrist.x) * img_w,
            (base_point.y - wrist.y) * img_h
        )

        if dist_tip_wrist > dist_base_wrist:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            fingers = fingers_up(handLms, h, w)

            # Debugging display
            cv2.putText(frame, str(fingers), (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

            # Cursor movement with index finger
            index_x = int(handLms.landmark[8].x * w)
            index_y = int(handLms.landmark[8].y * h)

            screen_x = np.interp(index_x, [0, w], [0, screen_w])
            screen_y = np.interp(index_y, [0, h], [0, screen_h])

            curr_x = prev_x + (screen_x - prev_x) * alpha
            curr_y = prev_y + (screen_y - prev_y) * alpha
            prev_x, prev_y = curr_x, curr_y

            # Gestures
            if fingers == [1,0,0,0]:   # Index only → move cursor
                pyautogui.moveTo(curr_x, curr_y)

            elif fingers == [1,1,0,0]: # Index + middle → left click
                pyautogui.click()
                pyautogui.sleep(0.3)

            elif fingers == [0,1,0,0]: # Middle only → right click
                pyautogui.click(button='right')
                pyautogui.sleep(0.3)

            elif fingers == [1,1,1,1]: # Open palm → volume up
                os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 5)'")
                pyautogui.sleep(0.5)

            elif fingers == [0,0,0,0]: # Fist → volume down
                os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 5)'")
                pyautogui.sleep(0.5)

    cv2.imshow("Hand Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
