# coding=utf8
'''
basic tf operation examples, 
1. write a tf function use tf.xxxx
2. feed data to tf.placeholder and set data to tf.Variable
3.run...
'''
'''
基本的tf操作例子:
1.写一个使用tf.xxx函数的类子
2.构建一个placeholder 并给变量赋值
'''
# coding=utf8
import tensorflow as tf

# direct sum with constand value
print '================================'
print '常量定义操作，使用tf.constant定义常量'
a = tf.constant(2)
b = tf.constant(3)
c=a+b
d=a*b
# 构建session
sess=tf.Session()
# 获取
print sess.run(c)
print sess.run(d)
print '=============================='
#
print  'placeholder相当于接口'
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

# 
add = tf.add(a, b)
mul = tf.multiply(a, b)
print 'feed_dict相当于输入字典'
print sess.run(add, feed_dict={a: 2, b: 3})
print sess.run(mul, feed_dict={a: 2, b: 3})


print '================================'
#
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix2, matrix1)
print sess.run(product)
print '================================='
#here you should also be able to use tf.placeholder

print '乘法操作'
mat1=tf.Variable(tf.random_normal([3,2]))
mat2=tf.Variable(tf.random_normal([2,3]))
product=tf.matmul(mat1,mat2)

m1=[[1,3],[2,1],[0,5]]
m2=[[3,2,1],[1,2,3]]

print sess.run(product,feed_dict={mat1:m1,mat2:m2})
print '=============End==============='