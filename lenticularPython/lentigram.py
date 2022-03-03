import os
from PIL import Image # Pillow module

DPI = 360 # dots per inch. 300 default
LPI = 60  # lines per inch, taken from the lens design

# Conversions
# length[mm] = pixel * 25.4mm (1 in) / dpi
# pixel = dpi * mm / 25.4 mm (1 in)
# dpi = pixel * 25.4 mm (1 in) / mm
# i2cm = 25.4 #inch to cm
# DPcm = DPI / i2cm # Dots per cm  () # WHY?
# LPcm = LPI / i2cm # lines per cm () # WHY?

ima = Image.open(r"black.png")
imb = Image.open(r"white.png")
width, height = ima.size
stripwidth = 10
numstrips = round(width/stripwidth)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
outfile = 'batvader_' + str(stripwidth) + '.png'
print("width " + str(width)+ " stripwidth " + str(stripwidth))
strip = 0
h = height
x = 0
y = stripwidth

imgOut = Image.new("RGB", (width, height), "black")
while strip < numstrips:
	print("strip" + str(strip) + " x" + str(x) + " y" + str(y))
	strip_a = ima.crop((x,0,y,h))
	strip_b = imb.crop((x,0,y,h))
	imgOut.paste(strip_a,(x,0))
	imgOut.paste(strip_b,(x+stripwidth,0))
	x=x+stripwidth+stripwidth
	y=y+stripwidth+stripwidth
	strip += 1


imgOut.save(outfile)
