import cv2
import mediapipe as mp
from gesturelogic import handsgesture,signs
from audio_play import stop_music,drums_set,bass_set,synths_set

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

capture = cv2.VideoCapture(0)

hands = mphands.Hands(max_num_hands=2, model_complexity = 1)

def play_audio(x):
    max_vol = 0.6
    if x==0:
        drums_set(0)
        bass_set(0)
        synths_set(max_vol)
        change_text([1,0,0])
    elif x==1:
        drums_set(max_vol)
        bass_set(0)
        synths_set(max_vol)
        change_text([1,1,0])
    elif x==2:
        drums_set(0)
        bass_set(max_vol)
        synths_set(max_vol)
        change_text([1,0,1])
    elif x==3:
        drums_set(max_vol)
        bass_set(max_vol)
        synths_set(0)
        change_text([0,1,1])
    elif x==4:
        drums_set(max_vol)
        bass_set(max_vol)
        synths_set(max_vol)
        change_text([1,1,1])
    else:
        drums_set(0)
        bass_set(0)
        synths_set(0)
        change_text([0,0,0])

def text():
    cv2.putText(image, "SYNTH", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)
    cv2.putText(image, "DRUMS", (50, 100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)
    cv2.putText(image, "BASS", (50, 150),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)

def change_text(list):
    if list[0]: cv2.putText(image, "SYNTH", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)
    if list[1]: cv2.putText(image, "DRUMS", (50, 100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)
    if list[2]: cv2.putText(image, "BASS", (50, 150),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)

while True :
    data,image = capture.read()
    if not data : break

    image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) #flipping the image
    results = hands.process(image) #storing result
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    text()
    if results.multi_hand_landmarks :
        h,w,_ = image.shape
        total,last_total=0,-1
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mphands.HAND_CONNECTIONS
            )

            current_gesture = handsgesture(hand_landmarks,w,h)
            current_sign = signs(hand_landmarks,w,h)
            total+=current_gesture

            if total!=last_total:
                play_audio(total)
                last_total=total

        cv2.putText(image, current_sign, (250, 400),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Handtracker',image)
    if cv2.waitKey(1) & 0xFF == ord('0'): break #press 0 to quit

#cleanup
capture.release()
cv2.destroyAllWindows()
stop_music

