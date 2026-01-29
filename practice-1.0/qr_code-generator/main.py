'''
We are going to use a python library called qrcode and convert url to qr
'''

import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

try:
    img = qrcode.make(url)
    img.save(filename)
except Exception as e:
    print(f"An error occurred: {e}")