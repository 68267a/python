import os
from PIL import Image # Pillow module

DPI = 600 # dots per inch. 300 default
LPI = 60  # lines per inch, taken from the lens design

ima = Image.open(r"batman.png")
imb = Image.open(r"darthvader.png")
outfile = 'batvader'

if ima.width != imb.width or ima.height != imb.height:
	print('ERROR: Please choose images that are the same size')
	raise SystemExit

stripwidth = int(ima.width / (ima.width / DPI * LPI))
numstrips = ima.width / stripwidth

os.chdir(os.path.dirname(os.path.abspath(__file__)))
outfile += "_" + str(DPI) + "-" + str(stripwidth) + '.png'
print("file: " + outfile + "\nwidth: " + str(2*ima.width)+ "\nstripwidth: " + str(stripwidth) + "\nnumstrips: " + str(numstrips))

strip = 0
h = ima.height
x = 0
y = stripwidth

imgOut = Image.new("RGB", (ima.width, ima.height), "black")
while strip < numstrips:
	# print("strip" + str(strip) + " x" + str(x) + " y" + str(y))
	strip_a = ima.crop((x,0,y,h))
	strip_b = imb.crop((x,0,y,h))
	imgOut.paste(strip_a,(x,0))
	imgOut.paste(strip_b,(x+stripwidth,0))
	x=x+stripwidth+stripwidth
	y=y+stripwidth+stripwidth
	strip += 1

imgOut.save(outfile)
ima.close
imb.close