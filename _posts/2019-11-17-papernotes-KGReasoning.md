---
layout: post
title: "论文阅读笔记-知识图谱推理"
tags: PaperNote
author: Shenpotato
catalog: true
---



## 一、DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning 

### 1、概述：

（1）目标：基于已有的实体对，对实体对之间的关系路径进行推理

（2）基于深度学习的知识推理描述：

​	将知识推理的过程看作一个可以被基于策略代理解决的决策问题。在建立强化学习的训练模型之后，定义路径	路径受限的搜索算法。

### 2、模型框架

划分为两部分，外在部分是markov决策模型表示的知识图谱环境，内在部分是由神经网络组成的policy base代理。

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8pfzbibt3j30zo0h4ju8.jpg)

#### （1）markov决策模型（MDP）

<S, A, P, R>用来代表MDP，S为连续的状态空间，A是行动，P是概率状态转移矩阵，R是奖励函数

##### A. State: 

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8pfcmrg7aj30bi02kdfs.jpg)

使用translation-based embeddings（TransE/TransH）代表实体和关系

##### B. Action:

 KG中的所有relation

##### C. Rewards:

- **Global accuracy:**

  ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8pfgdjnkmj30l604iq30.jpg)

  在Action设定中，我们包含了当前状态下的可能relation路径，数量非常大，并且需要进行拓展的决策序列会成指数式增长。所以我们通过添加该节点的后续序列能否到达目标节点来进行简化。

- **Path efficiency:**

  ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8pfkhvmdvj30ci0363ye.jpg)

  鉴于短路径相比于长路径更能得到可靠的推理结果和提高运行效率两方面考虑，将推理长度考虑进reward。

- **policy diversity:**

  ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g8pfv15ij5j30k005qgll.jpg)

  agent通常会寻找具有相同语义的路径，这些路径包含着冗余信息。所以需要对路径进行cosine相似度判断。

  

#### （2）policy based agent

agent实际上是一个全联接的神经网络，包含两层激活函数为ReLU的隐藏层，输出层为softmax层。



### 3、训练过程

知识推理过程中重要的制约因素是关系集太过庞大，这将导致神经网络的输出层的维度太高。

为了解决这个问题，文中使用了由AlphaGo的imitation learning pipline启发的**supervised policy **。因为在AlphaGo进行每一步决策时，要面对250可能的行动。

类比AlphaGo的一开始训练的专家移动（expert moves），作者使用随机广度优先搜索作为监督策略。

#### （1）带监督的策略学习

- 对于每一个关系，我们使用所有正样本的子集进行学习。

- 对于每一个正样本（source_entity,target_entity)，广度优先遍历用于寻找实体之间的正确路径。

- 对于每一条路径，使用Monte-Carlo策略梯度最大化期望累积奖励，更新参数

  期望累积奖励：

  ![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90t1fsbdcj30hc072glr.jpg)

  期望累积奖励的导数：

  ![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90t3g2d5vj30ls064wes.jpg)

由于BFS偏向于寻找最短路径，与我们的预期不符。因此，文中使用了一个策略：

随机选择一个中间节点inter_entity，寻找（source_entity,inter_entity)和（inter_entity,target_entity)之间的路径，并将其连接起来，用于训练agent。

#### （2）带奖励的训练

我们的目的是根据奖励函数去预测路径，因此，我们将奖励函数添加至监督策略网络。对于每一个关系，一对实体间的推理被视为一代。

从初始节点source_entity开始，agent根据随机策略（所有关系的概率分布）随机选择关系，拓展预测路径。这个关系链接可能链接出新的实体对象或者指向空。将negative rewards的推理视为不好的推理，进行舍弃，agent回到推理前实体位置。通过设置最大路径长度max_length提高训练的效率。在每一代结束后，策略网络进行如下更新：

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90toagf0zj30kk038weh.jpg)

具体的算法过程如下：

![image-20191117102542205](https://tva1.sinaimg.cn/large/006y8mN6ly1g90ts0h5pij30k80v8wiv.jpg)

#### （3）双向路径限制搜索

给定一个实体对，RL agent学到的推理路径可以作为规则的LHS。在KG中，一个实体可以通过一个关系连接到巨量实体，比如关系 ![[公式]](https://www.zhihu.com/equation?tex=personNationality^{-1}) ，如果规则中包含这样的关系，那路径的中间实体就会超级多，但如果换个方向就没有那么多了，所以就要bi-directional。

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90u1vt1i7j30lo0uqgoj.jpg)

### 4. 实验

通过link prediciton和fact prediction进行实验。

数据集：

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90u92v81aj30kq04k0t3.jpg)

只选了top200 relation的三元组，并且都加上了反关系。对于每个推理任务 ![[公式]](https://www.zhihu.com/equation?tex=r_i) ，都会去掉所有包含 ![[公式]](https://www.zhihu.com/equation?tex=r_i) 和 ![[公式]](https://www.zhihu.com/equation?tex=r_i^{-1}) 的三元组，再分成训练和测试集。对于链接预测任务来说，h都被看成是一个query，一系列目标实体用不同方式进行排序。而对fact prediction来说，正测试样本会与一些人工生成的负样本一起排序。

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g90ueglesej30nk0vwads.jpg)




## 二、Go for a Walk and Arrive at the Answer Reasoning Over Paths in Knowledge Bases using Reinforcement Learning

### 1、概述

不管是人工构建还是自动构建的知识图谱都存在大量的未完善问题，并且大部分valid facts能够通过分析存在信息推理出。

目前存在的知识推理通常是给定两个实体去推理其关系或者判断一个三元组是否合理。

本文针对问答系统下的问题，提出了MINERVA算法。已知source_entity，relation，使用神经强化学习来预测可能的路径，到达targeted_entity。

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g91woassb2j30pm0d4ta2.jpg)

如图，已知Malala Yousafzai获得的Nobel Peace Prize，我们需要通过谁和她共享诺贝尔奖推理出Kailash Satyarthi。



### 2、模型

#### （1）前提概要

##### A. 预定义

- 实体集E，关系集R。

- 一条事实被存储为(e1,r,e2)的形式，其中e1，e2∈  E，r∈  R。
- 一个知识图谱被表示为一个有向图G = (V,E,R)，其中V，E是图中的顶点和边。V = 实体集E，E⊆  V X R X V。

##### **B. 建模过程中会遇到问题**

- 为消除知识图谱中一对多的情况，考虑反向关系。for an edge (e1,r,e2) ∈ *E*, we add the edge (e2,r−1,e1) to the graph.  
- 使用Query anser模型，通过只计算需要的target_source，增加计算效率

#### （2）环境

环境实际上就是马尔可夫决策所需要的特征：State, Observation, Action, Transition, Reward.

- States: The state space S consists of all valid combinations in E × E × R × E .  包含查询信息，目标信息和agent当前位置信息。*S* = (et,e1q,rq,e2q) 
- Observations: 因为target_source在寻找过程中未知，所以不含e2q。O = (et,e1q,rq). 
- Actions: 一个agent可以选择当前状态的任何出边或静止不动。A*S* = {(et , *r*, *v*) ∈ *E* : *S* = (et , e1q , rq , e2q ), *r* ∈ R, *v* ∈ *V* } ∪ {(*s*, ∅, *s*)} 。静止不动的做法是为了保证在时间T内到达了target_entity后不再发生变化。
- Transition: 预定义状态转移矩阵，根据状态转移矩阵进行计算。δ : S ×A → S defined by δ(*S*,*A*) = (*v*,e1q,rq,e2q), where *S* = (et,e1q,rq,e2q) and *A* = (et,*r*,*v*)). 
- Rewards: 只有当agent到达终止状态时的reward为+1，其余时候都为0.if ST = (et,e1q,rq,e2q) is the final state, then we receive a reward of +1 if et = e2q else 0. , i.e. R(ST)=I{et =e2q}. 

#### （3）策略网络（policy network)



#### （4）训练



### 3、实验







## 三、 Multi-hop knowledge graph reasoning with reward shaping

