---
layout: post
title:  "Hadoop简介"
tags: Hadoop
author: Shenpotato
catalog: true
---


对hadoop进行介绍



# 一、Hadoop基本介绍

Hadoop是一个开源的，用于可靠，大规模，分布式计算的软件架构

用于：

- 海量数据的存储（HDFS-分布式文件系统）

  ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86spafqpuj30zy0rk0v9.jpg)

- 海量数据的分析（MapReduce-基于yarn，用于并行处理大数据集的计算框架）

  ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86spdo5w1j312w0n0q54.jpg)

  

- 资源管理调度（YARN-分布式作业调度系统）

**google的三篇论文**

- HDFS
- MapReduce
- BigTable





2. 分布式系统介绍

- 软件系统划分为多个子系统或者模块，各自运行在不同的机器上，子系统或者模块之间通过网络通信协作
- 例子：分布式操作系统，分布式文件系统，分布式数据库系统等



3. 离线数据分析流程

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86spmqiy8j30vu0li416.jpg)