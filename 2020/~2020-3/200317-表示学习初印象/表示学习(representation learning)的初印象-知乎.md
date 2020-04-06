## <font color=#00BCD4 >0 写在前面</font>
表示学习(**representation learning**)是深度学习领域中一个比较重要的方面，本文则提供对表示学习的一个定性理解。原文转自本人的[CSDN](https://blog.csdn.net/JohnJim0/article/details/104833122)
## <font color=#00BCD4 >1 什么是表示？</font>
要清楚什么是表示(representation)学习，就得先知道什么是representation。在《deep learning with
python》一书的1.1.3节中是这么定义的，At its core, it’s a different way to look at data—**to represent or encode data**。这个字面上理解就是表示或者编码数据的一种形式。举个例子，一张图片可以表示为RGB形式也可以表示为HSV形式，这就是对同一数据(data)的两种不同表示。在不同的任务中采取合适的表示会使得任务变得简单一点，比如如果要选取图片中的红色像素点，我们就可以采取RGB形式，如果想让图片更加饱和(saturated)，那么采取HSV形式更加简单。又比如说我们要辨别一种鸟类，我们可以使用它的眼睛颜色-羽毛颜色-尾巴形状(这些特征是笔者随便想的，不一定能实际用于分类)作为它的数据，也可以使用脚趾形状-羽毛颜色-尾巴形状作为数据，而眼睛颜色等也是鸟的特征，所以表示学习又叫特征学习(feature learning)。
## <font color=#00BCD4 >2 表示学习？</font>
为了更好地理解什么是表示学习？可以参考[知乎](https://www.zhihu.com/question/37162929)的一篇回答。如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200313080053207.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)
即稍微入门一点机器学习的都知道传统地做法都人为地设计特征或者说使用已经完全标记好的数据来试图接近最好的分类效果。但实际上很多未标记的或者说标记相对较少的训练数据，我们当然可以人为标记，但也可以自动地筛选出比较重要的特征，有点类似于**PCA(主成分分析)**的思路，这就是表示学习或者说特征学习。

表示学习虽然从结构上讲只是数据的一个预处理手段，但是正如“工欲善其事，必先利其器”一样，它的出现提供了进行无监督学习和半监督学习的一种方法。其重要性不言而喻，以至于在花书中被单独列出来作为一章。表示学习一个比较典型的方法就是**自编码器**，有兴趣的可以自查。

## <font color=#00BCD4 >3 参考资料</font>
[1] [知乎](https://www.zhihu.com/question/37162929)
[2]  repesentation learning维基百科
[3]  *deep learning with python*, François Chollet
[4]  *深度学习*(中文版)，伊恩*古德费洛