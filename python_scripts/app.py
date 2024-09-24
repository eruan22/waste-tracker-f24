import requests
import json

barcode = "3274080005003"

URL = "https://world.openfoodfacts.org/api/v0/product/" + barcode + ".json"

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