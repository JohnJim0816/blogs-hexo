# 先将jpg图像转成rgb值
写一个python脚本，注意安装pillow包，如下：
```python
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
```
然后会生成一个"rgb.txt" 
# 
打开Excel，然后打开"rgb.txt"，这时候会提示更改格式窗口，不管它直接完成  
设置单元格列宽，使单元格为正方形，大约值为2

新建一个Set_RGB宏，复制以下代码，注意更改最大列标，以及去掉"//"在内的注释
```bash
Sub Set_RGB()
    Dim r As Range,arr
    For Each r In Range("A:xxx")  //xxx为最大列标，点击一个格子然后ctrl+方向右键就能跳到最大列
        arr = Split(R,",")
        r.Interior.Color = RGB(CInt(arr(0)),CInt(arr(1)),CInt(arr(2)))
    Next
End Sub
```
然后运行，可能会出现下标越界等情况，不管它，直接回到excel就会发现已经生成



