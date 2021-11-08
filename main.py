import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys1 = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["caps off","A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

keys2 = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
         ["caps on","a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
         ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]]

class Button():
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.size = size
        self.text = text

    def drawAll(img, keys):
        for myButton in keys:
            x, y = button.pos
            w, h = button.size

    def draw(self, img):
        cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, "Q", (115, 180), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        return img

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    myButton = Button([100, 100], "Q")
    img = myButton.draw(img)

    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()