import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import math

image_name = "image.jpg"
watermark_text = "copyright @JX"
window_size = (800, 800)



def add_watermark(image):
    drawing = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=50)
    drawing.text(watermark_location, watermark_text, fill=(255, 255, 255, 128), font=font)
    return image


def resize_image(image, max_size):
    image.thumbnail(max_size, Image.LANCZOS)
    return image


root = tk.Tk()
img = Image.open(image_name).convert('RGBA')
img_width, img_height = img.size
watermark_location = (img_width*0.5, img_height*0.95)
watermark_img = add_watermark(img)
resize_image(watermark_img, window_size)

canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack(side='left', fill='both', expand=True)

tk_img = ImageTk.PhotoImage(watermark_img)
canvas.create_image(0, 0, anchor='nw', image=tk_img)
canvas.config(scrollregion=canvas.bbox('all'))
root.update_idletasks()

root.mainloop()
