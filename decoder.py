import cv2

def decode_image(image_path):

    image = cv2.imread(image_path)

    binary_data = ""

    for row in image:
        for pixel in row:

            for channel in range(3):
                binary_data += format(pixel[channel], '08b')[-1]

    all_bytes = [
        binary_data[i:i+8]
        for i in range(0, len(binary_data), 8)
    ]

    decoded_message = ""

    for byte in all_bytes:

        if byte == '11111110':
            break

        decoded_message += chr(int(byte, 2))

    return decoded_message