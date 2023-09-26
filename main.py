import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
colorB = (83, 181, 237)
rectangleSize = [200,200]
cx, cy, w, h = 100, 100, 200, 200


class DragRect():
    def __init__(self, posCenter, size=rectangleSize):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


rectList = []
for x in range(5):
    rectList.append(DragRect([x * 250 + 150, 150]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l, _, _ = detector.findDistance(8, 12, img, draw=False)
        print(l)
        if l < 30:
            cursor = lmList[8]  # index finger tip landmark
            for rect in rectList: # call the update here
                rect.update(cursor)

    ## Solid rectangle Section
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), (255, 0, 255), cv2.FILLED)
        cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    ## Transperent Rectangles Section
    # imgNew = np.zeros_like(img, np.uint8)
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w, h = rect.size
    #     cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
    #                   (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
    #     cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    out = img.copy()

    ## Transperent Rectangles Section
    # alpha = 0.5
    # mask = imgNew.astype(bool)
    # out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    cv2.imshow("Image", out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()