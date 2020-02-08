---
layout: post
title:  "pandas的基本用法"
tags: Python
author: Shenpotato
catalog: true
---



> 记录python中pandas的用法



在使用pandas之前，我们需要导入它。并且pandas经常与numpy联合使用。

```python
import pandas as pd
import numpy as np
```



1、数据结构的创建

pandas 中核心的数据结构有两个，一个为DataFrame，一个为Series。

（1）Series

可以把Series视为一个长度固定的字典。index为索引。

```python
s = pd.Series(data,index = index)
```

data的形似可以多种多样，包含字典，标量等

```python
# 返回索引为a,b,c,d，值都为5.0的Series
s1 = pd.Series(5.0, index =['a','b','c','d'])

# 通过字典进行初始化
dict = {'a':1,'b':2,'c':3}
s2 = pd.Series(dict)

# 返回s1中value的数据类型
s1.dtype
# 返回s1的名字
s1.name
```



（2）DataFrame

DataFrame可以视为一个包含有头信息的二维数组。形成的效果如下：

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8hiehzx6jj30r80k4dlu.jpg)

