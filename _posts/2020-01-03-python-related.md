---
layout: post
title: "python相关"
tags: Python 
author: Shenpotato
catalog: true
---



> 本文主要记录一下在使用python中的一些杂碎的问题，如配置等等



### 一、pip 安装第三包时出现readtimeout错误 

这是由于我们的timeout时间设置的比较短，在下载时超时了

 

有两个解决方案：

（1） pip install --default-timeout = 100 package_name

（2） pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ package_name

 

第一个是重新设置了判定超时的时间。但是在源下载地址下仍然具有下载速度慢，易超时的问题。

第二个是将源下载地址换为了清华大学/阿里云的镜像地址，通过加快下载速度以避免超时。推荐第二种。

```
pip install packagename -i https://pypi.tuna.tsinghua.edu.cn/simple/
												-i https://mirrors.aliyun.com/pypi/simple/
```



### 二、在mac终端切换python版本

1. 在.bash_profile中设置好python2和python3的路径

   ![](https://tva1.sinaimg.cn/large/006tNbRwgy1gakjck81ypj30ty0hm40y.jpg)

2. 在.bashrc中输入

   ![](https://tva1.sinaimg.cn/large/006tNbRwgy1gakjdje3k6j30ve05k750.jpg)

3. 每次切换python版本通过修改.bashrc中的python指向来实现，修改后编译文件使之生效

   ![](https://tva1.sinaimg.cn/large/006tNbRwgy1gakjgltikpj30sq066t9v.jpg)



### 三、Jupyter Notebook

1. mac下安装

   ```
   pip install --user jupyter
   
   pip3 install --user jupyter
   ```

   

2. 英文环境设置

   **UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in position 4: ordinal not in range 128**

   在~/.bashrc下添加：

   ```
   export LANG=en_US:UTF-8
   export LANGUAGE=en_US:en
   
   source ~/.bash_rc					#使生效
   ```

   

3. ctrl + enter快捷键执行

4. 加上！代表作为terminal执行





### 四、Tensorflow安装

```
pip install packagename==version -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

2.0以上版本的tensorflow进行了修改，可以安装旧版本，如1.15.3等等