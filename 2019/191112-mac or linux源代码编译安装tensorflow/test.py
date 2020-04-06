import tensorflow as tf
hello = tf.constant('hello world')  # 创建一个常量
print(hello)  # 输出
print(hello.numpy())  # 输出张量的值
print(hello.shape)   # 输出维度
print(hello.dtype)  # 输出张量类型
