from PIL import Image, ImageChops, ImageFilter

SOURCE_DIR = 'photos/'

# pict1 = Image.open(SOURCE_DIR + '123.jpeg')
# ava = pict1.crop((0, 0, pict1.width, pict1.width)).resize((700, 700)).transpose(Image.FLIP_LEFT_RIGHT)
# ava.save(SOURCE_DIR + 'ava.jpeg')
# ava.show()

# first = Image.open(SOURCE_DIR + '123.jpeg')
# back = Image.open(SOURCE_DIR + 'ava.jpeg')
#
# r, g, b = first.split()

# r.show()
# b.show()
# g.show()

ava = Image.open(SOURCE_DIR + 'ava.jpeg')
my = Image.open(SOURCE_DIR + 'my_photo.jpeg')

# result = ImageChops.add(ava, my, scale=1.5, offset=5)
# result.save('myst.jpeg')
# result.show()
# result = ImageChops.darker(ava, my)
# result.show()
# result = ImageChops.difference(ava, my)
# result.show()
# result = ImageChops.lighter(ava, my)
# result.show()

r, g, b = ava.split()
img1 = Image.merge('RGB', (r, g, b))
img2 = Image.merge('RGB', (r, g.filter(ImageFilter.GaussianBlur(25)), b))
ava.show()
img1.show()
img2.show()