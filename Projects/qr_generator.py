import qrcode

# 1. Define the data to be encoded
data = "https://www.facebook.com/profile.php?id=61570740825278&mibextid=ZbWKwL"

# 2. Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# 3. Add data to the QR Code object
qr.add_data(data)
qr.make(fit=True)

# 4. Create the image of the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# 5. Save the image
qr_image.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")
