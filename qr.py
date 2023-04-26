from turtle import fillcolor
import qrcode
from PIL import Image

Logo_link = 'logo.png'

#logo = Image.open('C:\Users\alxyg\Downloads\pdf2png(1)\LOGO PEQUEÑA.pdf')
logo = Image.open(Logo_link)

basewidth = 100

wpcenter = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpcenter)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

url = 'https://www.turismopequena.com.mx/'

QRcode.add_data(url)

QRcode.make()

QRcolor = 'Black'

QRimg = QRcode.make_image(
    fillcolor=QRcolor, back_color="white").convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
QRimg.save('gfg_QR.png')
print('QR code generated!')