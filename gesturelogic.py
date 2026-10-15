def handsgesture(hand_landmarks):
    list1 = []

    #get coordinates of all points
    for lm in hand_landmarks.landmark : list1.append(lm)
    '''{
        [6] is index finger base , [8] is index finger tip,
        [10] is index middle base , [12] is index middle tip,
        [14] is index ring base , [16] is index ring tip,
        [18] is index pinky base , [20] is index pinky tip,
        [3] is index thumb base , [4] is index thumb tip

        each contains x and y coords.
    }'''

    #1 means finger extended , 0 means finger retracted
    finger_state = [
                    list1[8].y < list1[6].y,   # Index
                    list1[12].y < list1[10].y, # Middle
                    list1[16].y < list1[14].y, # Ring
                    list1[20].y < list1[18].y  # Pinky
                    ]

    index,middle,ring,pinky = finger_state[0],finger_state[1],finger_state[2],finger_state[3]
    
    if list1[5].x < list1[17].x:
        # Hand orientation puts the thumb on the LEFT side then check if thumb tip is on left 0f inner joint
        thumb = list1[4].x < list1[3].x 
    else:
        # Hand orientation puts the thumb on the RIGHT side then check if thumb tip is on right 0f inner joint        thumb = list1[4].x > list1[3].x
        thumb = list1[4].x > list1[3].x
    
    if index and not any([middle,ring,pinky,thumb]):
        return 1
    elif all([index,middle]) and not any([ring,pinky,thumb]):
        return 2
    elif all([index,middle,ring]) and not any([pinky,thumb]):
        return 3
    elif all([index,middle,ring,pinky]) and not thumb:
        return 4
    elif all([index,middle,ring,pinky,thumb]): return 5

    #undefined gesture
    return 0

def signs(hand_landmarks):
    list1 = []

    #get coordinates of all points
    for lm in hand_landmarks.landmark : list1.append(lm)
    '''{
        [6] is index finger base , [8] is index finger tip,
        [10] is index middle base , [12] is index middle tip,
        [14] is index ring base , [16] is index ring tip,
        [18] is index pinky base , [20] is index pinky tip,
        [3] is index thumb base , [4] is index thumb tip

        each contains x and y coords.
    }'''

    #1 means finger extended , 0 means finger retracted
    finger_state = [
                    list1[8].y < list1[6].y,   # Index
                    list1[12].y < list1[10].y, # Middle
                    list1[16].y < list1[14].y, # Ring
                    list1[20].y < list1[18].y  # Pinky
                    ]

    index,middle,ring,pinky = finger_state[0],finger_state[1],finger_state[2],finger_state[3]
    
    if list1[5].x < list1[17].x:
        # Hand orientation puts the thumb on the LEFT side then check if thumb tip is on left 0f inner joint
        thumb = list1[4].x < list1[3].x 
    else:
        # Hand orientation puts the thumb on the RIGHT side then check if thumb tip is on right 0f inner joint        thumb = list1[4].x > list1[3].x
        thumb = list1[4].x > list1[3].x

    if all([index,pinky,thumb]) and not any([middle,ring]):
        return "That's cool bro, rock n all."
    elif middle and not any([thumb,index,ring,pinky]):
        return "Fuck u too. (from Akshat)"
    elif thumb and not any([index,middle,ring,pinky]):
        return "Thumbs up!"
    else:
        return ""