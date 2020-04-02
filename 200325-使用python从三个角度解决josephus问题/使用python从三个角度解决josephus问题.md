## <font color=#00BCD4 >0 写在前面</font>
josephus问题是数据结构教材中的一个常见实例，其问题可以描述为：
>设$n$个人围坐一圈，现在要求从第$k$个人开始报数，报到第$m$个的人退出。然后从下一个人开始继续按照同样规则报数并退出，直到所有人退出为止。要求按照顺序输出每个人的序列号。
## <font color=#00BCD4 >1 基于数组概念的解法</font>
首先考虑基于python的list和固定大小的数组概念，即将list看作元素个数固定的对象，只改变值而不删除元素，相当于摆了一圈$n$把椅子，人虽然退出但是椅子还在，我们可以给每个人从$1$到$n$编号，没有人的位置用$0$表示，思路如下：
* 初始
建立包含$n$个人(编号)的list
找到第$k$个人开始
* 运行
从$k$的位置开始数到$m$，中间遇到$0$的就跳过
数到$m$之后，将其值改为$0$
然后继续循环，总共循环$n$次(因为每次循环就会退出一个人)

代码如下：
```python
def josephus_A(n, k, m):
    people = list(range(1, (n+1)))
    i = k-1
    for num in range(n):
        count = 0
        while count < m: 
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end=" ")
                people[i] = 0
            i = (i+1) % n # count只是flag，真正记的数是i
        if num < n-1:
            print(end=",", )
        else:
            print(" ")
```
## <font color=#00BCD4 >2 基于顺序表的解法</font>
顺序表是线性表的一种，即表中元素放在一块足够大的连续存储区里，首元素存入存储区开始位置，其余元素依次存放。顺序表在python中的也是list，跟第一种解法不同，当第$m$个人退出需要进行删除元素的操作，才是顺序表。而第一种解法的数组想要删除并不是那么容易，这里是因为python中没有内置对数组的支持，所以用list代替，具体可以参照c++中的数组，如果要删除中间的某个元素的话，必须对后面的元素重新编号。代码实现如下：
```python
def josephus_L(n, k, m):
    people = list(range(1, (n+1)))
    i=k-1
    for num in range(n,0,-1):
        i=(i+m-1)%num
        print(people.pop(i),end=", " if num>1 else "\n")
```
## <font color=#00BCD4 >2 基于循环单链表的解法</font>
单链表即单向链接表，典型的就是c++中的链表，循环单链表就是头尾相连的单链表，也是线性表的一种，这道题目使用循环单链表记录$n$个人围坐一圈最为契合。我们只需要数到第$m$个结点就删除，删除操作对于链表来说比较容易，而且不需要有i = (i+1) % n这样的整除操作。但是问题在于python并没有像c++那样有内置对链表的支持，因此需要建立一个链表的类，建立是比较麻烦的，但是操作比较简单，如下：
```python
class LNode: # 建立链表结点
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_
class LCList: # 建立循环链接表
    def __init__(self):
        self._rear=None
    def is_empty(self):
        return self._rear is None
    def prepend(self,elem): # 前端插入
        p=LNode(elem)
        if self._rear is None:
            p.next=p # 建立一个结点的环
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear.next=p
    def append(self,elem): # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next
    def pop(self): # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear =None
        else:
            self._rear.next=p.next
        return p.elem
    def printall(self): # 输出表元素
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p=p.next
class LinkedListUnderflow(ValueError): # 自定义异常
    pass
class Josephus(LCList):
    def __init__(self,n,k,m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),end=("\n" if self.is_empty() else ", "))
    def turn(self,m):
        for i in range(m):
            self._rear = self._rear.next
```