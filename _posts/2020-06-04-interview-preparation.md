---
layout: post
title: "秋招准备"
tags: Tools 
author: Shenpotato
catalog: true
---



> 秋招面试准备



### 一、项目相关

#### 1. 网络自验证项目

基础背景知识

##### 1.1 Batfish

Batfish是一个网络验证工具，通过分析网络设备的配置信息来确保网络的安全性，可靠性和可编译性。通过设配配置来构建完整的网络模型行为，并发现违反网络策略（内置，用户定义，最佳实践）的情况。

Batfish的主要用例是在部署之前验证配置更改。部署前验证是现有网络自动化工作流程中的一个关键缺口。通过将Batfish包括在自动化工作流程中，可以确保部署正确的更改。

Batfish无需直接与设备进行交互。其核心的分析依赖于网络设备的配置。这些分析可以通过BGP，拓扑信息等进行额外的优化。



##### 1.2 SDN网络





### 二、计算机网络

#### 1.OSI七层模型

| 层级   | 协议                            |
| ------ | ------------------------------- |
| 应用层 | TELNET, HTTP, FTP, NFS, SMTP    |
| 表示层 | 数据格式和加密                  |
| 会话层 | 开始、控制和结束一个会话        |
| 传输层 | TCP, UDP, SPX                   |
| 网络层 | IP, IPX, ICMP, Routing protocol |
| 链路层 | ATM, ARP                        |
| 物理层 |                                 |

#### 2. TCP协议

三次握手：

四次挥手：

流量控制：

拥塞控制：



### 三、操作系统

#### 1. 内存管理

#### 2. 进程调度

#### 3. 进程通信

#### 4. Linux常用命令



### 四、数据库

#### 1. 事务（ACID）

#### 2. 范式

#### 3. 关联

#### 4. 聚集函数

#### 5. 索引（b+树）

#### 6. innodb与其他的区别

#### 7. 锁的粒度





数据结构：（重头戏），除了广义表不需要重点看之外。《数据结构》严蔚敏
线性表，尤其是链表（头插法、尾插法、删除、双链表、带头结点与不带、循环链表等）、栈、队列。
哈弗曼树、二叉树、二叉排序树（删除、增加）、b树、b-树、b+树、b*树、红黑树、字典树、树的三种遍历（代码实现，递归与非递归）。
图的遍历（dfs、bfs、递归与非递归）、拓扑排序、最小生成树（Dijkstra、Foyd、Prim、kruskal）。
查找：常用的就二分查找了。
排序：冒泡、插入（常用）、选择（常用）、快速（常用）、堆（常用）、归并（常用），希尔（不常用）、基数（不常用）
**口诀：不稳定：快选希堆，其他则是稳定算法。**
补充：
KMP算法及改进BM算法[传送门](https://www.cnblogs.com/ZuoAndFutureGirl/p/9028287.html)
并查集，用于求朋友的朋友问题（最小生成树个数）,[并查集](https://www.cnblogs.com/noKing/p/8018609.html)[并查集路径优化](https://blog.csdn.net/qq_19782019/article/details/78919990)
三路快速排序（快排优化），[传送门](https://www.cnblogs.com/deng-tao/p/6536302.html)
刷题：leetcode（top like100）

Java
Java基础倒是很少问，一般问源码层面问题，注意1.7和1.8的区别
1、《深入理解Java虚拟机》，最重要的是JMM（Java Memory Model）,我自己的建议就是从JMM为中心，开始向四周扩展，构建知识网。
**从JMM -> GC算法，GC Root的确定，线程逃逸问题，Java对象头（Synchronized实现原理），栈的原理，类加载机制问题，三级\**\*结构、内存屏障，即volatile关键字原理，线程调度等，全部可以从jmm发散，或者从某个点切入，也能讲到JMM。**
2、集合：HashMap、HashTable、ConcurrentHashmap、LinkedHashmap、TreeMap、TreeSet、ArrayList、LinkedList、PriorityLinkedList源码等等
3、锁：乐观锁（版本号（mysql通过多版本号来解决幻读问题），cas），悲观锁（AQS，AbstractOwnableSynchronizer是重点）、ReentrantLock、CountDownLatch、CyclicBarrier、读写锁等等，与synchronized的原理对比等。
4、多线程：线程几种实现方式，状态转换，ThreadPoolExecutor参数解析，执行流程。
5、六大原则：
单一职责原则（Single Responsibility Principle  SRP）
开闭原则（Open Close Principle OCP）
里氏替换原则（Liskov Substitution Principle LSP）
依赖倒转原则（Dependence Inversion Principle  DIP）
接口隔离原则（Interface Segregation Principle  ISP）
迪米特原则 （Least Knowledge Principle  LKP）
6、常用设计模式（手写单例模式）：工厂模式(bean)、***模式（aop）、观察者模式(消息发布订阅、dubbo)，说的这样都是在spring中可以联系起来的
Spring中常用的设计模式有哪些？
7、如何用线程打印abab问题，[传送门](https://blog.csdn.net/lsq_401/article/details/79766310)
8、海量数据问题：归并排序思想，[传送门](http://www.cocoachina.com/articles/30336)
**9、Spring mvc作为后端，讲述从前端请求到后端返回的全部流程，从dns解析到tcp建立连接，再到arp解析，再到反向\**\*，再到DispatchServlet、HandlerAdapter（通过HandlerMapping找到对应的requestmapping方法）、ModelAndView等，这个问题足以将基础和框架全部联系起来。**
10、反向***策略：轮询、随机、加权、最少连接、ip hash、dns最短等
11、四层***(lvs)和七层***（nginx）
12、分布式session问题
13、洗牌算法
14、zookeeper实现分布式锁，以及它的***过程等
15、Spring ioc的原理，aop的原理（jdk和cglib，与静态***AspectJ的区别）
16、Spring bean的是如何管理的？
17、在maven中如何出现了循环依赖问题，spring中的bean是如何注入的？
18、dubbo原理，架构图
19、一些常见的rpc框架，rpc和http有何区别
20、如何实现i++的原子操作，（加锁问题，volatile关键字(可见性（三级***缓存失效，通过对比自身数据）、有序性（内存屏障）)）
21、布隆过滤器





第一点可能会手写生产者消费者模式，或者多线程交替打印，或者单例模式实现，然后紧接着就是volatile，synchronized关键字，jvm的话可能就是内存模型，gc算法，垃圾收集器，cms和gc相关的区别优劣势。第二点可能就是出个算法题，或者让你手写，或者说下解题思路第三点基本上就是sql调优，优化方法，索引结构，最左原则，以及explain相关结果分析，redis可能就是问问缓存穿透，击穿，雪崩，自己底层结构之类的。第四点框架可能问你bean的生命周期，启动过程。



### 