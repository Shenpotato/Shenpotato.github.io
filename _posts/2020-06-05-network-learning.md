---
layout: post
title: "网络知识学习"
tags: Tools 
author: Shenpotato
catalog: true
---



> 华为数通知识学习
>
> 视频地址：https://www.bilibili.com/video/BV1Jx411j7pR



![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfhb45nwosj30yx0ki0v8.jpg)



### 一、数据通信网络的基本概念

#### 1.1 交换机（Switch）

终端/数据中心接入在交换机的网元上，每个网元是个冲突域。

一个交换机是个广播域（Broadcast Domain)。广播，是在特殊场景下的数据传播方式。ARP，DHCP等协议所要用到。广播增加了数据传输的损耗。在IPV6取消了广播。

单播（Unicast）：点对点的传播

组播（Muliticast）：一对多，视频，多媒体上应用

广播（Broadcast）：只在某个局域网内生效，三层（IP）上的目的ip表示为255.255.255.255；二层目的MAC表示为全F。

交换机的基本功能：

- 数据帧的交换
- 终端用户设备接入
- 基本的接入安全功能（MAC地址过滤，ARP的记片）
- 广播域的隔离（VLAN）
- 二层链路的冗余，防环以及负载均衡

连接在同一个交换机上的网元，通常处于同一个广播域中，又称为同一个LAN中，同一个逻辑子网中。

同一个交换机上的pc之间的通信行为称为二层通信



#### 1.2 路由器（Router）

路由器类比车站，数据相当于人，车站决定人怎么到达某个目的地。这个过程称为路由。

- 隔绝广播，实现跨三层的数据访问
- 路由协议的支持，维护路由表
- 路径选择及数据转发
- 广域网接入，地址转换及特定的安全功能

![image-20200605111810757](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfh8ucyb59j30zy0mz48a.jpg)



### 二、OSI七层模型(Open System Interconnect)

开放系统互连参考模型，是由IOS（国际标准化组织）定义的。是一个灵活，文件和可交互的模型

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfhbd5fbimj30zg0mdq5b.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfhosz1odvj30zd0kk0w1.jpg)



#### 2.1 应用层

为应用软件提供接口，是应用程序能够使用网络服务。常见协议：http(80), ftp(20/21), smtp(25), telnet(23), dns(53)

#### 2.2 表示层

数据的编/解码，加/解密，压缩/解压缩。常见标准如ASCII，JPEG。

#### 2.3 会话层

建立，管理和终止表示层尸体之间的会话连接。在设备或节点之间提供会话控制。在系统之间协调通信过程。

#### 2.4 传输层

将上层应用程序的数据进行分段和重组，组合为数据流的形式。有UDP和TCP

#### 2.5 网络层

定义了逻辑地址。分组寻址，将分组数据从源端传输到目的端。通过路由选择，和维护路由表实现。

#### 2.6 数据链入层

在不可靠的物理链路上，提供可靠的数据传输入伍，把帧从一跳移动到另一跳。组帧，物理编址，流量控制，差错控制。数据链入层（以太网二层）逻辑地址：MAC地址（48 bits） 

#### 2.7 物理层

工作在物理层的设备——Hub集线器

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfics2g8rfj312i0ohtc2.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gficxz0w5xj30y10nsgoo.jpg)



### 三、TCP & UDP

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfid26943xj30wy0n2q5a.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfid4tx52dj30wu0li76w.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gfid5uaj02j310e0kngn5.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8z41ipq0j30hh0cr0tq.jpg)

#### 3.1 TCP与UDP简单对比

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8z5wzttzj30qq0cyt9x.jpg)

源端口号随机分配，一般未系统中未使用的且大于1023；目的端口号在未指定的情况下使用应用服务的进程的默认端口号。

#### 3.2 TCP

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8z71osxfj30nk0dc3ze.jpg)

Sequence number（序列号），Acknowledegment number（确认号）：保证可靠传输

windows（活动窗口）

control bit（控制位）：6个位



##### 3.2.1 三次握手

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8zmytsodj30ot0fcwfa.jpg)

seq是自己的序列号，ctl = SYN 代表控制号的SYN置1，ack是用于确认对端的序列号。



##### 3.2.2 四次挥手

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8zs80ivxj30st0ga75l.jpg)



##### 3.2.3 滑动窗口

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8zxryn4dj30q60h1407.jpg) 





#### 3.3 UDP

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg8zls8qwmj30od0bhgm5.jpg)



### 四、IP

#### 4.1 基本信息

##### 4.1.1 报文格式

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg902ogncsj30of0ek0tt.jpg)

**Priority&Type of Service：**处理QOS

**Identification，Fragment offset：**分片

**Time to live(TTL)：**防环。报文发送时，赋给TTL一个初始值，每经过一个路由时减一，当TTL值为1时，向数据包起源发送报错消息（ICMP消息）。

**Protocol：**用于告知上层协议是什么

**Header checksum：**检测报文是否完整

##### 4.1.2 基本概念

- IP地址在网络中用于标识一个节点（或者网络设备的接口）
- 也用于IP分组在网络中的寻址
- IPv4有32位，使用”点分十进制“表示。

##### 4.1.3 地址划分

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg998h51zpj30od0d2gmw.jpg)

路由器不关心Host部分，只关心网络号。

**子网掩码：**网络部分用1表示，主机部分用0表示。192.168.1.0/24

**可变长子网划分：**将主机位的某几位借给网络位。其中255将作为广播号，0作为自身，将保留。192.168.1.0/25

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gga4cabpu5j30q30anmyb.jpg)



#### 4.2 网络传输过程

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg98olnj7kj30pw0d675p.jpg)

PC通过ARP协议获取了R1的MAC地址，PC发送一个数据帧到R1，源MAC地址为PCMAC地址，目的MAC地址为R1 GE0/0/0MAC地址。目的IP地址为192.168.1.1，源IP地址为192.168.2.1。

R1发现MAC地址匹配，进行拆解MAC帧头，发现目的IP地址不匹配，则根据路由表进行转发，再次包装上新得MAC帧头，发送至R2。

R2发现MAC地址匹配，IP地址虽然不是自身IP，但是是本地直连网段，则将报文重新封装转发至Server，完成整个传输流程。

**traceroute ipaddr：**追溯ping通某一ip地址的路径



#### 4.3 ARP（地址解析协议）

-  将IP地址解析为MAC地址
- 维护ARP映射缓存

当前主机未知目的IP的MAC地址时，需要通过交换机进行广播，对应IP地址发送一个单播的数据帧回去，携带对应的MAC地址

![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gg98jnoslxj30i708s3z8.jpg)

主机将对应IP地址和MAC地址对应起来的表称为ARP表。

- 广播和ARP表造成的负担大
- 不可靠和不安全，无确认机制可能造成ARP欺骗。





### 五、IP路由选择

#### 5.1 路由器

##### 5.1.1 路由器工作内容

- 路由器知道目的地址
- 发现到达目的地址的可能路径
- 选择最佳路径、路由表(Routing Information Base)
- 维护路由信息
- 转发ip数据

初始情况下，只知道直连接口所在的网络，直连网络在路由表中标记为Direct。直连网络出现在路由表的前提，是该网络的物理接口和协议状态都为UP。

##### 5.1.2 路由条目的来源：

- 直连路由：路由器本地接口所在的网段
- 静态路由：手工配置的路由条目
- 动态路由：路由器之间动态学习到的路由

**模拟一个简单通信场景下ip表的配置**：

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gixfuxmwfyj30rk09tmxe.jpg)

针对如上场景，AR1 GE0/0/0口和AR2 GE0/0/0口是同一个网段，AR2 GE0/0/1口和AR3 GE0/0/0口是同一个网段。

1. 路由器本身感知直连路由，路由表中有直连路由。比如AR1中存在192.168.23.0/24 这条目的ip的直连路由。

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gixgftv1zwj30q30a9wfm.jpg)

2. 但此时，因为AR1路由表中不存在目的ip为193.168.23.3的路由，所以AR1与AR2之间无法通信（未确定动态路由协议以及其他静态路由的条件下）。为了使AR1和AR3能够通信，我们可以**手动配置一条静态路由**。

   ip为193.168.23.3，NextHop（下一跳）为192.168.12.2。

```
[Router] ip route-static 网络号 掩码 出接口 下一跳ip地址
```

3. 此时，由于**通信是双向的**，AR1和AR3之间仍然ping不通。所以，需要我们再次对AR3中的路由表进行静态路由配置。

##### 5.1.3 最长匹配原则

![](https://tva1.sinaimg.cn/large/007S8ZIlly1giyhd9q3hpj30qh0fjgmp.jpg)



#### 5.2 静态路由

##### 5.2.1 默认路由

![ ](https://tva1.sinaimg.cn/large/007S8ZIlly1gixgsa8sgkj30qy0i3wg4.jpg)

当遇到子网ip很多时，我们可以通过配置默认路由，来匹配。

```
[Router]ip route-static 0.0.0.0 0.0.0.0 192.168.12.2
```



##### 5.2.2 路由汇总

当遇到子网ip很多时，我们可以通过配置默认路由，来匹配，子网的ip要在一个ip子网掩码内。

```
[Router]ip route-static 172.16.0.0 19 192.168.12.2
```



##### 5.2.3 浮动静态路由

出于负载均衡考虑，我们可以将同一个ip配置给不同的子接口进行下一跳。在下一跳的途中，我们可以设置preference属性，数据包将优先通过preference属性较小的子接口转发。



**路由的接口：**

GE：实际存在的三层物理接口

Loopback：虚拟的接口

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gixh4kldc0j30p50h80uj.jpg)



### 六、动态路由协议

根据不同的划分标准：

![](https://tva1.sinaimg.cn/large/007S8ZIlly1giyimg58a8j30io0d874s.jpg)

#### 6.1 距离矢量路由选择协议





