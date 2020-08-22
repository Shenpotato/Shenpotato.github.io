---
layout: post
title: "IDEA的相关使用"
tags: Tools 
author: Shenpotato
catalog: true
---



> 记录IntelliJ IDEA的使用



### 1、配置类注释和方法注释

#### （1）类注释

Preferences -> Editor -> File and Code Templates -> includes -> File Header

![](https://tva1.sinaimg.cn/large/0082zybpgy1gc679h40tjj315n0u0q75.jpg)

```
/**
 * @author  ShenPotato
 * @date  ${DATE} ${TIME}
 * @version 1.0
 */
```

在每次生成类时，就会自带类注释头。

#### （2）方法注释

Preferences -> Editor -> Live Templates -> 右边+号添加自己的Template Group -> 选择创建好的TemplateGroup，添加Template。

![](https://tva1.sinaimg.cn/large/0082zybpgy1gc678n4nfrj311f0u0gpn.jpg)

Abbreviation是快捷键，当键入这个字符串时，结合Options中的Expand with（Tab)键，生成模版。模版信息：

```
/**
* @author ShenPotato
* @descrpiton 
* @date $date$ $time$
*/
```

**网上的模版配置**：
文件头：

```
/*
 * <p>项目名称: ${project_name} </p> 
 * <p>文件名称: ${file_name} </p> 
 * <p>描述: [类型描述] </p>
 * <p>创建时间: ${date} </p>
 * <p>公司信息: ************公司 *********部</p> 
 * @author <a href="mail to: *******@******.com" rel="nofollow">作者</a>
 * @version v1.0
 * @update [序号][日期YYYY-MM-DD] [更改人姓名][变更描述]
 */
```
方法：
```
/**
 * @Title：${enclosing_method}
 * @Description: [功能描述]
 * @Param: ${tags}
 * @Return: ${return_type}
 * @author <a href="mail to: *******@******.com" rel="nofollow">作者</a>
 * @CreateDate: ${date} ${time}</p> 
 * @update: [序号][日期YYYY-MM-DD] [更改人姓名][变更描述]     
 */
```



### 2、常用快捷键

以mac上为例：

option + enter：导入包

control + enter：自动生成构造函数，setter/getter函数等方法

command + option + shift + u：类的集成结构图





### 3、将多个项目整合到一个项目中

1. 新建一个项目

2. 打开project structure，在Project中设置好SDK等相关配置

3. 在project structure的module中选择项目导入

   ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghn52haev3j310r0u0whl.jpg)

### 

#### 