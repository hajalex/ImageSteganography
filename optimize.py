import cv2
import numpy as np
from PIL import Image


# Function to convert data to binary format
def data2binary(data):
    if type(data) == str:
        binary_data = ''.join([format(ord(i), '08b') for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        binary_data = [format(i, '08b') for i in data]
    return binary_data


# Function to hide data within an image
def hide_data(img, data):
    data += "$$"  # Mark the end of the data
    data_index = 0
    binary_data = data2binary(data)
    data_length = len(binary_data)

    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if data_index < data_length:
                pix[0] = int(r[:-1] + binary_data[data_index])
                data_index += 1
            if data_index < data_length:
                pix[1] = int(g[:-1] + binary_data[data_index])
                data_index += 1
            if data_index < data_length:
                pix[2] = int(b[:-1] + binary_data[data_index])
                data_index += 1
            if data_index >= data_length:
                break
    return img


# Function to encode the data into an image
def encode():
    img_name = input("Enter image name: ")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input('Enter message: ')
    if data == 0:
        raise ValueError('Empty data')
    enc_img = input("Enter encoded image name: ")
    enc_data = hide_data(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h), Image.ANTIALIAS)
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)


# Function to extract hidden data from an image
def find_data(img):
    binary_data = ''
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]

    readable_data = ''
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break

    return readable_data[:-2]


# Function to decode the hidden data from an image
def decode():
    image_name = input('Enter image name: ')
    image = cv2.imread(image_name)
    msg = find_data(image)
    return msg


# Main function to manage steganography operations
def steganography():
    print('''\nImage Steganography
            1. Encode
            2. Decode''')
    user_input = int(input('\nYour choice? '))
    
    if user_input == 1:
        encode()
    else:
        hidden_msg = decode()
        print('\nYour hidden message:', hidden_msg)


# Call the steganography function to begin
steganography()
