import cv2
from utils import text_to_binary
from visualizer import show_difference

def encode_image(image_path, secret_message):

    original_image = cv2.imread(image_path)     # original image
    image = cv2.imread(image_path)

    binary_message = text_to_binary(secret_message)
    binary_message += '1111111111111110'

    data_index = 0

    for row in image:
        for pixel in row:

            for channel in range(3):

                if data_index < len(binary_message):

                    pixel[channel] = int(
                        format(pixel[channel], '08b')[:-1]
                        + binary_message[data_index],
                        2
                    )

                    data_index += 1

    cv2.imwrite("images/output/encoded.png", image)

    print("Message Hidden Successfully")
    show_difference(image_path, "images/output/encoded.png")