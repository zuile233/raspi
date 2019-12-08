from pcf8591 import *
from time import sleep
from random import randint

#oled setup
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
font=ImageFont.truetype("LiberationSans-Regular.ttf",15)


#pcf8591 setup
setup(0x48)

foodx=randint(1,60)*2
foody=randint(2,28)
food=(foodx,foody,foodx+2,foody+1)

xx=64
yy=16
x=0
y=0
size=1

draw.rectangle((foodx,foody,foodx+2,foody+1), outline=255, fill=255)


while True:
    readx=read(0)
    ready=read(1)
    
    if ready<100:
        y=-1
    elif ready>200:
        y=1
    else:
        y=0
    if readx<100:
        x=-1
    elif readx>200:
        x=1
    else:
        x=0
    xx=xx+2*x
    yy=yy+y
    
    if xx<=1 or yy<=1 or xx+2*size>=127 or yy+size>=31:
        draw.text((0, 0), "Game",  font=font, fill=255)
        draw.text((0, 16), "Over",  font=font, fill=255)
        #oled setup end !!!should be in while
        disp.image(image)
        disp.display()
        break
    if xx<=foodx and yy<=foody and xx+2*size>=foodx+2 and yy+size>=foody+1:
        size+=1
        foodx=randint(1,60)*2
        foody=randint(2,28)
        food=(foodx,foody,foodx+2,foody+1)
        
        
        
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.rectangle((0,0,width-1,height-1), outline=255, fill=0)
    draw.rectangle(food, outline=255, fill=255)
    draw.rectangle((xx,yy,xx+2*size,yy+size), outline=255, fill=255)
    #oled setup end !!!should be in while
    disp.image(image)
    disp.display()
    
    sleep(0.05)
