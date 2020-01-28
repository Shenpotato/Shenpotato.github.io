---
layout: post
title: "Git使用"
tags: Tools 
author: Shenpotato
catalog: true
---



> 本文主要讲述了什么是Git，如何配置本地Git以及本地Git仓库和远程Github如何进行交互
>
> 操作以mac系统下为例



## 一、Git和Github 的概念

- Git是一个版本控制软件，进行控制的形式多样，可通过git bash，git gui实现本地仓库的创建，与远程仓库的连接，上传内容至远程仓库，从远程仓库下载内容至本地仓库等功能。

- Github是一个版本控制社区网站。用户可在Github上申请账号，并创建版本仓库。在Github上的仓库即为远程仓库。



## 二、Git的使用

### 1、Git的安装与配置

#### （1）安装

安装部分不多做讲解，主要就是搜索git下载，安装的过程

#### （2）配置

以配置整台机子的Git仓库为例。通过`git config --global`设置username以及userpassword等属性，实现与Github相连接。



### 2、Git的使用

我们以命令行来讲解Git的使用。

如上所说，Git是一个版本控制软件，它维护的东西是仓库，在仓库上实现代码、文档修改的记录，回退等功能。

我们以如何将本地的文件上传至远程仓库来讲解基础的Git使用。



#### （1）将本地文件上传至Github仓库

- 在本地打开终端，将当前目录移至需上传的目录
- 通过`git init.`创建初始本地仓库
- 通过`git add .`将本地需要上传的文件添加至缓冲区，可通过键入具体的文件名实现上传具体的文件至缓冲区
- 通过`git commit -m "commitmessage"`将缓冲区的文件上传至本地仓库。其中commitmessage为自己想要为此次提交添加的备注，方便日后查看。
- 接着，我们需要在Github上新建仓库，这个仓库即为远程仓库，并获取到https地址。
- 通过`git remote add origin httpsaddr`将本地仓库与远程仓库绑定，其中httpsaddr是远程仓库地址。
- 通过`git push -f origin master`将当前分支master推送到远端。其中-f是忽略本地和远程仓库冲突的部分，强制将本地仓库推送至远程仓库。就此，本地文件上传到远程仓库的过程完成。



#### （2）创建和合并分支

在实际生产中，每个人都有负责的部分代码，会对代码进行修改。为了实现每个人都可以对代码进行修改且不干扰别人的修改，分支的概念随之产生。通常，master分支我们称为主分支。我们一般从master分之下clone代码，并在自己的分支上进行修改，最后再merge到主分支master分支之上。

总结创建和合并分支的命令：

- 查看分支：`git branch`
- 创建新分支：`git branch newbranchname`
- 切换分支：`git checkout branch name`
- 创建+切换分支：`git checkout -b branchname`
- 删除分支：`git branch -d branchname`
- 合并分支：`git merge branchname`



## 三、patch的概念

### 1、应用场景

当多人维护一个项目的时候，组员发现一个项目有bug时但又没有提交修改的权限，所以需要将自己所做的修改用diff命令生成一个patch，patch记录了组员所做的修改，组长能更高效的审视组员所做的修改。



### 2、diff命令制作补丁

` diff [option] oldfile newfile > patchname.patch`

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbccv32ybbj30xm0bxmy6.jpg)

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbcct9luyij30u012t42i.jpg)

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbcctg10dqj30u012tq7d.jpg)