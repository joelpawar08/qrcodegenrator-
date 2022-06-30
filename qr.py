import pyqrcode
import png
from pyqrcode import QRCode

string = input("Enter your Link to genrate QR Code ")
print("QR Genrated Check in the same Folder ")
url = pyqrcode.create(string)
url.svg("myqr.svg" , scale = 8)
url.png('myqr.png', scale =6)
QRcolor = "green"