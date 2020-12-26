from PIL import Image,ImageEnhance
im = Image.open('test2.jpg')
im.show()
enh = ImageEnhance.Contrast(im)
enh.enhance(1.8).show("30% more contrast")
