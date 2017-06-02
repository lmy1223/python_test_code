# -*- coding: UTF-8 -*-

# 求最小值，实现的几种方法，求最大值也同理

# 1. 最简单的直接用Python的 min() 方法，同理 max()方法
In [7]: min_one = min(1,2,3)

In [8]: print(min_one)
1

# 2.利用数组里面的sort排序 

In [9]: def min_two(*args):
    ...:     list1 = list(args)
    ...:     list1.sort()
    ...:     return list1[0]
    ...:

In [10]: print(min_two(1,2,3))
Out[10]: 1

# 3

In [14]: def min_three(*args):
    ...:     min_num= args[0]
    ...:     for i in args[1:]:
    ...:         if i < min_num:
    ...:             min_num= i
    ...:     return min_num
    ...:

In [15]: print(min_three(2,3,4,5))
Out[15]: 2


# 4

In [20]:
    ...: def min_four(first, *args):
    ...:     for i in args:
    ...:         if i < first:
    ...:             first = i
    ...:     return first
    ...:

In [21]: print(min_four(2,3,4,5))
Out[21]: 2

# 最大 & 最小

# 传入一个回调函数最大 Or 最小的 callback
In [27]: def min_or_max_num(callback, *args):
    ...:     num = args[0]
    ...:     for i in args[1:]:
    ...:         if callback(i, num):
    ...:             num = i
    ...:     return num
    ...:
    ...:
    ...: def min_num(x, y):
    ...:     return x < y
    ...:
    ...:
    ...: def max_num(x, y):
    ...:     return x > y
    ...:

In [28]: print(min_or_max_num(min_num, 1, 2, 3, 4))
1

In [29]: print(min_or_max_num(max_num, 1, 2, 3, 4))
4
