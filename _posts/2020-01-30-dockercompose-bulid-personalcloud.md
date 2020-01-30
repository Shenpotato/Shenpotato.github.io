---
layout: post
title: "使用 Docker Compose 快速搭建个人云并配置多存储介质"
tags: Docker Tools  
author: Shenpotato
catalog: true
---



## 使用 Docker Compose 快速搭建个人云并配置多存储介质

[参考文章](https://cloud.tencent.com/developer/labs/lab/10414)



要注意的是在通过

`pip install docker-compose --ignore-installed`

安装docker compose时，会出现如下所示的错误

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbez0zcxr5j30rs06a0tq.jpg)

这是由于缺少了Python.h导致的，通过

`yum install python-devel`可解决。

其他方面按照文章所示配置即可。

后续添加使用这个个人云存储和下载文件