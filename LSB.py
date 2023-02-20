import cv2
import numpy as np
from PIL import Image


# ============================================================================= #


def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p


# ============================================================================= #


def hidedata(img, data):
    data += "$$"
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


# ============================================================================= #


def encode():
    img_name = input("\Enter image name:")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input('\Enter msg:')
    if data == 0:
        raise ValueError('Empty data')
    enc_img = input("\enter encoded image:")
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h), Image.ANTIALIAS)
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)


# ============================================================================= #


def find_data(img):
    bin_data = ''
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]
    all_bytes = [bin_data[i:i+8]for i in range(0, len(bin_data), 8)]

    readable_data = ''
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break

    return readable_data[:-2]

# ============================================================================= #


def decode():
    image_name = input('\Enter image name :')
    image = cv2.imread(image_name)
    img = Image.open(image_name, 'r')
    msg = find_data(image)
    return msg

# ============================================================================= #


def steganography():

    print('''\nimage stego 
            1.encode 
            2.decode''')
    u_in = int(input('\n your num?'))
    if u_in == 1:
        encode()
    else:
        ans = decode()
        print('\n your msg :'+ans)


steganography()