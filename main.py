
# encryption text in image (method 1)

# from stegano import lsb
#
# secret = lsb.hide( "img/1.png", "Secret information or password: 0011 " )
# secret.save("img/1_secret.png")
#
# result = lsb.reveal("img/1_secret.png")
#
# print(result)
#


# encryption text in image (method 2)

# from stegano import exifHeader
#
# secret = exifHeader.hide("img/2.jpg", "img/2_secret.jpg", "Секретная скрытая информация по срокам и датам")
#
# result = exifHeader.reveal("img/2_secret.jpg")
# result = result.decode()
# print(result)

# encryption text in image (method 3)
# pip install wheel steganocryptopy

from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/3.png", "secret_text.txt")
secret.save("img/3_secret.png")

result = Steganography.decrypt("key.key", "img/3_secret.png")
print(result)
