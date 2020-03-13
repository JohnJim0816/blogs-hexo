## 读取图像像素RGB值

from PIL import Image

imload= Image.open('test.jpg')
im=imload.convert("RGB")
width,height=im.size
demo=open('rgb.txt','a')

for y in range(height):
    for x in range(width):
        rgb=im.getpixel((x,y))
        rgb=str(rgb)
        demo.write(rgb[1:-1]+"\t")
    demo.write("\n")
demo.close()