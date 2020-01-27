---
layout: post
title:  "Numpy的基本用法"
tags: Python
author: Shenpotato
catalog: true
---


记录python中numpy库的基本用法。

# Numpy的基本用法

Numpy的中文网站：https://www.numpy.org.cn/

import numpy as np

## 一、数组创建

```python
np.zeros(m,n)  //创建0为元素的m*n维数组

np.ones(m,n)   //创建1为元素的m*n维数组

np.array([1,2,3,4],[1,2,3,4])		//创建一个指定元素的数组

np.range(0,2,0.1) 	//创建从0开始，步长为0.1，以1.9结束的数组

np.linspace(1. ,4. ,6)		//在1-4中，等步长的产生6个元素，包含1，4

np.random.rand(d1,d2,...,dn)  //创建n维数组，每个维度长度为di，数组值为0-1的任意值
np.random.randn()		// 数组值服从正态分布

nprandom.randint(low, high=None, size=None, dtype=’l’)		//生成low-high区间的，size维度的随机数

np.random.choice(a, size=None, replace=True, p=None) //从a中选取元素组成size大小的数组

```



## 二、数组操作

```python

np.transpose(A)		//将A数组转置

np.argmax(A,axis)		//对数组A，寻找从维度axis上看，每个维度的最大值
```



### 1、数组相乘

```python
np.dot(A,B)  //对数组进行叉乘，返回一个数组
A * B   
np.multiply(A,B)		//A B数组中相同位置元素相乘
```



```
np.sum(A,axis = 0)		// A矩阵对每一列进行累加
np.sum(A,axis = 1)		// A矩阵对每一行进行累加
```



## 三、数组输出

