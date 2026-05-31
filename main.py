from tkinter import *
from tkinter import filedialog
from encoder import encode_image
from decoder import decode_image

root = Tk()

root.title("Image Steganography Tool")
root.geometry("500x400")

selected_image = ""

def choose_image():
    global selected_image

    selected_image = filedialog.askopenfilename()

def encode():

    message = text_box.get("1.0", END)

    encode_image(selected_image, message)

def decode():

    hidden = decode_image(selected_image)

    result_label.config(text=hidden)

Button(root, text="Choose Image", command=choose_image).pack()

text_box = Text(root, height=10)
text_box.pack()

Button(root, text="Encode", command=encode).pack()

Button(root, text="Decode", command=decode).pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()