import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
# width
cap.set(3, 640)
#height
cap.set(4, 480)
camera = True

barcode = ""
confirm_count = 0
confirm_limit = 20

while camera == True:
    success, frame = cap.read()
       
    if confirm_count == confirm_limit:
        break

    for code in decode(frame):
        print(code.data.decode("utf-8"))

        if code.data.decode("utf-8") != barcode:
            barcode = code.data.decode("utf-8")
            confirm_count = 0
        else:
            confirm_count += 1
        
    cv2.imshow("Testing-code-scan", frame)
    cv2.waitKey(1)

print("Barcode:", barcode)