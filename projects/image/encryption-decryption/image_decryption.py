from PIL import Image
from time import sleep
from string import ascii_letters
from image_encryption import how_many_pixels_in_row, en_de_H_crypt_code  # horizontal decryption
#from image_encryption import how_many_pixels_in_col, en_de_V_crypt_code  # vertical decryption

enc_img = Image.open("files\encrypted_image.png")

decrypted_password = ""

''' vertical middle pass :
for y in range(0, enc_img.size[1], how_many_pixels_in_col):
    decrypted_password += chr(enc_img.getpixel((en_de_V_crypt_code, y))[0])'''

print(decrypted_password)
for x in range(0, enc_img.size[0], how_many_pixels_in_row):
    decrypted_password += chr(enc_img.getpixel((x, en_de_H_crypt_code))[0])


alphabets = ascii_letters + ' '   # ' ' + ascii_letters
founded = ""

for password in decrypted_password:
    for char in alphabets:
        if char == password:
            founded+=char
            print(founded)
            break
        print(founded+char)
        sleep(0.03)
print(f"\n\npassword is : '{founded}'\n\n\n")

enc_img.close()
#MadMad_34