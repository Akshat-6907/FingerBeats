import cv2
import mediapipe as mp
from gesturelogic import handsgesture, signs

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

capture = cv2.VideoCapture(0)

hands = mphands.Hands(max_num_hands=2, model_complexity = 1)

while True :
    data,image = capture.read()
    if not data : break

    image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) #flipping the image
    results = hands.process(image) #storing result
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks :
        h,w,_ = image.shape
        total=0
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mphands.HAND_CONNECTIONS
            )

            current_gesture = handsgesture(hand_landmarks,w,h)
            current_sign = signs(hand_landmarks,w,h)
            total+=current_gesture
            
        cv2.putText(image, str(total), (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)
        cv2.putText(image, current_sign, (250, 400),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Handtracker',image)
    if cv2.waitKey(1) & 0xFF == ord('0'): break #press 0 to quit

#cleanup
capture.release()
cv2.destroyAllWindows()