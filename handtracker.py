import cv2
import mediapipe as mp
from gesturelogic import handsgesture, signs

mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles

mphands = mp.solutions.hands

capture = cv2.VideoCapture(0)

hands = mphands.Hands()

while True :
    data,image = capture.read()
    image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) #flipping the image
    results = hands.process(image) #storing result
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks :
        total,sign=0,""
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mphands.HAND_CONNECTIONS
            )

            current_gesture = handsgesture(hand_landmarks)
            current_sign = signs(hand_landmarks)
            total+=current_gesture
            
        cv2.putText(image, str(total), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5, cv2.LINE_AA)
        cv2.putText(image, current_sign, (250, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Handtracker',image)
    if cv2.waitKey(1) & 0xFF == ord('0'): break #press 0 to quit

#cleanup
capture.release()
cv2.destroyAllWindows()