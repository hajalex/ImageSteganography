# Steganography
The field of information security is regarded as being essential in the digital world, and its demand is growing daily.
One of the security measures used when exchanging information is cryptography.
The goal of cryptography is to conceal communication, in the sense that it conceals information in a digital medium to avoid raising suspicions about the presence of information there.

# Steganography in image
is the process of concealing private information or messages within digital images without changing their exterior appearance.
Steganography in photos primarily aims to hide the presence of the hidden data while preserving the usability and quality of the image.

This procedure includes modifying the RGB values or the least significant bits (LSB) of the pixels of a digital image in order to embed information, typically plaintext, into the image files.
Since it affects the tiniest amount of information in a pixel and is not visible to humans, the modifications are made in a way that does not significantly alter the image's quality or appearance. 

# Image Steganography

This Python script enables you to hide messages within images using a simple steganography technique. It encodes messages into the least significant bits of the image pixels, making the changes almost imperceptible to the human eye.

## How It Works

The script provides two main functionalities: encoding a message into an image and decoding a hidden message from an image.

### Encoding

1. Run the script and choose the **Encode** option.
2. Provide the name of the input image (make sure it's in the same directory).
3. Enter the message you want to hide within the image.
4. Provide the desired name for the encoded image.

The script will encode the message into the image, creating an encoded version of the image that contains the hidden message.

### Decoding

1. Run the script and choose the **Decode** option.
2. Provide the name of the encoded image (make sure it's in the same directory).

The script will extract the hidden message from the encoded image and display it.

## Getting Started

1. Clone this repository to your local machine using `git clone https://github.com/your-username/Image-Steganography.git`.
2. Make sure you have Python and the required libraries installed (`cv2`, `numpy`, `PIL`).
3. Run the script using `python steganography.py`.
