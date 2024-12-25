# qr code genrate using python
# example 1
import qrcode
data = "https://www.instagram.com/codemoji.telugu/"
qr = qrcode.make(data)
qr.save("codemoji.png")
print("QR code generated and saved as 'codemoji.png'



# example 2

import qrcode
data = "https://mail.google.com/mail/u/0/#inbox/yalamsai77@gmail.com/"
qr = qrcode.make(data)
qr.save("ysai.png")
print("QR code generated and saved as 'ysaipng'")









