def text_to_binary(message):
    binary = ''.join(format(ord(char), '08b') for char in message)
    return binary

def calculate_capacity(image):

    height, width, _ = image.shape

    total_bits = height * width * 3

    total_chars = total_bits // 8

    return total_chars