---
layout: post
title: "绿联docker使用配置"
tags: Tools 
author: Shenpotato
catalog: true
categories: utils
---



绿联官方配置的docker源不行，需要重新配置

1. 在绿联设置中打开允许ssh访问

![image-20250515153616356](/img/in-post/utils/image-20250515153616356.png)

1. 使用对应的用户名密码通过ssh登陆绿联终端

```shell
## 登陆
ssh useraccount@ip

## 编辑docker配置
sudo vim /etc/docker/daemon.json

## 配置内容
## registry-mirrors中填https://github.com/dongyubin/DockerHub可用的docker地址
{
        "data-root": "/volume1/@docker",
        "registry-mirrors": ["https://dytt.online"]
}

## 重新加载
sudo systemctl daemon-reload

## 重启docker
sudo systemctl restart docker
```
