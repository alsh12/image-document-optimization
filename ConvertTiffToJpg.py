from PIL import Image
im = Image.open('./Tiffs/sample.tiff')
im.save('./ConvertedImages/tifftojpg.jpeg')
