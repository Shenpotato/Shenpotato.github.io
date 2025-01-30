---
layout: post
title:  "Jekyll搭建本地博客运行环境"
tags: Tools
author: Shenpotato
catalog: true
categories: utils
---



> 此博客网站通过在github上用jekyll搭建，mac上使用

- 使用brew安装ruby，根据提示进行PATH配置
- /opt/homebrew/opt/ruby/bin/bundle(指定brew安装的bundle) install
- /opt/homebrew/opt/ruby/bin/bundle(指定brew安装的bundle) exec jekyll serve
- 访问<http://localhost:4000>

jekyll建站时的相对路径是对项目而言，因此图片路径可指定为/img/post/xxx.png
