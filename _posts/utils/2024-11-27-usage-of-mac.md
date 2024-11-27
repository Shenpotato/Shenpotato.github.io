---
layout: post
title: "mac使用记录"
tags: Tools 
author: Shenpotato
catalog: true
categories: utils
---

> 记录mac上软件

## 常用工具

### 浏览器：Arc

[Arc](https://arc.net/)
目前暂时只支持ios和mac，后续会支持windows。可以无缝将迁移chrome上的信息到arc上
使用技巧介绍：<https://www.youtube.com/watch?app=desktop&v=nlNsCB4SbVc&t=212s>

### 生产力工具：raycast

[raycast](https://www.raycast.com/)。spotlight的升级版
使用技巧介绍：<https://www.youtube.com/watch?v=x6IcLAdUjSI>

- alias/快捷键打开文件
- file + 文件信息查询文件

### MD笔记工具：Typora

https://typora.io/

(免激活方式)[https://github.com/zhuolhc/Mac-typora-activation?tab=readme-ov-file]

### 知识管理工具：Obsidian

### 压缩工具：KeKa

### 视频播放：IINA



## 开发工具

### 包管理工具：HomeBrew

软件管理的工具，类似于ubuntu系统下的apt-get功能

**安装brew**

```ruby
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

**切换brew源**

```ssh
# 替换brew.git:
 cd "$(brew --repo)"
 git remote set-url origin https://mirrors.ustc.edu.cn/brew.git   #中科大
 git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git   #清华

# 替换homebrew-core.git:
 cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
 git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git   #中科大
 git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git  #清华

# 替换homebrew-bottles:
 echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
 source ~/.bash_profile
 echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
 source ~/.bash_profile

# 应用生效:
 brew update
```

切换回官方源

```ssh
# 重置brew.git:
 cd "$(brew --repo)"
 git remote set-url origin https://github.com/Homebrew/brew.git

# 重置homebrew-core.git:
 cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
 git remote set-url origin https://github.com/Homebrew/homebrew-core.git
```

**使用brew**

```ssh
brew install git     #安装git
brew uninstall git    #卸载git
brew search /gi*/    #查询软件/gi*/是个正则表达式，包含在/ /中
brew list        #列出已安装的软件，可以查看brew的安装地址
brew update       #更新brew
brew info        #显示软件信息
brew deps        #显示包依赖

# 将安装的bin文件导入到PATH，以/opt/homebrew/bin为例
vim ~/.bash_profle
export PATH="$PATH:/opt/homebrew/bin"
```



### 代码编辑器：Visual Studio Code

可以通过首选项->设置同步，通过github账号进行不同设备之间vs code配置的同步



### 终端工具：Tabby



****
