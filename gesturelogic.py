import math

def distance(node,wrist,width,height):
    return math.hypot((node.x - wrist.x)*width , (node.y - wrist.y) * height)

def finger_states(hand_landmarks,w,h):
    #get coordinates of all points
    list1 = list(hand_landmarks.landmark)
    finger_state = []
    wrist = list1[0]

    '''{
        [6] is index finger first bend joint , [8] is index finger tip,
        [10] is index middle first bend joint , [12] is index middle tip,
        [14] is index ring first bend joint , [16] is index ring tip,
        [18] is index pinky first bend joint , [20] is index pinky tip,

        each contains x and y coords.
    }'''
    #1 means finger extended , 0 means finger retracted
    nodes = [(8,6),(12,10),(16,14),(20,18)]
    for i in nodes:
        finger_state.append(distance(list1[i[0]],wrist,w,h) > distance(list1[i[1]],wrist,w,h))

    thumb = distance(list1[4],list1[17],w,h)>distance(list1[3],list1[17],w,h)
    finger_state.append(thumb)

    return finger_state

def handsgesture(hand_landmarks,w,h):
    index,middle,ring,pinky,thumb = finger_states(hand_landmarks,w,h)
    
    if index and not any([middle,ring,pinky,thumb]):
        return 1
    elif all([index,middle]) and not any([ring,pinky,thumb]):
        return 2
    elif all([index,middle,ring]) and not any([pinky,thumb]):
        return 3
    elif all([index,middle,ring,pinky]) and not thumb:
        return 4
    elif all([index,middle,ring,pinky,thumb]): return 5
    elif not any([index,middle,ring,pinky,thumb]): return 0
    #undefined gesture
    return -1

def signs(hand_landmarks,w,h):
    index,middle,ring,pinky,thumb = finger_states(hand_landmarks,w,h)

    if all([index,middle,ring,pinky,thumb]):
        return "HELLO !!"
    else:
        return ""