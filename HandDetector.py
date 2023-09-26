import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon,
                                        self.trackingCon)  # Initialising here as done in the beginning
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:  # If hand is visible
            for handLms in self.results.multi_hand_landmarks:  # for a single hand
                if draw:  # agar draw karna ho to karo
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]  # made for only one hand, you can make for two
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()  # detector object of class

    while True:
        success, img = cap.read()

        img = detector.findHands(img)  # finding hand with the object
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        img = cv2.resize(img, (640, 360))
        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
