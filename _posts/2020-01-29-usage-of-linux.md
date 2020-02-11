---
layout: post
title: "linux使用"
tags: Tools 
author: Shenpotato
catalog: true
---



> 最近将腾讯云服务器上的操作系统换成了centos的linux系统，因此，这篇文章主要记录了腾讯云服务器的相关使用以及linux的相关使用。

(菜鸟教程链接)[https://www.runoob.com/linux/linux-tutorial.html]



## 一、腾讯云服务器

2019年的暑假写了一个个人简历的展示性网站，并部署在了腾讯云服务器上，还绑定了个域名。之前为了部署的方便，云服务器上的操作系统为windows操作系统。

今年寒假想对网站进行一些调整，并且把服务器的部署环境转为linux。

云服务器上改操作系统是非常方便的，直接在云服务器的控制台中修改实例操作系统为centos7的linux系统。

购买设置的时候默认打开了22端口，用于sshd服务监听是否有远程访问的请求，也正是我们可以进行远程访问的前提。

在mac上的iterm2上直接通过`ssh root@129.204.85.46`访问云服务器，通过`logout`断开ssh与服务器的连接。

在windows上可以使用Xshell和XFtps或者MobaXterm（自己使用后推荐）进行远程登录云服务器。



## 二、Linux相关操作

暂时只记录自己认为常用的和基础的命令。



### 1、网络操作

```
ifconfig / ip addr			#查看网路配置相关信息

ping webaddress					#查看网络联通性

/etc/sysconfig/network-scripts		#网络配置文件的位置

netstat -anp						#查看所有的网络服务
netstat -anp | grep java					#查看服务名为java的服务信息
```



### 2、文件操作

#### 2.1 vim文本编辑器

主要分为三种模式：正常模式，插入模式，命令行模式

通过`vim filename`进入一个文件，当没有这个文件时，默认创建一个名为filename的文件，可带后缀

##### 2.1.1 一般/正常模式

通常进入一个文件时，就是正常模式。可以进行复制粘贴等操作。

- 拷贝当前行/拷贝当前行向下的5行：yy/5yy，粘贴：p
- 删除当前行/当前行向下5行：dd/5dd
- 
- 跳转至文档首行/末行：gg/G
- 撤销前一个操作：u
- 光标跳转到指定某一行：先输入行号，再输入shift➕g



##### 2.1.2 插入模式

在正常模式时输入字母 **i** 进入，对文本进行编辑；使用esc回退到一般模式



##### 2.1.3 命令行模式

提供相关指令，完成读取，存盘，替换，离开vim，显示行号等操作。使用 : 或 / 从一般模式进入命令行模式；使用esc回退到一般模式。

- wq：写入并退出
- q：当文件内容没有改变时，执行退出的操作
- q!：不保存强制退出
- /findword：在文档中查找某个字付（串），回车查找，输入n查找下一个
- set nu：显示文件行号；set nonu：取消显示文件行号

![](https://tva1.sinaimg.cn/large/0082zybpgy1gbskvx8231j314s0u0qb8.jpg)



#### 2.2 文件操作

##### 2.2.1 信息展示

```
pwd 											#当前工作目录绝对路径

ls [option] [dir/file]	 	
ls -a 										#当前目录下所有的文件和目录，包括隐藏的
ls -l											#以列表的方式显示信息

history	[number]					#展示之前使用过的命令
```



##### 2.2.2 当前工作目录移动

```
cd 												#切换到指定目录
cd ../										#转移到上层目录
cd ~											#切换到底层目录
```



##### 2.2.3 创建&删除操作

```
mkdir [option] [dir]			#创建目录

rmdir											#删除空目录
rm 
rm -rf [dirpath]					#强制删除非空目录，r代表递归删除，f代表强制删除不提示
touch [filename.xxx]			#创建空文件，可以同时创建多个
```



##### 2.2.4 拷贝&移动操作

```
cp [option] [file/dir] [dirpath]			#拷贝文件到指定目录
cp -r  test1dir/ testdir2/						#递归拷贝文件夹下所有目录到新目录下

mv														#重命名或移动文件/目录
mv oldfilename newfilanme 		#重命名
mv filanem dirpath						#移动文件
```



##### 2.2.5 查看操作

```
cat													#已只读查看文件内容
cat -n filename | more 			#n代表显示行好，｜more表示管道操作

more 
```

![？](https://tva1.sinaimg.cn/large/006tNbRwgy1gblwayxiovj30ho09ggm2.jpg)

```
less 							#分屏查看文件，按需读取，在大文件时有更高的效率
```

| 操作        | 功能说明                               |
| :---------- | -------------------------------------- |
| space/down  | 向下翻一页                             |
| up          | 向上翻一页                             |
| / substring | 向下搜索字符串 n：向下查找 N：向上查找 |
| ? substring | 向上搜索字符串 n：向上查找 N：向下查找 |
| q           | 离开查看界面                           |

```
head -n number filename			#查看文件前n行内容
tail -n number filename			#查看文件后n行内容
tail -f filename						#监听file文件发生变化的内容（常用）
```



##### 2.2.6 重定向操作

```
> filename 								#将内容覆盖文件
>> filename 							#将内容插入文件末尾

ls -l > a.txt							#将当前目录下的文件（夹）以列表形式插入a.txt文件中
```



##### 2.2.7 查找操作

```
find [findspace] [option]
find /home -name a.txt			#在/home下，根据文件名字查找，还可-user查找指定用户的文件	
find / -size +10M						#在整个linux文件系统下，查找文件大小大于10M的文件

locate filename							#基于数据库进行查询，速度快
updatedb										#locate使用前需要更新一下数据库
```

**grep指令和管道符号｜**

在查询，查看等操作时，可以通过管道指令配合grep操作对内容进行过滤

```
cat hello.txt | grep -ni yes	#n表示显示行号，i表示是否区分大小写
```



##### 2.2.8 文件（解）压缩

```
gzip/gunzip [filepath] filename		#压缩/解压缩指定文件，操作执行后源文件自动删除，只能压缩为.gz格式

zip -r zipname filepath						#递归压缩路径下的文件为指定名称的.zip文件
unzip -d unzippath zipname 				#将zip文件解压缩到指定位置（路径需要注意）

tar [option] filename.tar.gz			#将文件打包为tar.gz结尾
tar -zcvf test.tar.gz test1.txt test2.txt			#将test1和test2打包为test.tar.gz
tar -zcvf test.tar.gz /test/			#打包文件夹
tar -zxvf test.tar.gz -C /test/		#解压到指定位置，目录必须存在
```

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbmu978k9vj30io05yjro.jpg)



##### 2.2.9 文件所有者&用户组修改

```
chown username filename						#修改文件的属主用户 

chgrp groupname filename					#修改文件所属用户组
```



#### 2.3 权限管理

##### 2.3.1 权限介绍

![](https://tva1.sinaimg.cn/large/0082zybpgy1gbs95tbni6j30qe06u0tl.jpg)

**第一串字符串：**

- 0位表示文件类型（d：目录，-：文件，l：软链接，c：字符设备，b：块文件，硬盘）
- 1-3位表示文件所有者的权限
- 4-6位表示文件所属用户组所拥有的权限
- 7-9位表示其他用户的权限

**第二串字符串：**如果是文件，表示硬链接的数目；如果是目录，则表示子目录的数目

**第三，四串字符串：**所属用户和用户组

**第五串字符串：**如果是文件，表示文件大小；如果是目录，则为4096

**后续：**文件最后修改时间和文件名



##### 2.3.2 rwx含义

1. rwx 作用到文件
   - [ r ]代表可读(read): 可以读取,查看
   - [ w ]代表可写(write): 可以修改,但是不代表可以删除该文件,删除一个文件的前提条件是对该文件所在的目录有写权限，才能删除该文件.
   -  [ x ]代表可执行(execute):可以被执行

2. rwx 作用到目录

   - [ r ]代表可读(read): 可以读取，ls 查看目录内容

   -  [ w ]代表可写(write): 可以修改,目录内创建+删除+重命名目录

   - [ x ]代表可执行(execute):可以进入该目录

     

##### 2.3.3 权限操作

```
chmod targetoptionauthority filename 			#权限的修改添加去除操作
chmod u=rwx,g=rx,o=rx test1.txt
chmod 755 test1.txt
```

**target：**u：所有者，g：所有组，o：其他用户，a：所有用户

**option：**+：添加，-：去除，=：赋予权限（覆盖之前的权限）

**authority：**rwx所代表的权限，r = 4，x = 2，x = 1。可通过数字进行修改



### 3、设备操作

#### 3.1 关机

```
shutdown -h now			#立即关机
shutdown -h 1				#一分钟后关机
shutdown -r now			#立即重新启动

halt								#立即关机

reboot							#重启系统

sync								#将内存数据同步到磁盘。建议关机前进行此操作
```



#### 3.2 登录与注销

```
su - username 			#切换为系统管理员

logout							#注销用户
```



### 4、用户&用户组管理

Linux 系统是一个多用户多任务的操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。

Linux 的用户需要至少要属于一个组。

#### 4.1 添加用户&用户组

```
useradd [option] username

useradd -d /home/testuser tu		#指定用户的home目录	

groupadd groupname

useradd -g groupname username		#添加用户时附上所属组 

usermod -g groupname username		#修改用户的组
```

当创建用户成功后，会自动创建和用户同名的home目录。可以通过如上所示进行指定家目录。



#### 4.2 为用户指定密码

```
passwd username
```



#### 4.3 删除用户&用户组

```
userdel username			#删除用户，但保留home目录

userdel -r  username	#删除用户，并删除home目录

groupdel groupname
```

通常在删除用户时，保留home目录



#### 4.4 查询用户

```
id username
```

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbh48gkyxuj30pc034t92.jpg)

返回了用户id号，所在组id号，所在组名。当用户不存在时，返回“无此用户”。



#### 4.5 切换用户

```
su username
```

当从权限高的用户切换至权限低的用户时，不需要输入密码，反之则需要

当需要返回到原来的用户时，使用exit指令



#### 4.6 /etc目录下各项文件

##### 4.6.1 passwd文件

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbh4w458kgj30kk012dfs.jpg)

用户名：口令：用户标示号：组标示号：注释性描述：主目录：登录shell



##### 4.6.2 shadow文件

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbh4y5rfasj30pe00umx7.jpg)

登录名：加密口令：最后一次修改时间：最小时间间隔：最大事件间隔：警告时间：不活动时间：失效时间：标志



##### 4.6.3 group文件

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gbh51qhfrvj307800y0sj.jpg)

组名：口令：组标示号：组内用户列表



### 5、任务调度

定时的调度脚本/代码，完成某个任务。通过crontab完成

```
crontab option
crontab -e/-l/-r					#编辑crontab定时任务/查询crontab任务/删除当前用户所有的任务
service crond restart 		#重启任务调度
```

![](https://tva1.sinaimg.cn/large/0082zybpgy1gbsato3icij30ze0eo75r.jpg)

![](https://tva1.sinaimg.cn/large/0082zybpgy1gbsjn8taluj30qg0mc41f.jpg)

**任务实例：隔一分钟将当前日期添加到/usr/test/mydate.txt**

```
1)	先编写一个文件	/usr/test/mytask1.sh 
		date >> /usr/test/mydate.txt
2)	给 mytask1.sh  一个可以执行权限
		chmod 744 /usr/test/mytask1.sh 
3)	编辑定时调度任务
		crontab -e
4)	添加任务
		*/1 * * * *	/home/mytask1.sh		
```



### 6、进程管理

#### 6.1 查看进程

```
ps [option]						#参数比较多，举例常用的

ps -A									#列出所有行程

ps -u username				#指定用户的进程信息

ps -ef 								#详细列出所有的进程，常与管道过滤结合使用
ps -ef | grep java		#查看java进程
UID				PID		PPID		C	STIME		TTY			TIME			CMD
```

![](https://tva1.sinaimg.cn/large/0082zybpgy1gbsk86lwjzj30ts01wjrk.jpg)

```
pstree -p							#按树状图显示进程
```



#### 6.2 删除进程

```
kill PID									#删除进程
kill -9 PID								#强制删除进程
killall ProcessName				#删除某一进程名称
```



#### 6.3 动态监控进程

```
top [option]							#区别于ps的是，top是实时更新进程的信息

top -d 秒数/ -i 			 		 #使top命令隔几秒更新，默认3s/不显示闲置，僵尸进程
top -p PID								#监控

进入top界面后，可以通过：
1) "u"，回车，输入用户名，查看特定用户的进程
2) "k"，回车，输入进程号，终止特定进程
```



### 7、linux磁盘分区与挂载

搁置