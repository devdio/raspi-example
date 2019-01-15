# -*- coding: utf-8 -*-
import zbar
import PIL.Image

file = './qr01.png'

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

# greyscale L
pil = PIL.Image.open(file).convert('L')
(width, height) = pil.size

# Return image as a bytes object
raw = pil.tobytes()

# The Y800 color format is an 8 bit monochrome format.
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

for symbol in image:
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

del(image)





