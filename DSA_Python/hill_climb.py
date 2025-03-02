import sys
import cv2
import mediapipe as mp
import pydirectinput as p1
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    sys.exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
draw = mp.solutions.drawing_utils

def handLandmarks(colorImg):
    landmarkList = []
    landmarkPositions = hands.process(colorImg)
    landmarkCheck = landmarkPositions.multi_hand_landmarks
    if landmarkCheck:
        for hand in landmarkCheck:
            draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
            h, w, c = img.shape
            for index, landmark in enumerate(hand.landmark):
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([index, centerX, centerY])
    return landmarkList

def fingers(landmarks):
    isPalm = False
    isRightFinger = False
    tipIds = [4, 8, 12, 16, 20]  # Indexes for thumb and fingertips

    # Check for a full palm (all fingers spread)
    if all(landmarks[tipId][2] < landmarks[tipId - 2][2] for tipId in tipIds[1:]):
        isPalm = True  # Full palm detected

    # Check for right arrow (index finger up)
    if landmarks[tipIds[1]][2] < landmarks[tipIds[1] - 2][2]:  # Index finger is up
        isRightFinger = True  # Right arrow condition met

    return isPalm, isRightFinger

while True:
    check, img = cap.read()
    if not check:
        print("Failed to read from camera")
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lmList = handLandmarks(imgRGB)

    if len(lmList) != 0:
        isPalm, isRightFinger = fingers(lmList)

        # Control car movement
        if isPalm:  # Full palm detected
            p1.keyDown("left")  # Press left arrow key
            p1.keyUp("right")  # Ensure right key is released
        elif isRightFinger:  # Right arrow detected (index finger up)
            p1.keyDown("right")  # Move car forward
            p1.keyUp("left")  # Ensure left key is released
        else:
            p1.keyUp("left")  # Release left key if no palm
            p1.keyUp("right")  # Release right key if no index finger

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

try:
    cap.release()
except Exception as e:
    print(f"Error releasing camera: {e}")
    sys.exit()
cv2.destroyAllWindows()
