from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
import serial
import time

cap = cv.VideoCapture(0)
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

puerto_serie = serial.Serial('/dev/rfcomm0', 9600)
datos_a_enviar = ""

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    #lmList, bbox = detector.findPosition(img)
    if hands:
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        #print(f'H1 = {fingers1.count(1)}', end=" ")

        if len(hands) == 2:
            hand2 = hands[1]  # Get the first hand detected
            lmList2 = hand2["lmList"]  # List of 21 landmarks for the first hand
            bbox2 = hand2["bbox"]  # Bounding box around the first hand (x,y,w,h    coordinates)
            center2 = hand1['center']  # Center coordinates of the first hand
            handType2= hand1["type"]
            fingers2 = detector.fingersUp(hand1)

 
    
    if(len(hands) == 2):
        datos_a_enviar = "Two"
        puerto_serie.write(datos_a_enviar.encode('utf-8'))
    elif (len(hands) == 1):
        datos_a_enviar = "One"
        puerto_serie.write(datos_a_enviar.encode('utf-8'))
    else:
        datos_a_enviar = "Nada"
        puerto_serie.write(datos_a_enviar.encode('utf-8'))
    cv.imshow("Image",img)
    cv.waitKey(1)





