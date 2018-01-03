from PIL import Image
w = 50  # 宽度
h = 37  # 高度
img = 'dl.png'
im = Image.open(img)
im = im.resize((w, h), Image.NEAREST)
# print(im.getpixel((20, 20)))

a = [1,2,3]
print(*a)