# BOX COLOR CHANGER ON FINGER TIP

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 360)
detector = HandDetector(detectionCon=0.8)
colorR = 255, 0, 0

while True:
    success, img = cap.read()  # Capture the video frame by frame
    img = cv2.flip(img, 1)  # 0 for vertical flip
    img = detector.findHands(img)  # find Hands
    lmList, _ = detector.findPosition(img)  # position of hands as well as boxes info

    if lmList:
        cursor = lmList[8]
        if 100 < cursor[0] < 200 and 100 < cursor[1] < 200:  # if fingertips comes here
            colorR = 0, 255, 0  # green
        else:
            colorR = 255, 0, 0  # blue

    cv2.rectangle(img, (100, 100), (200, 200), colorR, cv2.FILLED)

    # Display the resulting frame
    cv2.imshow("frame", img)

    # the 'q' button is set as the quitting button you may use any desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()
