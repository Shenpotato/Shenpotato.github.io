---
layout: post
title: "mac使用记录"
tags: Tools 
author: Shenpotato
catalog: true
---



> 记录mac上特殊的使用技巧和软件



### 1. HomeBrew

软件管理的工具，类似于ubuntu系统下的apt-get功能

#### 1.1 安装brew

```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```



#### 1.2 切换brew源

```
# 替换brew.git:
 cd "$(brew --repo)"
 git remote set-url origin https://mirrors.ustc.edu.cn/brew.git   #中科大
 git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git	  #清华

# 替换homebrew-core.git:
 cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
 git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git   #中科大
 git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git		#清华

# 替换homebrew-bottles:
 echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
 source ~/.bash_profile
 echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
 source ~/.bash_profile

# 应用生效:
 brew update
```

切换回官方源

```
# 重置brew.git:
 cd "$(brew --repo)"
 git remote set-url origin https://github.com/Homebrew/brew.git

# 重置homebrew-core.git:
 cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
 git remote set-url origin https://github.com/Homebrew/homebrew-core.git
```



#### 1.3 使用brew

```
brew install git 				#安装git

brew uninstall git 			#卸载git

brew search /gi*/ 			#查询软件/gi*/是个正则表达式，包含在/ /中

brew list								#列出已安装的软件

brew update							#更新brew

brew info								#显示软件信息

brew deps								#显示包依赖
```

