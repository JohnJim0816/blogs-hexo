今天有人问了我一道题，如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330204930105.png#pic_center =400x300)
意思就是给定一个顺序为654321的栈，判断下面的栈是否是正确的。

## <font color=#00BCD4 >解题思路</font>
栈的元素存储与利用是遵循后进先出(LIFO)的，如下图，我们可以用一个半开口的方框表示栈，开口的一端称为栈顶，就是这端进行着压栈(push)和出栈(pop)操作。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330205711830.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5KaW0w,size_16,color_FFFFFF,t_70)
对于给定的待判断序列，比如这里的A选项453126，我们可以依次按照这个序列的顺序进行推演，
* 首先是第一个元素4，我们可以用这个元素"4"将原栈一分为二，即第一步，左边为原栈wt，右边为st_tmp，注意st_tmp开口方向相反。
* 然后我们先判断st的栈顶是否是当前遍历的元素"4"，如果是就pop掉，并遍历下一个元素"5"，如第二步，
* 按照相同操作我们来到第三步。此时遍历到元素"3"，此时左边st的栈顶并不等于元素"3"，因此我们需要从st_tmp中依次从栈顶找到并push到左边的st然后再pop掉，这一步可以简化为直接pop掉。
* 到了第四步遍历"1"时，我们发现左边st的栈顶也没有，右边st_tmp的栈顶也没有，此时我们就要逐次把st_tmp的栈顶push到左边，直到发现st_tmp的栈顶等于此时遍历的元素"1"为止。如果此时不幸pop掉了st_tmp中的所有元素也没有找到元素"1"，说明该序列并不是正确的序列
* 幸运的是这里还是找到了元素"1"并pop掉，如第六步
* 接下来的步骤都是类似的操作，如果最后成功pop掉st和st_tmp中的所有元素，说明该序列是正确的，即原栈654321可以通过一系列的push/pop步骤得到该序列。
## <font color=#00BCD4 >代码实现</font>
代码实现如下，这里不仅能实现654321的判断，还能实现其他个数比如4321的判断，只需要更改变量```n```即可
```python
class StackUnderflow(ValueError):
    '''自定义栈相关的异常类
    '''
    pass

class SStack:
    '''基于顺序表实现的栈类
    '''

    def __init__(self):
        self._elems = []  # 用list对象 _elems存储栈中元素

    def is_empty(self):
        return self._elems == []

    def top(self):  # 取得最后压入的元素，即栈顶
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        else:
            return self._elems[-1]

    def push(self, elem):  # 压栈
        self._elems.append(elem)

    def pop(self):  # 出栈
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

    def elems(self):
        elems = self._elems
        return elems


st = SStack()
flag = True
# n = int(input("栈元素个数:"))
n = 6 # n也可以改为其他的
for i in range(n, 0, -1):
    st.push(i)
st_tmp = SStack()
input_series = input("输入待判断序列")
series_list = list(map(int, input_series))
print(series_list)

while not st.top() == series_list[0]:  # 以待判断序列首元素为界，将原栈一分为二
    st_tmp.push(st.top())
    st.pop()

for serie in series_list:
    if (not st.is_empty()) and serie == st.top():
        st.pop()
    else:
        if st_tmp.is_empty():
            flag = False
        else:
            while not serie == st_tmp.top():
                st.push(st_tmp.top())
                st_tmp.pop()
                if st_tmp.is_empty():
                    break
            if st_tmp.is_empty():
                flag = False
            else:
                st_tmp.pop()
    if flag == False:
        break

print(flag)
```
## <font color=#00BCD4 >后记</font>
如果觉得本文有帮助，欢迎点赞+收藏以提供博主源源不断的更文动力。另外欢迎关注个人公众号，二维码如下：

![Alt](https://img-blog.csdnimg.cn/20200317165848597.png#pic_center =100x100)