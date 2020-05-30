import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2(history = 50, varThreshold = 16, detectShadows = False)

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame,learningRate = -1)

    imgResult = cv2.bitwise_and(frame,frame,mask=fgmask)
    cv2.imshow('frame',fgmask)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & ord('q')==0xff:
        break

cap.release()
cv2.destroyAllWindows()