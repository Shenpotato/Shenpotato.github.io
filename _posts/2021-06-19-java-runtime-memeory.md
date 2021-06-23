---
21layout: post
title: "java内存区域"
tags: jvm
author: Shenpotato
catalog: true
---



> 参考：
>
> [Java内存区域（运行时数据区域）和内存模型（JMM）](https://www.cnblogs.com/czwbig/p/11127124.html)
>
> [一个Java对象和Hashmap对象占用多大内存](https://blog.csdn.net/belongtocode/article/details/103377187)
>
> [jvm系列(二):JVM内存结构]( https://mp.weixin.qq.com/s?__biz=MzI4NDY5Mjc1Mg==&mid=2247483949&idx=1&sn=8b69d833bbc805e63d5b2fa7c73655f5&chksm=ebf6da52dc815344add64af6fb78fee439c8c27b539b3c0e87d8f6861c8422144d516ae0a837&scene=21#wechat_redirect)
>
> 《深入理解java虚拟机 ： JVM高级特性与最佳实践(第2版)》》周志明
>
> [Java内存溢出代码实例](https://blog.csdn.net/weixin_43754564/article/details/101638409)



# 一、概述

![Image](https://tva1.sinaimg.cn/large/008i3skNgy1grp4kww7lxj30ho0asjs6.jpg)

JVM内存结构主要有三大块：**堆内存**、**方法区**和**栈**。堆内存是JVM中最大的一块由年轻代和老年代组成，而年轻代内存又被分成三部分，**Eden空间**、**From Survivor空间**、**To Survivor空间**,默认情况下年轻代按照**8:1:1**的比例来分配；

方法区存储类信息、常量、静态变量等数据，是线程共享的区域，为与Java堆区分，方法区还有一个别名Non-Heap(非堆)；栈又分为java虚拟机栈和本地方法栈主要用于方法的执行。

下图展示详细区分：

![](https://tva1.sinaimg.cn/large/008i3skNgy1grnm9q6ajwj30yg0g7tbu.jpg)



## 1. Java堆

对于大多数应用来说，Java 堆（Java Heap）是 Java 虚拟机所管理的内存中最大的一块。Java 堆是被所有线程共享的一块内存区域，在虚拟机启动时创建。此内存区域的唯一目的就是存放对象实例，几乎所有的对象实例都在这里分配内存。

堆是垃圾收集器管理的主要区域，因此很多时候也被称做“GC堆”（Garbage Collected Heap）。从内存回收的角度来看，由于现在收集器基本都采用分代收集算法，所以 Java 堆中还可以细分为：新生代和老年代；再细致一点的有 Eden 空间、From Survivor 空间、To Survivor 空间等。从内存分配的角度来看，线程共享的 Java 堆中可能划分出多个线程私有的分配缓冲区（Thread Local Allocation Buffer,TLAB）。

Java 堆可以处于物理上不连续的内存空间中，只要逻辑上是连续的即可，当前主流的虚拟机都是按照可扩展来实现的（通过 -Xmx 和 -Xms 控制）。如果在堆中没有内存完成实例分配，并且堆也无法再扩展时，将会抛出 OutOfMemoryError 异常。



## 2. 栈

### 2.1 Java虚拟机栈

Java 虚拟机栈（Java Virtual Machine Stacks）是**线程私有的，它的生命周期与线程相同**。

**虚拟机栈描述的是 Java 方法执行的内存模型**：**每个方法在执行的同时都会创建一个栈帧**（Stack Frame，**是方法运行时的基础数据**结构）用于**存储局部变量表、操作数栈、动态链接、方法出口**等信息。**每一个方法从调用直至执行完成的过程，就对应着一个栈帧在虚拟机栈中入栈到出栈的过程。**

在活动线程中，只有**位于栈顶的帧才是有效的，称为当前栈帧**。正在执行的方法称为当前方法，栈帧是方法运行的基本结构。在执行引擎运行时，所有指令都只能针对当前栈帧进行操作。

![操作栈的压栈与出栈-《码出高效》](https://tva1.sinaimg.cn/large/008i3skNgy1grnmknba61j30yg0l97fh.jpg)

#### 2.1.1 局部变量表

局部变量表是**存放方法参数和局部变量**的区域。 局部变量没有准备阶段， 必须显式初始化。如果是非静态方法，**则在 index[0] 位置上存储的是方法所属对象的实例引用**，一个引用变量占 4 个字节，**随后存储的是参数和局部变量**。字节码指令中的 STORE 指令就是将操作栈中计算完成的局部变呈写回局部变量表的存储空间内。

虚拟机栈规定了两种异常状况：如果**线程请求的栈深度大于虚拟机所允许的深度，将抛出 StackOverflowError 异常**；如果虚拟机栈可以动态扩展（当前大部分的 Java 虚拟机都可动态扩展），**如果扩展时无法申请到足够的内存，就会抛出 OutOfMemoryError 异常**。

#### 2.2.2 操作栈

操作栈是个初始状态为空的桶式结构栈。在方法执行过程中， 会有各种指令往栈中写入和提取信息。JVM 的执行引擎是基于栈的执行引擎， 其中的栈指的就是操作栈。字节码指令集的定义都是基于栈类型的，栈的深度在方法元信息的 stack 属性中。

**i++ 和 ++i 的区别：**

1. i++：从局部变量表取出 i 并压入操作栈(load memory)，然后对局部变量表中的 i 自增 1(add&store memory)，将操作栈栈顶值取出使用，如此线程从操作栈读到的是自增之前的值。
2. ++i：先对局部变量表的 i 自增 1(load memory&add&store memory)，然后取出并压入操作栈(load memory)，再将操作栈栈顶值取出使用，线程从操作栈读到的是自增之后的值。

之前之所以说 i++ 不是原子操作，即使使用 volatile 修饰也不是线程安全，就是因为，可能 i 被从局部变量表（内存）取出，压入操作栈（寄存器），操作栈中自增，使用栈顶值更新局部变量表（寄存器更新写入内存），其中分为 3 步，volatile 保证可见性，保证每次从局部变量表读取的都是最新的值，但可能这 3 步可能被另一个线程的 3 步打断，产生数据互相覆盖问题，从而导致 i 的值比预期的小。

#### 2.2.3  动态链接

每个栈帧中包含一个在常量池中对当前方法的引用， 目的是支持方法调用过程的动态连接。

#### 2.2.4 方法返回地址

方法执行时有两种退出情况：

1. 正常退出，即正常执行到任何方法的返回字节码指令，如 RETURN、IRETURN、ARETURN 等；
2. 异常退出。

无论何种退出情况，都将返回至方法当前被调用的位置。方法退出的过程相当于弹出当前栈帧，退出可能有三种方式：

1. 返回值压入上层调用栈帧。

2. 异常信息抛给能够处理的栈帧。

3. PC计数器指向方法调用后的下一条指令。

   

### 2.2 本地方法栈

本地方法栈（Native Method Stack）与虚拟机栈所发挥的作用是非常相似的，它们之间的区别不过是虚拟机栈为虚拟机执行 Java 方法（也就是字节码）服务，而本地方法栈则为虚拟机使用到的 Native 方法服务。Sun HotSpot 虚拟机直接就把本地方法栈和虚拟机栈合二为一。与虚拟机栈一样，本地方法栈区域也会抛出 StackOverflowError 和 OutOfMemoryError 异常。

线程开始调用本地方法时，会进入 个不再受 JVM 约束的世界。本地方法可以通过 JNI(Java Native Interface)来访问虚拟机运行时的数据区，甚至可以调用寄存器，具有和 JVM 相同的能力和权限。 当大量本地方法出现时，势必会削弱 JVM 对系统的控制力，因为它的出错信息都比较黑盒。对内存不足的情况，本地方法栈还是会抛出 nativeheapOutOfMemory。

JNI 类本地方法最著名的应该是 `System.currentTimeMillis()` ，JNI使 Java 深度使用操作系统的特性功能，复用非 Java 代码。 但是在项目过程中， 如果大量使用其他语言来实现 JNI , 就会丧失跨平台特性。



## 3. 方法区

方法区（Method Area）与 Java 堆一样，是各个线程共享的内存区域，它用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译器编译后的代码等数据。虽然
Java 虚拟机规范把方法区描述为堆的一个逻辑部分，但是它却有一个别名叫做 Non-Heap（非堆），目的应该是与 Java 堆区分开来。

Java 虚拟机规范对方法区的限制非常宽松，除了和 Java 堆一样不需要连续的内存和可以选择固定大小或者可扩展外，还可以选择不实现垃圾收集。垃圾收集行为在这个区域是比较少出现的，其内存回收目标主要是针对常量池的回收和对类型的卸载。当方法区无法满足内存分配需求时，将抛出 OutOfMemoryError 异常。

**JDK8 之前，Hotspot 中方法区的实现是永久代（Perm），JDK8 开始使用元空间（Metaspace），以前永久代所有内容的字符串常量移至堆内存，其他内容移至元空间，元空间直接在本地内存分配。**

为什么要使用元空间取代永久代的实现？

1. 字符串存在永久代中，容易出现性能问题和内存溢出。
2. 类及方法的信息等比较难确定其大小，因此对于永久代的大小指定比较困难，太小容易出现永久代溢出，太大则容易导致老年代溢出。
3. 永久代会为 GC 带来不必要的复杂度，并且回收效率偏低。
4. 将 HotSpot 与 JRockit 合二为一。

### 3.1 运行时常量池

运行时常量池（Runtime Constant Pool）是方法区的一部分。Class 文件中除了有类的版本、字段、方法、接口等描述信息外，还有一项信息是常量池（Constant Pool Table），用于存放编译期生成的各种字面量和符号引用，这部分内容将在类加载后进入方法区的运行时常量池中存放。

一般来说，除了保存 Class 文件中描述的符号引用外，还会把翻译出来的直接引用也存储在运行时常量池中。

运行时常量池相对于 Class 文件常量池的另外一个重要特征是具备动态性，Java 语言并不要求常量一定只有编译期才能产生，也就是并非预置入 Class 文件中常量池的内容才能进入方法区运行时常量池，运行期间也可能将新的常量放入池中，这种特性被开发人员利用得比较多的便是 String 类的 intern() 方法。

既然运行时常量池是方法区的一部分，自然受到方法区内存的限制，当常量池无法再申请到内存时会抛出 OutOfMemoryError 异常。



## 4. 程序计数器

程序计数器（Program Counter Register）是一块较小的内存空间，它可以看作是**当前线程**所执行的字节码的行号指示器。

由于 Java 虚拟机的**多线程是通过线程轮流切换并分配处理器执行时间的方式来实现**的，在任何一个确定的时刻，一个处理器内核都只会执行一条线程中的指令。

因此，为了**线程切换后能恢复到正确的执行位置**，**每条线程都需要有一个独立的程序计数器**，各条线程之间计数器互不影响，独立存储，我们称这类内存区域为“线程私有”的内存。

如果线程正在执行的是一个 **Java 方法，这个计数器记录的是正在执行的虚拟机字节码指令的地址**；如果正在执行的是 **Native 方法，这个计数器值则为空（Undefined）**。此内存区域是唯一一个在 Java 虚拟机规范中没有规定任何 OutOfMemoryError 情况的区域。



## 5. 实例

### 5.1 jvm参数设置

![Image](https://tva1.sinaimg.cn/large/008i3skNgy1grp4sevh7aj30hs070glt.jpg)

控制参数

- -Xms设置堆的最小空间大小。
- -Xmx设置堆的最大空间大小。
- -XX:NewSize设置新生代最小空间大小。
- -XX:MaxNewSize设置新生代最大空间大小。
- -XX:PermSize设置永久代最小空间大小。
- -XX:MaxPermSize设置永久代最大空间大小。
- -Xss设置每个线程的堆栈大小。

没有直接设置老年代的参数，但是可以设置堆空间大小和新生代空间大小两个参数来间接控制。

> 老年代空间大小=堆空间大小-年轻代大空间大小



### 5.2 堆、栈、方法区分配

所有的对象在实例化后的整个运行周期内，都被存放在堆内存中。堆内存又被划分成不同的部分：伊甸区(Eden)，幸存者区域(Survivor Sapce)，老年代（Old Generation Space）。

方法的执行都是伴随着线程的。原始类型的本地变量以及引用都存放在线程栈中。而引用关联的对象比如String，都存在在堆中。为了更好的理解上面这段话，我们可以看一个例子：

```java
import java.text.SimpleDateFormat;
import java.util.Date;
import org.apache.log4j.Logger;
public class HelloWorld {    
  private static Logger LOGGER = Logger.getLogger(HelloWorld.class.getName());
  public void sayHello(String message) {
    SimpleDateFormat formatter = new SimpleDateFormat("dd.MM.YYYY");
    String today = formatter.format(new Date());
    LOGGER.info(today + ": " + message);
  }
}
```

这段程序的数据在内存中的存放如下：

![Image](https://tva1.sinaimg.cn/large/008i3skNgy1grp4tifknij30hs0as3zm.jpg)



### 5.3 常见的jvm错误

对内存结构清晰的认识同样可以帮助理解不同OutOfMemoryErrors：

```
Exception in thread “main”: java.lang.OutOfMemoryError: Java heap space
```

原因：对象不能被分配到堆内存中

```
Exception in thread “main”: java.lang.OutOfMemoryError: PermGen space
```

原因：类或者方法不能被加载到老年代。它可能出现在一个程序加载很多类的时候，比如引用了很多第三方的库；

```
Exception in thread “main”: java.lang.OutOfMemoryError: Requested array size exceeds VM limit
```

原因：创建的数组大于堆内存的空间

```
Exception in thread “main”: java.lang.OutOfMemoryError: request <size> bytes for <reason>. Out of swap space?
```

原因：分配本地分配失败。JNI、本地库或者Java虚拟机都会从本地堆中分配内存空间。

```
Exception in thread “main”: java.lang.OutOfMemoryError: <reason> <stack trace>（Native method）
```

原因：同样是本地方法内存分配失败，只不过是JNI或者本地方法或者Java虚拟机发现



# 二、jvm中对象

对象在内存中存储的布局可以分为3个部分：**对象头（Header），实例数据（Instance Data），对齐填充（Padding）**。



## 1. 对象头

对象头包括两部分信息：

一部分存储对象自身运行时数据。如哈希码，GC分代年龄，锁状态标志，线程持有锁，偏向线程ID等。称为Mark word。

另一部分为类型指针，对象指向他的类元数据。

如果是数组，对象头中需要有一块用于记录数组长度。

### 1.1 类型指针详解

类型指针分为句柄与直接指针两种。

#### 1.1.1 句柄

Java栈本地变量表的reference指向Java堆中句柄池，句柄池中存在两个指针，一个指针指向Java堆实例池中的对象实例数据，另一个指针指向方法区中的对象类型数据。

![img](https://tva1.sinaimg.cn/large/008i3skNgy1grsm3jgffmj30ls0b2djj.jpg)

#### 1.1.2 直接指针

Java栈本地变量表的reference指向Java堆实例池中的对象实例数据，该数据后的指针指向方法区中的对象类型数据。

![img](https://tva1.sinaimg.cn/large/008i3skNgy1grsm3nej61j30m90apwht.jpg)

句柄的优势在于，在对象被移动时（如垃圾回收），只需要修改句柄中的实例数据指针，不需要修改reference本身；直接指针的优势在于访问速度快。HotSpot采用直接指针的方法。



## 2.实例对象

对象真正存储的有效信息，代码中所定义的各种类型的字段内容。从父类继承下来的字段也会显示在子类对象中。



## 3. 对齐填充

仅起占位符的作用。由于HotSpot jvm要求对象的起始地址是8字节的整数倍。其用于填充对象满足8字节的整数倍



# 三、常见内存溢出

内存溢出（Out Of Memory），又称为oom。



## 1. 堆内存溢出

Java堆用于存储对象实例，因此需要不断地创建对象，并且保证GC Roots之间存在可达路径避免被垃圾回收。

```java
/*
 ** VM Args: -Xms20m -Xmx20m -XX:+HeapDumpOnOutOfMemoryError
 */
public class HeapDemo {

    public static void main(String[] args) {
        int i = 1;
        List<byte[]> list = new ArrayList<byte[]>();

        while (true) {
            list.add(new byte[10 * 1024 * 1024]);
            System.out.println("第" + (i++) + "次分配");
        }
    }
}
```



## 2. 栈内存溢出

每个线程都有一个私有的栈，随着线程的创建而创建，栈里面存放着“栈帧”，每个方法都会创建一个栈帧，栈帧中存放着局部变量表（基本数据类型和对象引用），操作数栈，方法出口等基本信息。和堆一样大小可以固定也可以动态扩展。堆溢出有两种思路：
1.不断创建线程。
2.不断执行方法

```java
/*
** 通过不断创建线程来模拟栈溢出
 */
public class StackDemo1 {
    public static void main(String[] args) {
        int i =0;

        while(true) {
            new Thread(new Runnable() {
                @Override
                public void run() {

                }
            }).start();
        }
    }
}

/*
** 通过不断执行方法来模拟栈溢出
 */
public class StackDemo2 {

    static int depth = 0;

    public void countMethod() {
        depth++;
        countMethod();
    }

    public static void main(String[] args) {
        StackDemo2 demo = new StackDemo2();
        try{
            demo.countMethod();
        }finally {
            System.out.println("方法执行了"+depth+"次");
        }

    }
}
```



## 3. 常量池内存溢出

如果要模拟常量池溢出，可以使用String的intern()方法。如果常量池包含一个该字符串，就返回该String对象，否则就将该对象添加到常量池中。
注意：JDK1.7以后intern()方法改为在常量池记录Java Heap中首次出现的字符串的引用，因此执行测试代码会导致堆内存溢出。

```java
/*
**	-Xms5m -Xmx5m
*/
public class ConstantPoolDemo {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        int i = 0;
        while(true){
            list.add(String.valueOf(i++).intern());
        }
    }
}
```



## 4. 方法区溢出

方法区存放的是Class的相关信息，因此可以不断动态添加类来模拟方法区溢出（CGLib）

```java
/*
 **  -XX:PermSize=10M -XX:MaxPermSize=10M
 */
public class MethodAreaDemo {
    public static void main(String[] args) {
        while (true) {
            Enhancer enhancer = new Enhancer();
            enhancer.setSuperclass(Person.class);
            enhancer.setUseCache(false);
            enhancer.setCallback(new MethodInterceptor() {
                public Object intercept(Object obj, Method arg1, Object[] args, MethodProxy proxy) throws Throwable {
                    return proxy.invokeSuper(obj, args);
                }
            });
            Person person = (Person) enhancer.create();
            person.Hi("Wzy");
        }
    }

    static class Person {
        public String Hi(String str) {
            return "hello " + str;
        }
    }
}  
```







# 三、直接内存

直接内存（Direct Memory）并不是虚拟机运行时数据区的一部分，也不是 Java 虚拟机规范中定义的内存区域。

在 JDK 1.4 中新加入了 NIO，引入了一种基于通道（Channel）与缓冲区（Buffer）的 I/O 方式，它可以使用 Native 函数库直接分配堆外内存，然后通过一个存储在 Java 堆中的 DirectByteBuffer 对象作为这块内存的引用进行操作。这样能在一些场景中显著提高性能，因为避免了在 Java 堆和 Native 堆中来回复制数据。

显然，本机直接内存的分配不会受到 Java 堆大小的限制，但是，既然是内存，肯定还是会受到本机总内存（包括 RAM 以及 SWAP 区或者分页文件）大小以及处理器寻址空间的限制。服务器管理员在配置虚拟机参数时，会根据实际内存设置 -Xmx 等参数信息，但经常忽略直接内存，使得各个内存区域总和大于物理内存限制（包括物理的和操作系统级的限制），从而导致动态扩展时出现 OutOfMemoryError 异常。

![Java线程与内存 -《码出高效》](https://tva1.sinaimg.cn/large/008i3skNgy1grnmkm1v7qj30yg0i77fd.jpg)



# 四、Java内存模型

Java内存模型是共享内存的并发模型，线程之间主要通过读-写共享变量（堆内存中的实例域，静态域和数组元素）来完成隐式通信。

Java 内存模型（JMM）控制 Java 线程之间的通信，决定一个线程对共享变量的写入何时对另一个线程可见。



## 1. 计算机高速缓存和缓存一致性

计算机在高速的 CPU 和相对低速的存储设备之间使用高速缓存，作为内存和处理器之间的缓冲。将运算需要使用到的数据复制到缓存中，让运算能快速运行，当运算结束后再从缓存同步回内存之中。

在多处理器的系统中(或者单处理器多核的系统)，每个处理器内核都有自己的高速缓存，它们有共享同一主内存(Main Memory)。

当多个处理器的运算任务都涉及同一块主内存区域时，将可能导致各自的缓存数据不一致。

为此，需要各个处理器访问缓存时都遵循一些协议，在读写时要根据协议进行操作，来维护缓存的一致性。

![图摘自51CTO技术栈 作者 陈彩华](https://tva1.sinaimg.cn/large/008i3skNgy1grnmkmli6qj30k00ewwjg.jpg)

## 2. JVM主内存与工作内存

Java 内存模型的主要目标是定义程序中各个变量的访问规则，即在虚拟机中将变量（线程共享的变量）存储到内存和从内存中取出变量这样底层细节。

Java内存模型中规定了所有的变量都存储在主内存中，每条线程还有自己的工作内存，线程对变量的所有操作都必须在工作内存中进行，而不能直接读写主内存中的变量。

这里的工作内存是 JMM 的一个抽象概念，也叫本地内存，其存储了该线程以读 / 写共享变量的副本。

**就像每个处理器内核拥有私有的高速缓存，JMM 中每个线程拥有私有的本地内存。**

不同线程之间无法直接访问对方工作内存中的变量，线程间的通信一般有两种方式进行，一是通过消息传递，二是共享内存。Java 线程间的通信采用的是共享内存方式，线程、主内存和工作内存的交互关系如下图所示：

![img](https://tva1.sinaimg.cn/large/008i3skNgy1grnmknz2yaj30yg0lmad6.jpg)

这里所讲的主内存、工作内存与 Java 内存区域中的 Java 堆、栈、方法区等并不是同一个层次的内存划分，这两者基本上是没有关系的，如果两者一定要勉强对应起来，那从变量、主内存、工作内存的定义来看，主内存主要对应于Java堆中的对象实例数据部分，而工作内存则对应于虚拟机栈中的部分区域。



## 3. 重排序和happens-before规则

在执行程序时为了提高性能，编译器和处理器常常会对指令做重排序。重排序分三种类型：

1. 编译器优化的重排序。编译器在不改变单线程程序语义的前提下，可以重新安排语句的执行顺序。
2. 指令级并行的重排序。现代处理器采用了指令级并行技术（Instruction-Level Parallelism， ILP）来将多条指令重叠执行。如果不存在数据依赖性，处理器可以改变语句对应机器指令的执行顺序。
3. 内存系统的重排序。由于处理器使用缓存和读 / 写缓冲区，这使得加载和存储操作看上去可能是在乱序执行。

从 java 源代码到最终实际执行的指令序列，会分别经历下面三种重排序：

![img](https://tva1.sinaimg.cn/large/008i3skNgy1grnmkorj7pj30of050t8l.jpg)

JMM 属于语言级的内存模型，它确保在不同的编译器和不同的处理器平台之上，通过禁止特定类型的编译器重排序和处理器重排序，为程序员提供一致的内存可见性保证。

java 编译器禁止处理器重排序是通过在生成指令序列的适当位置会插入内存屏障（重排序时不能把后面的指令重排序到内存屏障之前的位置）指令来实现的。

**happens-before**

从 JDK5 开始，java 内存模型提出了 happens-before 的概念，通过这个概念来阐述操作之间的内存可见性。

如果一个操作执行的结果需要对另一个操作可见，那么这两个操作之间必须存在 happens-before 关系。这里提到的两个操作既可以是在一个线程之内，也可以是在不同线程之间。

**这里的“可见性”是指当一条线程修改了这个变量的值，新值对于其他线程来说是可以立即得知的。**

如果 A happens-before B，那么 Java 内存模型将向程序员保证—— A 操作的结果将对 B 可见，且 A 的执行顺序排在 B 之前。

重要的 happens-before 规则如下：

1. 程序顺序规则：一个线程中的每个操作，happens- before 于该线程中的任意后续操作。
2. 监视器锁规则：对一个监视器锁的解锁，happens- before 于随后对这个监视器锁的加锁。
3. volatile 变量规则：对一个 volatile 域的写，happens- before 于任意后续对这个 volatile 域的读。
4. 传递性：如果 A happens- before B，且 B happens- before C，那么 A happens- before C。

下图是 happens-before 与 JMM 的关系

![图来自简书用户 你听___](https://tva1.sinaimg.cn/large/008i3skNgy1grnmkp9r6xj30m40ha75b.jpg)

