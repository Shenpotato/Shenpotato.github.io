---
layout: post
title: "面试记录"
tags: Interview 
author: Shenpotato
catalog: true
---



## 一、腾讯WXG后台开发实习面试

### 1、初面（挂）

1. 介绍华为实习项目

   （1）云网络是什么，SDN是什么

   - 云网络是将网络管理、控制甚至数据连接转移到云计算服务上。示例包括使用基于云计算的网络控制器来引导跨WAN连接的流量，或者使用云计算服务提供商的内部WAN来承载客户WAN流量。

   - SDN（Software Define network，软件定义网络）。是将分布式控制的网络架构重构为集中控制的网络架构。

     传统网络：管理平面，控制平面和数据平面。管理平面主要包括设备管理系统和业务管理系统，设备管理系统负责网络拓扑、设备接口、设备特性的管理，同时可以给设备下发配置脚本。控制平面负责网络控制，主要功能为协议处理与计算。比如路由协议用于路由信息的计算、路由表的生成。数据平面是指设备根据控制平面生成的指令完成用户业务的转发和处理。例如路由器根据路由协议生成的路由表对接收的数据包从相应的出接口转发出去。传统网络通常部署网管系统作为管理平面，而控制平面和数据平面分布在每个设备上运行。

     SDN三层架构：转控分离，集中控制，开放接口

     ![](https://tva1.sinaimg.cn/large/00831rSTgy1gcnjjbxpovj30fe0a5mxj.jpg)

     SDN的部署方式分为Underlay和Overlay，Overlay主要是指网络虚拟化技术，比如我们用到的vxlan等隧道技术。

   （2）流通信是怎么判断结束的

   （3）真实数据集下是怎么比较的DFS和Floyd的

2. 介绍jda的实习经历

   （1）什么字段需要建立索引

   https://www.cnblogs.com/abcdwxc/p/9855474.html

   - 索引：系统根据某种算法，将已有的数据（未来可能新增的数据），单独建立一个文件，文件能够实现快速的匹配数据，并找到对应表的数据
   - 意义：提升查询效率，以及约束数据的有效性（唯一性）。索引本身会产生索引文件，非常消耗磁盘空间
   - mysql提供的索引：主键(primary key)，唯一索引(unique key)，全文索引(fulltext index)，普通(index)
   - 数据库建立索引的规则
     - 表的主键、外键必须有索引； 
     - 数据量超过300的表应该有索引； 
     - 经常与其他表进行连接的表，在连接字段上应该建立索引； 
     - 经常出现在Where子句中的字段，特别是大表的字段，应该建立索引； 
     - 索引应该建在选择性高的字段上； 
     - 索引应该建在小字段上，对于大的文本字段甚至超长字段，不要建索引； 
     - 复合索引的建立需要进行仔细分析；尽量考虑用单字段索引代替：
     - 频繁进行数据操作的表，不要建立太多索引
     - 删除无用索引，避免对执行计划造成负面影响

   （2）是如何运行脚本的

   （3）Restful是什么

   一种设计模式，将GET，UPDATE，DELETE

3. TCP为什么三次握手，四次挥手

   三次握手防止重连，两次握手

4. ARP是哪一层的协议

   ‘ARP是介于网络层和物理链路层的协议，主要负责mac地址的解析

5. 进程和线程的区别

6. 线程之间的通信有哪些

7. java中的JVM内存分配是什么样的

   先通过类加载器（ClassLoader）会把 Java 代码转换成字节码，运行时数据区（Runtime Data Area）再把字节码加载到内存中，而字节码文件只是 JVM 的一套指令集规范，并不能直接交给底层操作系统去执行，因此需要特定的命令解析器执行引擎（Execution Engine），将字节码翻译成底层系统指令，再交由 CPU 去执行，而这个过程中需要调用其他语言的本地库接口（Native Interface）来实现整个程序的功能。（类加载器+java文件——>运行时数据区+字节码文件+内存——>命令解析器执行引擎+字节码文件——>底层系统指令+本地库接口+cpu）

   栈保存函数的局部变量和函数返回信息，堆内存用来保存类和对象。

   ![img](https://tva1.sinaimg.cn/large/00831rSTgy1gcnw3fkxbsj30d70b2wey.jpg)

   **（1）程序计数器**
   ​	程序计数器（Program Counter Register）是一块较小的内存空间。它可以视为**当前线程**所执行的**行号	指示器**，指令在执行时，需要通过改变这个计数器来选取下一条需要执行的指令。Java虚拟机的多线程是通过轮流切换并分配处理器执行时间的方式来实现的，在一个确定的时刻只有一个处理器执行一条线程中的指令，**为了在线程切换后能恢复到正确的执行位置，每个线程都会有一个独立的程序计数器**，因此，**程序计数器是线程私有的**。

   **（2）Java虚拟机栈**
   ​	Java虚拟机栈（Java Virtual Machine Stacks)，和程序计数器一样也是**线程私有**的，它的生命周期与线程相同，与线程是同时创建的。

   ​	Java虚拟机栈**存储线程中Java方法调用的状态**，包括局部变量、参数、返回值以及运算的中间结果等。**一个Java虚拟机栈包含了多个栈帧，一个栈帧用来存储局部变量表、操作数栈、动态链接、方法出口等信息**。当线程调用一个Java方法时，虚拟机压入一个新的栈帧到该线程的Java栈中，当该方法执行完成，这个栈帧就从Java栈中弹出。我们平常所说的**栈内存（Stack）指的就是Java虚拟机栈**。 

   **（3）本地方法栈**
   ​	本地方法栈（Native Method Stack）与Java虚拟机栈的作用非常类似，他们的区别就是Java虚拟机栈为虚拟机执行Java方法而服务，**本地方法栈则是为虚拟机用到本地Native方法而服务**。

   ​	在Java虚拟机规范中对本地方法栈的语言和数据结构等没有强制规定，因此具体的Java虚拟机可以自由实现它，比如HotSpot VM**将本地方法栈和Java虚拟机栈合二为一**。

   **（4）Java堆**

   ​	Java堆（Java Heap）是Java虚拟机所**管理内存中最大的一块**，被所有**线程共享的一块内存区域**，在虚拟机启动时创建。

   ​	Java**堆存储的对象被垃圾收集器管理**，这些受管理的对象无需也无法显示的销毁。从内存回收的角度，Java堆可以粗略的分为新生代和老年代。从内存分配的角度Java堆中可能划分出多个线程私有的分配缓冲区。根据Java虚拟机规范规定，Java堆的所使用的内存在物理上不需要连续，逻辑上连续即可。 如果在堆中没有足够的内存来完成实例分配，并且堆也无法进行扩展时，则会抛出OutOfMemoryError异常。

   **（5）方法区**
   ​	方法区（Method Area）也是被所有**线程共享的运行时内存区域**。用来存储**已经被Java虚拟机加载的类的结构信息、常量、静态变量和即时编译器编译后的代码等数据**。如果方法区的内存空间不满足内存分配需求时，Java虚拟机会抛出OutOfMemoryError异常。

   **（6）运行时常量池**
   ​	运行时常量池（Runtime Constant Pool）是方法区的一部分。Class文件不仅包含了类的版本、接口、字段和方法等信息，还包含了常量池，它用来存放编译时期生成的字面量和符号引用，这些内容会在类加载后存放在方法区的运行时常量池中。运行时常量池可以理解为是类或接口的常量池的运行时表现形式。

8. 方法是怎么进入内存的

9. 编译一个java文件的时候生成几个class文件

   会生成多个，根据定义类的个数

10. 有用过哪些消息队列

   RabbitMQ、RocketMQ、ActiveMQ、Kafka

11. java的垃圾回收是怎么实现的，如果使用计数的方式有什么缺点

12. select * 会带来什么问题

    - 一张表上所有的列不可能都带有索引，所以select *无法进行using index，必须走主键回表，会带来大量的物理io操作
    - innodb默认一个page16k，如果表中有text，一行记录超过了16k，会存在行连接，带来额外的io
    - select * 带来内存负担，许多不常用的数据进入innodb_buffer_pool_size中，降低内存查询命中率
    - 网络传输的开销变大

13. 对于redis的理解

    是一个key-value数据库，在内存中

    性能极高 – Redis能支持超过 100K+ 每秒的读写频率。
    丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
    原子 – Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。
    丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。




自我扩展：

1. 视图的作用

2. 为什么要使用mybatis

   传统架构：

   ![](https://tva1.sinaimg.cn/large/00831rSTgy1gcnvqtwlbaj307s0fmaa6.jpg)

   - 每次访问数据库都需要创建数据库连接，最后不需要使用还得释放连接，频繁地连接释放连接会造成系统资源浪费，从而影响系统性能；
   - 需要在Java代码里面编写SQL语句，SQL语句发生改动，需要重新编译Java代码，就种硬编码的方式造成代码不易维护的缺点；
   - Preparedstatement中设置的参数要与占位符在数量上一一对应，而且查询的条件不确定，参数或多或少，这就能引起很多麻烦
   - ResultSet中遍历结果时，需要对应相应数据库字段，这些字段属于硬编码，也不利于系统的维护。

   Mybatis:

   Mybatis是一款优秀支持自定义SQL查询、存储过程和高级映射的持久层框架，消除了几乎所有的JDBC代码和参数的手动设置以及结果集的检索。Mybatis可以使用XML或者注解进行配置和映射，通过将参数映射到配置中的SQL，形成最终执行的SQL语句，最终将执行SQL语句的结果映射到Java对象返回。

   与其他映射框架不同，**Mybatis** 不是把 **Java对象** 直接和数据库联系起来，而是把 **Java对象** 与 **SQL语句** 联系起来，把对象传进SQL语句来设置参数    



## 二、腾讯CSIG后台开发实习面试（电脑管家）

### 1.初面（3.9 30min）

1. 项目介绍

   讲一下Floyd算法

   两个项目具体是怎么实现的

2. struct和union的区别（C++）

   https://blog.csdn.net/firefly_2002/article/details/7954458

3. jvm的垃圾回收算法

   GCroot是怎么实现的

4. 进程之间的通信

5. jvm的运行数据区

6. tcp协议介绍



### 2.第二轮（3.18 50min）

1. 介绍多线程聊天室实现
   - Socket是如何实现的
   - tcp协议，udp协议的原理，比较以及应用
   - tcp内部是通过什么协议实现的
   - tcp连接数受什么影响（让我思考，跟服务器的什么有关系

2. 介绍springboot的项目
   - 自我介绍为主，看如何项目的完成，如何选择对应的技术
3. 算法：
   - 反转链表
   - 二叉树的中序实现->后序实现
   - java中map的实现（红黑树）
4. jvm
   - java文件如何运行（编译再到操作系统的过程）
   - java文件可以不通过字节码，直接转为二进制码吗
   - 如何判断一个对象是垃圾（垃圾回收机制）
   - 垃圾回收中新生代和老生代
5. java相关
   - 介绍反射机制，如何进行
6. c++/c相关
   - c和c++的区别
   - c和c++转成二进制码的区别
7. 我的提问
   - 问了组的干嘛的
   - 技术栈的影响
   - 面试流程
   - 表达了对于腾讯的浓浓爱意



### 3.第三轮（3.20 30min）组长面？

1. 项目

   - 聊天室
   - 网站
   - jda实习
   - 华为实习

2. 堆栈区别

3. 垃圾回收机制

   gcroot是从哪里开始的

4. java中有虚函数吗



### 4. 第四轮（总监面）挂

可能会问到的问题：

1. 一个10G的文件，里面全部是自然数，一行一个，乱序排列，对其排序。在32位机器上面完成，内存限制为 2G。

   https://www.jianshu.com/p/bf9dbbc147ed

2. 一个数是不是2的次方

3. 二叉树翻转：递归

   ```java
   TreeNode mirror（TreeNode treeNode）{
   		if(P==NULL) return null;
   		swap(treeNode.left, treeNode.right);
   		mirror(treeNode.left);
   		mirror(treeNode.right);
   }
   
   void swap(TreeNode leftNode, TreeNode rightNode){
   		TreeNode tempNode = leftNode;
     	leftNode = rightNode;
     	rightNode = tempNode;
   }
   ```

   

4. 青蛙跳台阶

5. 项目里面有哪些可以进行调优的地方

   - 聊天室中，tcp链接可能会出现的问题（链接数目，吞吐量）
   - 个人简历，高并发量，访问量

6. 业界最新的一些技术

实际问的：

实际项目往深了问



## 三、腾讯视频

### 1.初面

1. Tcp的三次握手，四次挥手

2. 进程间通信方式

3. map和vector的区别

4. 如何实现一个单例

5. IO的方式

6. 算法：判断循环链表是否为空

   

7. 介绍各种数据结构

8. 最小生成树：kruskal和kruskal之外还有什么

   prim算法

9. 快排怎么实现的

10. redis的数据结构是什么样的

11. 什么应该建立索引





## 四、腾讯文档



### 2. 二面

1. 死锁产生的条件，如何防止死锁

   两个或多个线程之间的对与互斥资源的相互等待。

2. 银行家算法

   主要是通过计算avaliable是否大于need，来判断某个序列执行是否可以。

   https://zhuanlan.zhihu.com/p/59533950

3. 进程和线程的区别

4. 有哪些链表，时间复杂度和空间复杂度是什么

   

5. 桶排序

   思想1: 将数据划分为相同大小的部分，再将各个部分分别进行排序，最后合并。

   思想2: 获取最大值和最小值，创建max-min长度的数组。对每个位置进行编号，分别对应max-min范围中的所有数字。当有数进来时，则对对应位置的数组a[index]进行++。

   

6. 选择排序，插入排序怎么实现

   

7. 网络安全

8. http3.0比较http2.0比较http1.0

9. elastic search使用

10. flutter使用

