---
layout: post
title: "人工智能-归结推理"
tags: knowledge_reasoning logic 
author: Shenpotato
catelog: true
---

CSIT6000F Aritifical Intelligence 归结演绎推理



## 一、什么是归结演绎推理

- 归结演绎推理是一种基于逻辑“反证法”的机械化定理证明方法。其基本思想是把永真性的证明转化为不可满足性的证明。即要证明$$P\implies{Q}$$永真，只要能够证明$$\neg(P)\vee{Q}$$为不可满足即可。

- 谓词公式不可满足的充要条件是其子句集不可满足。因此，要把谓词公式转换为子句集，再用鲁滨逊归结原理求解子句集是否不可满足。如果子句集不可满足，则$$P\implies{Q}$$永真
  



## 二、逻辑学基础

### 1、谓词公式的永真性

如果谓词公式P对非空个体域D上的任一解释都取得真值T，则称P在D上是永真的；如果P在任何非空个体域上均是永真的，则称P永真。

### 2、谓词公式的可满足性

对于谓词公式P，如果至少存在D上的一个解释，使公式P在此解释下的真值为T，则称公式P在D上是可满足的。

### 3、谓词公式的范式

范式是公式的标准形式，公式往往需要变换为同它等价的范式，以便对它们进行一般性的处理。在谓词逻辑中，根据量词在公式中出现的情况，可将谓词公式的范式分为以下两种。

**前束范式**

- 任一含有量词的谓词公式均可化为与其对应的前束范式

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95spz9fycj30xf065tab.jpg)

**Skolem 范式**

- 任一含有量词的谓词公式均可化为与其对应的Skolem范式

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95srj5egej30xb02o74o.jpg)



### 4、子句和子句集

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95srswvctj30y80a0ac4.jpg)



### 5、谓词公式化为子句集

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95ss9vd57j30qd0v00xu.jpg)



## 二、鲁滨逊归结原理（消解原理）

### 1、基本思想

- 检查子句集S中是否包含空子句，若包含，则S不可满足。
- 若不包含，在S中选择合适的子句进行归结，一旦归结出空子句，就说明S是不可满足的



### 2、命题逻辑中的归结原理：

设$$C_1$$和$$C_2$$是子句集中的任意两个子句，如果$$C_1$$中的文字$$L_1$$与$$C_2$$中的文字$$L_2$$互补，那么从$$C_1$$和$$C_2$$中分别消去$$L_1$$和$$L_2$$，并将两个子句中余下的部分析取，构成一个新子句$$C_{12}$$。其中$$C_{12}$$称为$$C_1$$和$$C_2$$的归结式，$$C_1$$和$$C_2$$称为$$C_{12}$$的亲本子句。

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95yr8w1oaj30r90h8whv.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95yrbfqxgj30fv0a7gm4.jpg)



### 3、谓词逻辑中的归结原理：

设$$C_1$$和$$C_2$$是两个没有公共变元的子句，$$L_1$$和$$L_2$$分别是$$C_1$$和$$C_2$$中的文字。如果$$L_1$$和$$L_2$$存在最一般合一$$\delta$$，则称$$C_{12}=(C_1\delta-L_1\delta)\cup{(C_2\delta-L_2\delta)}$$为$$C_1$$和$$C_2$$的二元归结式，而$$L_1$$合$$L_2$$为归结式上的文字。

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zlsls7vj30px08b75l.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zlvnkmtj30g9096mxh.jpg)





## 三、归结反演

### 1、证明定理

- 将已知前提表示为谓词公式$$F$$
- 将待证明的结论表示为谓词公式$$Q$$，并否定得到$$\neg{Q}$$
- 把谓词公式集$$\{F,\neg{Q}\}$$化为子句集$$S$$
- 应用归结原理对子句集$$S$$中的子句进行归结，并把每次归结得到的归结式都并入到$$S$$中。如此反复进行，若出现了空子句，则停止归结，此时就证明了$$Q$$为真

### 2、求解问题

- 已知前提$$F$$用谓词公式表示
- 把待求解的问题$$Q$$用谓词公式表示，并否定$$Q$$，再与$$ANSWER$$构成析取式$$(\neg{Q}\vee{ANSWER})$$
- 把谓词公式集$$\{F,(\neg{Q}\vee{ANSWER})\}$$化为子句集$$S$$
- 对$$S$$应用归结原理进行归结
- 若得到归结式$$ANSWER$$，则答案就在$$ANSWER$$中

### 3、应用

#### （1）归结反演证明定理

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zyqdcdlj30r70bmq4h.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zyu9glij30p80z80xg.jpg)

#### （2）归结反演求解问题

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zyyjy32j30ho0atmxu.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zzh7evpj30id0c50tm.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zzkes1sj30i40b5t9b.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g95zzo2ivzj30kh0hhjsu.jpg)