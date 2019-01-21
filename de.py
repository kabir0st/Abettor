import qrcode

def run():
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )
    data = "9559ebf7fa3f4e6d83ea504242bd8415"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("image.jpg")

if __name__ == "__main__":
    run()