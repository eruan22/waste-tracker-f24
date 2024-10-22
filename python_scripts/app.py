import requests
import json
import cv2
from pyzbar.pyzbar import decode

def get_barcode():
    cap = cv2.VideoCapture(0)
    # width
    cap.set(3, 640)
    #height
    cap.set(4, 480)
    camera = True

    barcode = ""
    confirm_count = 0
    confirm_limit = 10

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
    
    return barcode

def get_packaging_info():
    URL = "https://world.openfoodfacts.org/api/v0/product/" + get_barcode() + ".json"

    #make api request
    r = requests.get(url=URL)

    data = r.json()

    if data and 'product' in data:
        product = data['product']
        packaging = product.get('packaging', None)  # Safely get 'packaging'


        if packaging:
            print(packaging)
        else:
            print("packaging key not found.")
            print(None)
    else:
        print("product data not available.")
        print(None)


def main():
    get_packaging_info()

if __name__ == "__main__":
    main()