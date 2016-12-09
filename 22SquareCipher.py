#!/usr/bin/python
# coding: utf-8

from PIL import Image
import subprocess

cipher_raw = open("SquareCipher.txt", "r")
cipher_list = list(cipher_raw)
num_lines = len(cipher_list)
canvas_size = 5 * num_lines

img_black_5x5 = Image.open("Black_5x5.png", "r")
img_white_5x5 = Image.open("White_5x5.png", "r")

canvas = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))

for i in range(num_lines):
	for j in range(num_lines):
		if cipher_list[i][j].isupper():
			canvas.paste(img_black_5x5, (i*5, j*5))
		else:
			canvas.paste(img_white_5x5, (i*5, j*5))

canvas.save("canvas1.png", 'png', quality=100, optimize=False)

for i in range(num_lines):
	for j in range(num_lines):
		if cipher_list[i][j].isupper():
			canvas.paste(img_black_5x5, (i*5, j*5))
		else:
			canvas.paste(img_white_5x5, (i*5, j*5))

canvas.save("canvas2.png", 'png', quality=100, optimize=False)

subprocess.call(["eog", "canvas1.png"])
subprocess.call(["eog", "canvas2.png"])
