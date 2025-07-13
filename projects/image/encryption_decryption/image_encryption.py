from PIL import Image

img = Image.open("files\\image_for_handout.jpg")
#en_de_V_crypt_code = int(img.size[0]/2)  # vertical middle of image
en_de_H_crypt_code = int(img.size[1]/2)  # horizontal middle of image

char_password = "it is the root password"
decimal_password = []
for c in char_password:
    decimal_password.append(ord(c))

how_many_pixels_in_row = int(img.size[0]/len(decimal_password)+1)
#how_many_pixels_in_col = int(img.size[1]/len(decimal_password)+1)

'''  multi lines :
for y in range(0, img.size[1], how_many_pixels_in_col):
    dec_pass_cnt = 0
    for x in range(0, img.size[0], how_many_pixels_in_row):
        img.putpixel((x,y), (decimal_password[dec_pass_cnt],decimal_password[dec_pass_cnt],0))
        dec_pass_cnt+=1  '''

''' vertical encryption :
dec_pass_cnt = 0
for y in range(0, img.size[1], how_many_pixels_in_col):
    img.putpixel((en_de_V_crypt_code, y), (decimal_password[dec_pass_cnt],decimal_password[dec_pass_cnt],0))
    dec_pass_cnt+=1 '''

# horizontal encryption
dec_pass_cnt = 0
for x in range(0, img.size[0], how_many_pixels_in_row):
    img.putpixel((x, en_de_H_crypt_code), (decimal_password[dec_pass_cnt],decimal_password[dec_pass_cnt],0))
    dec_pass_cnt+=1

img.save("files\\encrypted_image.png")
img.show()
img.close()
#MadMad_37