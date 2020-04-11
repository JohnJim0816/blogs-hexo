---
title: python3画动态图并保存视频
date: 2020-04-10 21:29:41
categories: python3
tags: 
    - python3
---

![](https://raw.githubusercontent.com/JohnJim0816/blog-figures/master/2020/4/11/python画动态图并保存视频-封面.jpeg)

## ion()画动态图
可以参考[网页](https://www.omegaxyz.com/2018/06/03/python-matplotlib-dynamic-graph/)，具体示例如下：
```python
import numpy as np
import matplotlib.pyplot as plt
 
plt.axis([0, 100, 0, 1])
plt.ion()
 
xs = [0, 0]
ys = [1, 1]
 
for i in range(100):
    y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys) 
    plt.pause(0.1)
```
<!-- more -->
## 保存视频
需要安装FFMpegWriter，MAC```brew install FFMpegWriter```，ubuntu```sudo apt-get install FFMpegWriter```。在ion()的基础上示例代码如下:
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

metadata = dict(title='Movie Test', artist='Matplotlib',comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()

with writer.saving(fig, "writer_test.mp4", 100):  # 100指的dpi，dot per inch，表示清晰度

    plt.axis([0, 100, 0, 1])
    plt.ion()
    
    xs = [0, 0]
    ys = [1, 1]
    
    for i in range(100):
        y = np.random.random()
        xs[0] = xs[1]
        ys[0] = ys[1]
        xs[1] = i
        ys[1] = y
        plt.plot(xs, ys)
        plt.pause(0.1)
        writer.grab_frame()
```