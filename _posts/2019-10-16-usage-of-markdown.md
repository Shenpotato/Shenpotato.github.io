---
layout: post
title:  "Markdown 的基本使用"
tags: markdown
author: Shenpotato
catelog: true
---


介绍了Markdown的一些基本用法



## 一、标题

标题分为六种，分别对应html中的<h1>~<h6>，此.md文件所用的就是一级标题

一级标题：# titile1

二级标题：##titile2

......

六级标题：######title6



## 二、列表

### 1.有序列表

在文本前加上1. 2. 3. 即可。

**注意**：1. 2. 3. 需要与后续文本保留一个空格

1. ordered item1
2. orederd item2
3. ordered iterm3





### 2.无序列表

在文本前加上 - 即可

- unordered iterm1

- unordered iterm2

- unordered iterm3

  



## 三、引用

###1. 基本引用

在文本前加上>

>这是一个引用
>
> 你好





###2. 超链接

#### (1) 网页超链接

​		[显示文本]+(链接地址)

​		[百度](https://www.baidu,com)



#### (2) 图片超链接

​		![显示内容] + （图片路径）

​		图片路径可以为本地路径或者服务器的路径![java知识路径](/Users/shenzhengtao/Resources/job/面试准备/java知识图.jpg)



### 3. 代码块

**单行代码：**`将文本包起来

`System.out.println("nihao");`

**多行代码：**使用```将代码文本包起来

```java
public static void main(String[] args){
  
}

```



## 四、latex数学公式

使用$$包起来表示数学公式。

https://www.jianshu.com/p/05987743d27c

### 1.上下标

**下标：**k_a  =  $$k_a$$

**上标：**k^a  = $$k^a$$

如果上下标有多个字符，用{}括起。 k^{ab}  =  $$k^{ab}$$

### 2.常用公式

| 写法                  | 说明   | 效果                      |
| --------------------- | ------ | ------------------------- |
| \frac{a}{b}           | 分式   | $$\frac{a}{b}$$           |
| \sqrt{a}              | 开根号 | $$\sqrt{2}$$              |
| \vec{a}               | 矢量   | $$\vec{a}$$               |
| \int_{1}^{2}xdx       | 积分   | $$\int_{1}^{2}xdx$$       |
| \sum_{n=1}^{100}{a_n} | 累加   | $$\sum_{n=1}^{100}{a_n}$$ |
| \prod_{n=1}^{99}{x_n} | 累乘   | $$\prod_{n=1}^{99}{x_n}$$ |

### 3.希腊符号

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g91zv2dwm6j30el09e3yv.jpg)



### 4. 逻辑符号

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95skdexbzj313e0s40v8.jpg)



##五、其他技巧

### 1. 字体变化

#### （1）粗体

​			将文本用**包裹

​			**加黑**

#### （2）斜体

​			将文本用*包裹

​			*斜体*



### 2. 分割线

在一个单独行里使用三个或以上 * 或者 - 来产生水平分割线

---

***

