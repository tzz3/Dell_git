from PIL import Image


c = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
	if alpha == 0:
		return ' '
	length = len(c)
	gray = int(0.1 * r + 0.2 * g + 0.7 * b)
	unit = 256.0 / length
	return c[int(gray / unit)]


if __name__ == '__main__':
	w = 50  # 宽度
	h = 37  # 高度
	img = 'dl.png'
	im = Image.open(img)
	im = im.resize((w, h))
	# print(im)
	txt = ""
	for i in range(h):
		for j in range(w):
			txt += get_char(*im.getpixel((j, i)))
		txt += '\n'

	print(txt)
	# 字符画输出到文件
	with open("output.txt", 'w') as f:
		f.write(txt)
