import qrcode

# QR code 1: name or short message
message = input("Enter your name or a short message: ").strip()
qrcode.make(message).save("my_name_qrcode.png")
print("QR code saved as my_name_qrcode.png")

# QR code 2: favorite website
website = input("Enter your favorite website URL: ").strip()
qrcode.make(website).save("https://hiddennepal.vercel.app/my_website_qrcode.png")
print("QR code saved as my_website_qrcode.png")

print("Open the images and scan them with your phone to check the contents.")