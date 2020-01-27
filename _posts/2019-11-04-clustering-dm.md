---
layout: post
title:  "聚类算法"
tags: cluster datamining
author: Shenpotato
catelog: true
---


## 一、聚类相关概念

### 1、聚类

将具有相似特征的数据划为一类。

**与分类Classificaiton的区别：**

分类问题是监督学习，样本有进行标记；

聚类问题是无监督性学习，样本没有进行标记。

### 2、高质量的聚类评判标准

- 高集群内相似度
- 低集群间相似度

### 3、作用

- 对回归问题的做预处理；主成分分析法PCA；相关性分析
- 对图片进行压缩；对向量进行降维
- 离群检测（outlier detection）



## 二、区分方法（Partition method）

partition method的基本思想：

计算所有节点与其聚类集的中心节点的距离平方和最小值。

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8ngml3o6sj318809odi0.jpg)

其中最经典两个算法：K-means与k-medoids/PAM

### 1、K-means算法

#### （1）算法思想：

初始化：随机选取k个中心节点

循环直至收敛：

- 根据给定的中心节点，选取每个节点与中心节点的最小距离划分聚群
- 根据集群，重新计算每个集群的中心节点

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8o2zz3lhzj318u0tidlb.jpg)

#### （2）优缺点

##### A. 优点:

计算高效。时间复杂度为O(tkn)，其中t为迭代次数，k为聚类集群树，n为节点总数。其中t，k<<n。

##### B. 缺点：

- 只适用于连续n维空间下的变量
- 对k值，即集群数量的选择准确度依赖很大
- 对噪声数据和离群数据很敏感
- 不适合发现具有非凸形状的聚类

#### （3）算法变种

1. 初始k中心节点位置的选取
2. 不相似度计算
3. 计算聚类均值的策略
4. 解决分类数据

### 2、PAM（Partitioning Around Medoids)

#### （1）算法思想

区别于k-means，pam选择的聚类中心点是已有的数据节点。

- 在所有节点中随机选取k个代表节点作为中心节点

- 对于每一个未被选中的节点h和未被选中的节点i，计算他们总计交换损失TCih

- 对于每对i和h：

  如果TCih < 0，使用i代替h；

  对集群中所有的未选中节点进行此操作，直至没有未选中的节点

- 循环 2-3直到centroid没有改变

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8o440atf5j312u0u0jui.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8o451prokj316i0tywhv.jpg)

#### （2）优缺点

##### A. 优点：

拥有更好的鲁棒性

##### B. 缺点：

时间复杂度高。时间复杂度为O(k(n-k)2)。

#### （3）变种

- CLARA（Clustering Large Application):：通过采样划分样本，对每个子样本选出计算聚类，选出最好的聚类作为输出
- CLARANS (“Randomized” CLARA) ：动态绘制邻居样本，聚类过程可以表示为搜索图，其中每个节点都是一个潜在的解决方案，即一组k个medoids。如果找到了局部最优，则从新随机选择的节点开始，以寻找新的局部最优



## 三、层次聚类

层次聚类算法是指在树形结构中，将所有样本点自底向上合并或者将一棵树自顶向下分裂的过程。

在介绍层次聚类算法之前，需要介绍关于集群之间距离的概念

- single link：两个集群之间最近节点的距离
- complete link：两个集群之间最远节点的距离
- Group average link：两个集群中节点的距离的平均值
- centroid link：两个集群中心点（坐标值的平均值）的距离
- median link：两个集群中心点（已存在节点）的距离

#### 1、AGNES(Agglomerative Nesting) 

- 根据single linkage得出节点间的距离矩阵
- 寻找距离矩阵中最小距离对应的节点，合并两个节点
- 更新距离矩阵
- 循环2，3直至达到收敛条件（距离矩阵中距离全部大于可合并距离阈值/集群数量到达阈值）

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8o8xqylmfj317e0s877x.jpg)

#### 2、DIANA(Divisive Analysis)

DIANA是AGNES的反向过程，是将合并的节点进行分解的算法。



## 四、基于密度的方法

### 1、基本概念

- Eps：半径值。选取节点i，以该半径画圆，圆内的节点称为i的邻居节点
- Neps(q)：q节点在Eps半径下的节点数目
- MinPts：在Eps半径下，最少的邻居节点数目。
- 核心点（core point）：当|Neps(q)|>=MinPts时，q节点为核心点
- 直接密度可达（Directly density-reachable)：如果q在p的邻域E之中，且p为核心点，则称q从p直接可达。
- 密度可达（density-reachable)：p是核心点，p可以通过一条路径，路径上的点都是核心点到达点q（q可以不为核心点）
- 密度相连（density-connected)：o和p，q都为密度可达，那么p,q密度相连
- 边界点（border point)：p不为核心点，但在核心点q的邻域中
- 离群点（outlier）：

### 2、DBSCAN算法

- 计算每个点的Neps(q)，划分节点为核心点，边界点，离群点/噪声点
- 随机选取一个核心点，找寻所有的密度可达点，在剩余点中去除遍历过的节点
- 重复2，直至没有核心点

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8oaumrzyqj315a0pgwgr.jpg)

## 五、基于网格的方法

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8oaykzqkxj314p0u00xf.jpg)



## 六、聚类评估

#### 1、选取集群的个数

##### （1）经验法(Empirical method)：

节点数的一半的开平方

##### （2）肘法(Elbow method)：

聚类内方差曲线的转折点

##### （3）交叉验证(Cross validation method)：

- 将给定数据集划分为m个部分
- 使用m-1部分的数据获得聚类模型
- 使用剩下部分的去测试聚类质量



#### 2、评估集群质量

两种方法：外部与内部

##### (1)外在:

受监督的，即可以得到基本事实

- 使用某些聚类质量度量将聚类与基本事实进行比较

- 如：精确度和召回率指标

##### (2)内在：

无监督的，即基本事实不可用

- 通过考虑群集的分离程度以及群集的紧凑程度来评估群集的优劣
- 如：轮廓系数

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8obanbhu9j314n0u0wjo.jpg)





















