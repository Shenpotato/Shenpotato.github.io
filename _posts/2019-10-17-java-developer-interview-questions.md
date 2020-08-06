---
layout: post
title:  "java面试常见208个问题"
tags: Java  
author: Shenpotato
catalog: true
---



> java开发工程师面试常见的208道题汇总



![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86s8oellfj30f00jst9k.jpg)



## **1. Java 基础**

1. #### JDK 和 JRE 有什么区别？

   - JDK：Java Development Kit 的简称，Java 开发工具包，提供了 Java 的开发环境和运行环境。
   - JRE：Java Runtime Environment 的简称，Java 运行环境，为 Java 的运行提供了所需环境。

   具体来说 JDK 其实包含了 JRE，同时还包含了编译 Java 源码的编译器 Javac，还包含了很多 Java 程序调试和分析的工具。简单来说：如果你需要运行 Java 程序，只需安装 JRE 就可以了，如果你需要编写 Java 程序，需要安装 JDK。

   

2. #### == 和 equals 的区别是什么？

   **== 解读**

   对于基本类型和引用类型 == 的作用效果是不同的，如下所示：

   - 基本类型：比较的是值是否相同；
   - 引用类型：比较的是引用是否相同；

   代码示例：

   ```java
   String x = "string";
   String y = "string";
   String z = new String("string");
   System.out.println(x==y); // true
   System.out.println(x==z); // false
   System.out.println(x.equals(y)); // true
   System.out.println(x.equals(z)); // true
   
   ```

   代码解读：因为 x 和 y 指向的是同一个引用，所以 == 也是 true，而 new String()方法则重写开辟了内存空间，所以 == 结果为 false，而 equals 比较的一直是值，所以结果都为 true。

   **equals 解读**

   equals 本质上就是 ==，只不过 String 和 Integer 等重写了 equals 方法，把它变成了值比较。看下面的代码就明白了。

   首先来看默认情况下 equals 比较一个有相同值的对象，代码如下：

   ```java
   class Cat {
       public Cat(String name) {
           this.name = name;
       }
   
       private String name;
   
       public String getName() {
           return name;
       }
   
       public void setName(String name) {
           this.name = name;
       }
   }
   
   Cat c1 = new Cat("王磊");
   Cat c2 = new Cat("王磊");
   System.out.println(c1.equals(c2)); // false
   
   ```

   输出结果出乎我们的意料，竟然是 false？这是怎么回事，看了 equals 源码就知道了，源码如下：

   ```java
   public boolean equals(Object obj) {
           return (this == obj);
   }
   
   ```

   原来 equals 本质上就是 ==。

   那问题来了，两个相同值的 String 对象，为什么返回的是 true？代码如下：

   ```java
   String s1 = new String("老王");
   String s2 = new String("老王");
   System.out.println(s1.equals(s2)); // true
   
   ```

   同样的，当我们进入 String 的 equals 方法，找到了答案，代码如下：

   ```java
   public boolean equals(Object anObject) {
       if (this == anObject) {
           return true;
       }
       if (anObject instanceof String) {
           String anotherString = (String)anObject;
           int n = value.length;
           if (n == anotherString.value.length) {
               char v1[] = value;
               char v2[] = anotherString.value;
               int i = 0;
               while (n-- != 0) {
                   if (v1[i] != v2[i])
                       return false;
                   i++;
               }
               return true;
           }
       }
       return false;
   }
   ```

   原来是 String 重写了 Object 的 equals 方法，把引用比较改成了值比较。

   **总结** ：== 对于基本类型来说是值比较，对于引用类型来说是比较的是引用；而 equals 默认情况下是引用比较，只是很多类重新了 equals 方法，比如 String、Integer 等把它变成了值比较，所以一般情况下 equals 比较的是值是否相等。

   

3. #### 两个对象的 hashCode() 相同，则 equals() 也一定为 true，对吗？

   不对，两个对象的 hashCode() 相同，equals() 不一定 true。

   代码示例：

   ```java
   String str1 = "通话";
   String str2 = "重地";
   System. out. println(String. format("str1：%d | str2：%d",  str1. hashCode(),str2. hashCode()));
   System.out.println(str1. equals(str2));
   
   ```

   执行的结果：

   ```java
   str1：1179395 | str2：1179395
   
   false
   
   ```

   代码解读：很显然“通话”和“重地”的 hashCode() 相同，然而 equals() 则为 false，因为在散列表中，hashCode() 相等即两个键值对的哈希值相等，然而哈希值相等，并不一定能得出键值对相等。

   

4. #### final 在 java 中有什么作用？

   - final 修饰的类叫最终类，该类不能被继承。

   - final 修饰的方法不能被重写。

   - final 修饰的变量叫常量，常量必须初始化，初始化之后值就不能被修改。

     

5. #### java 中的 Math.round(-1.5) 等于多少？

   为-1。round()可理解为四舍五入，ceil()理解为向上取整，floor()理解为向下取整。

   Math.ceil(-1.5) = -1，Math.floor(-1.5) = -2，Math.round(1.5) = 2。

   

6. #### String 属于基础的数据类型吗？

   String 不属于基础类型，基础类型有 8 种：byte、boolean、char、short、int、float、long、double，而 String 属于具体的类。

   

7. #### java 中操作字符串都有哪些类？它们之间有什么区别？

   String，StringBuffer，StringBulider。

   String 和 StringBuffer、StringBuilder 的区别在于 String 声明的是不可变的对象，每次操作都会生成新的 String 对象，然后将指针指向新的 String 对象。而 StringBuffer、StringBuilder 可以在原有对象的基础上进行操作，所以在经常改变字符串内容的情况下最好不要使用 String。

   StringBuffer 和 StringBuilder 最大的区别在于，StringBuffer 是线程安全的，而 StringBuilder 是非线程安全的，但 StringBuilder 的性能却高于 StringBuffer，所以在单线程环境下推荐使用 StringBuilder，多线程环境下推荐使用 StringBuffer。

   

8. #### String str="i"与 String str=new String(“i”)一样吗？

   String str = "i";首先在方法区中的字符串缓冲区进行判断，是否有该对象，有则直接指向该对象，若无，则在字符串缓冲区中创建该对象。

   String str = new String("i");直接在堆栈中创建改对象，并指向对象。

   一言以蔽之，String str="i"的方式，Java 虚拟机会将其分配到常量池中；而 String str=new String("i") 则会被分到堆内存中。

   

9. #### 如何将字符串反转？

   使用 StringBuilder 或者 stringBuffer 的 reverse() 方法。

   示例代码：

   ```java
   // StringBuffer reverse
   StringBuffer stringBuffer = new StringBuffer();
   stringBuffer.append("abcdefg");
   System.out.println(stringBuffer. reverse()); // gfedcba
   
   ```

   ```java
   //String转StringBuffer：
   StringBuffer sb = new StringBuffer(s);
   StringBuffer sb = new StringBuffer();
   sb.append()
   
   //StringBuffer转String
   String s = New String(sb);
   String s = sb.toString();
   
   
   ```

   

10. #### String 类的常用方法都有那些？

    1. 字符串判断：

       equals()：字符串比较	

       contains()：是否包含某字符	

       isEmpty()：是否为空

       startwith()	endwith()：是否以某字符开始

    2. 字符串获取：

       indexOf()：返回指定字符的索引

       charAt()：返回指定索引处的字符
       subString()：截取字符串某段

    3. 字符串转换：

       getBytes()：返回字符串的 byte 类型数组

       toCharArray()：返回字符数组

       toLowerCase()：将字符串转成小写字母

       toUpperCase()：将字符串转成大写字符

       valueOf()：把任意数据类型转换为字符串

       concat()：字符串拼接

    4. 其余：

       replace()：字符串替换

       trim()：去除字符串两端空白

       length()：返回字符串长度

       compareTo()：比较字符串

    

11. #### 抽象类必须要有抽象方法吗？

    不需要，抽象类不一定非要有抽象方法。但有抽象方法的类必须声明为抽象类。并且抽象类有构造函数。

    示例代码：

    ```java
    abstract class Cat {
        public static void sayHi() {
            System. out. println("hi~");
        }
    }
    
    ```

    上面代码，抽象类并没有抽象方法但完全可以正常运行。

    

12. #### 普通类和抽象类有哪些区别？

    - 普通类不能包含抽象方法，抽象类可以包含抽象方法。

    - 抽象类不能直接实例化，普通类可以直接实例化。

      

13. #### 抽象类能使用 final 修饰吗？

    不能，定义抽象类就是让其他类继承的，如果定义为 final 该类就不能被继承，这样彼此就会产生矛盾，所以 final 不能修饰抽象类，如下图所示，编辑器也会提示错误信息

    

14. #### 接口和抽象类有什么区别？

    ##### 成员区别：

    抽象类的成员变量可以为常量或者变量，有构造方法，成员方法可为抽象或不抽象，访问修饰符不限

    接口的成员变量必为常量，无构造方法，成员方法必为抽象方法，访问修饰符为public

    ##### 设计理念区别：

    抽象类设计为继承extends，“is a”，体现为继承该体系的共性功能

    接口设计为实现implements，“like a” ，体现该继承体系的扩展功能，主要为功能的实现

    

15. #### java 中 IO 流分为几种？

    按照输入输出来分：输入流，输出流

    按照类型来：字节流，字符流

    字节流和字符流的区别是：字节流按 8 位传输以字节为单位输入输出数据，字符流按 16 位传输以字符为单位输入输出数据。

    

16. #### BIO、NIO、AIO 有什么区别？

    - BIO：Block IO 同步阻塞式 IO，就是我们平常使用的传统 IO，它的特点是模式简单使用方便，并发处理能力低。
    - NIO：Non IO 同步非阻塞 IO，是传统 IO 的升级，客户端和服务器端通过 Channel（通道）通讯，实现了多路复用。
    - AIO：Asynchronous IO 是 NIO 的升级，也叫 NIO2，实现了异步非堵塞 IO ，异步 IO 的操作基于事件和回调机制。

17. #### Files的常用方法都有哪些？

    - Files. exists()：检测文件路径是否存在。

    - Files. createFile()：创建文件。

    - Files. createDirectory()：创建文件夹。

    - Files. delete()：删除一个文件或目录。

    - Files. copy()：复制文件。

    - Files. move()：移动文件。

    - Files. size()：查看文件个数。

    - Files. read()：读取文件。

    - Files. write()：写入文件。

      

## **2. 容器**

1. #### java 容器都有哪些？

   Java 容器分为 Collection 和 Map 两大类，其下又有很多子类，如下所示：

   - Collection

   - List

     - ArrayList
     - LinkedList
     - Vector
     - Stack

   - Set

     - HashSet
     - LinkedHashSet
     - TreeSet

   - Map

   - HashMap

     - LinkedHashMap

   - TreeMap

   - ConcurrentHashMap

   - Hashtable

     

2. #### Collection 和 Collections 有什么区别？

   - Collection 是一个集合接口，它提供了对集合对象进行基本操作的通用接口方法，所有集合都是它的子类，比如 List、Set 等。

   - Collections 是一个包装类，包含了很多静态方法，不能被实例化，就像一个工具类，比如提供的排序方法： Collections. sort(list)。

     

3. #### List、Set、Map 之间的区别是什么？

   List、Set、Map 的区别主要体现在两个方面：元素是否有序、是否允许元素重复。

   三者之间的区别，如下表：

   ![区别图](https://images.gitbook.cn/6e7001c0-3be3-11e9-af57-196eefd310b5)

   

4. #### HashMap 和 Hashtable 有什么区别？

   **（1）HashMap：**

   - 线程不安全的，要依靠Collections.synchronized()方法或通过子类CurrentHashMap实现线程安全；
   - 可以有一个为null的键
   - 通过继承AbstactMap，实现Map接口
   - 初始容量为16，负载因子为0.75，扩容时扩大两倍

   **（2）HashTable：**

   - 线程安全
   - 不可以有值为null的键
   - 继承于Dictionnary，实现Map接口
   - 初始容量为11，负载因子为0.75，扩容时扩大两倍+1

   

5. #### 如何决定使用 HashMap 还是 TreeMap？

   当查找多时使用TreeMap，增删改多时用HashMap。

   

6. #### 说一下 HashMap 的实现原理？

   HashMap底层是个类型为Entry的数组，数组的每个元素都是一个链表。Entry通过next属性指向下一个元素。通过put()方法实现元素的添加与修改。

   在调用put()方法时，先对该键进行二次hash计算，得出在数组中的位置。再进行键唯一性判断，若键已存在，则覆盖其值。若键不存在，则将键值对添加到Entry数组中。

   在jdk1.8之后，当链表长度大于8时，将链表转换为红黑树。

   

7. #### 说一下 HashSet 的实现原理？

   HashSet将元素存在Entry类型的key中，底层通过调用HashMap的put()方法进行增改实现。

   

8. #### ArrayList 和 LinkedList 的区别是什么？

   - ArrayList底层通过动态数组实现，查找快，增删慢

   - LinkedList通过双向链表实现，增删快，查找慢

     

9. #### 如何实现数组和 List 之间的转换？

   数组转List：Arrays.aslist()

   List转数组：toArray()

   

10. #### ArrayList 和 Vector 的区别是什么？

    - ArrayList：在创建对象未指定容量时，在第一次添加时设定初始容量为10；扩容扩大1.5倍；线程不安全；速度快

    - ArrayList比Vector快，它因为有同步，不会过载。 

    - ArrayList更加通用，因为我们可以使用Collections工具类轻易地获取同步列表和只读列表。

      Vector：在创建对象时就设定初始容量为10；扩容扩大2倍；线程安全；速度慢

      

11. #### Array 和 ArrayList 有何区别？

    - Array可以容纳基本类型和对象，而ArrayList只能容纳对象。 

    - Array是指定大小的，而ArrayList大小是固定的。 

    - Array没有提供ArrayList那么多功能，比如addAll、removeAll和iterator等

      

12. #### 在 Queue 中 poll()和 remove()有什么区别？

    poll() 和 remove() 都是从队列中取出一个元素，但是 poll() 在获取元素失败的时候会返回空，但是remove() 失败的时候会抛出异常。peek()不删除元素，只是返回最后一个元素的值。

    

13. #### 哪些集合类是线程安全的？

    Vector，Hashtable，StringBuffer，Stack，enumeration

    

14. #### 迭代器 Iterator 是什么？

    迭代器是一种**设计模式**，它是一个对象，它可以遍历并选择序列中的对象，而开发人员不需要了解该序列的底层结构。迭代器通常被称为“轻量级”对象，因为创建它的代价小。

    

15. #### Iterator 怎么使用？有什么特点？

    Java中的Iterator功能比较简单，并且只能单向移动：　

    (1) 使用方法iterator()要求容器返回一个Iterator。第一次调用Iterator的next()方法时，它返回序列的第一个元素。注意：iterator()方法是java.lang.Iterable接口,被Collection继承。

    (2) 使用next()获得序列中的下一个元素。　

    (3) 使用hasNext()检查序列中是否还有元素。　

    (4) 使用remove()将迭代器新返回的元素删除。　

    (5) foreach()方法实现对于每个元素的操作。

    

16. #### Iterator 和 ListIterator 有什么区别？

    - Iterator可用来遍历Set和List集合，但是ListIterator只能用来遍历List。 
    - Iterator对集合只能是前向遍历，ListIterator既可以前向也可以后向。 
    - ListIterator实现了Iterator接口，并包含其他的功能，比如：增加元素，替换元素，获取前一个和后一个元素的索引，等等

    

17. #### 怎么确保一个集合不能被修改？


    - Collections.unmodifiableList(List)
    
    - Collections.unmodifiableMap(Map)
    
    - Collections.unmodifiableSet(Set)




## **3. 多线程**

1. #### 并行和并发有什么区别？

   并行：两个或两个以上的进程在**同一时间点**发生

   并发：两个或两个以上的进程在**同一时间点段内**发生，**宏观看同时发生，微观看是交替发生**

   

2. #### 线程和进程的区别？

   进程：是操作系统进行资源分配的基本单位，切换进程消耗资源大

   线程：是操作cpu进行调度的基本单位，切换线程消耗资源小，因此又称为轻量级进程

   

3. #### 守护线程是什么？

   在后台运行的线程，其目的是为其他线程提供服务，也称为“守护线程"。JVM的垃圾回收线程就是典型的后台线程。当所有的线程都为守护线程时，虚拟机退出。

   

4. #### 创建线程有哪几种方式？

   **（1）继承Thread类创建线程类**

   - 定义Thread类的子类，并重写该类的run方法，该run方法的方法体就代表了线程要完成的任务。因此把run()方法称为执行体。
   - 创建Thread子类的实例，即创建了线程对象。
   - 调用线程对象的start()方法来启动该线程。

   **（2） 通过Runnable接口创建线程类**

   - 定义runnable接口的实现类，并重写该接口的run()方法，该run()方法的方法体同样是该线程的线程执行体。
   - 创建 Runnable实现类的实例，并依此实例作为Thread的target来创建Thread对象，该Thread对象才是真正的线程对象。
   - 调用线程对象的start()方法来启动该线程。

   **（3.1）通过Callable和Future创建线程**

   - 创建Callable接口的实现类，并实现call()方法，该call()方法将作为线程执行体，并且有返回值。

   - 创建Callable实现类的实例，使用FutureTask类来包装Callable对象，该FutureTask对象封装了该Callable对象的call()方法的返回值。

   - 使用FutureTask对象作为Thread对象的target创建并启动新线程。

   - 调用FutureTask对象的get()方法来获得子线程执行结束后的返回值。

     ```java
     FutureTask<Integer> futureTask1 = new FutureTask<Integer>(new MyCallable(0,100));
     FutureTask<Integer> futureTask2 = new FutureTask<Integer>(new MyCallable(1,101));
     Thread t1 = new Thread(futureTask1);
     Thread t2 = new Thread(futureTask2);
     t1.start();
     t2.start();
     Integer f1 = futureTask1.get();
     Integer f2 = futureTask2.get();
     
     ```

   （3.2）通过线程池和Callable创建线程

   ```java
   ExecutorService pool = Executors.newFixedThreadPool(2);
   Future f1 = pool.submit(new MyCallable(0, 100));
   Future f2 = pool.submit(new MyCallable(1, 101));
   pool.shutdown();
   Integer i1 = (Integer) f1.get();
   Integer i2 = (Integer) f2.get();
   
   ```

   

5. #### 说一下 runnable 和 callable 有什么区别？

   （1）Callable规定的方法是call（），Runnable规定的方法是run（）

   （2）call（）方法可抛出异常，而run（）方法是不可以抛出异常的

   （3）Callable的任务执行后可返回值，运行Callable任务可拿到一个Future对象，而Runnable的任务是不能返回值的。

   Future表示异步计算的结果，它提供了检查计算是否完成的方法，以等待计算的完成，并检索计算的结果，通过Future对象可了解任务执行情况，可取消任务的执行，还可获取任务的执行结果。

   

6. #### 线程有哪些状态？

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86s9zayfwj30js0bl3zv.jpg)

   

7. #### sleep() 和 wait() 有什么区别？

   sleep()：方法是线程类（Thread）的静态方法，让调用线程进入睡眠状态，让出执行机会给其他线程，等到休眠时间结束后，线程进入就绪状态和其他线程一起竞争cpu的执行时间。因为sleep() 是static静态的方法，他**不能改变对象的机锁**，当一个synchronized块中调用了sleep() 方法，线程虽然进入休眠，但是对象的机锁没有被释放，其他线程依然无法访问这个对象。必须设定时间。

   wait()：wait()是Object类的方法，当一个线程执行到wait方法时，它就进入到一个和该对象相关的等待池，同时**释放对象的机**锁，使得其他线程能够访问，可以通过notify，notifyAll方法来唤醒等待的线程。可不设定时间。

   

8. #### notify()和 notifyAll()有什么区别？

   - 如果线程调用了对象的 wait()方法，那么线程便会处于该对象的等待池中，等待池中的线程不会去竞争该对象的锁。
   - 当有线程调用了对象的 notifyAll()方法（唤醒所有 wait 线程）或 notify()方法（只随机唤醒一个 wait 线程），被唤醒的的线程便会进入该对象的锁池中，锁池中的线程会去竞争该对象锁。也就是说，调用了notify后只有一个线程会由等待池进入锁池，而notifyAll会将该对象等待池内的所有线程移动到锁池中，等待锁竞争。
   - 优先级高的线程竞争到对象锁的概率大，假若某线程没有竞争到该对象锁，它还会留在锁池中，唯有线程再次调用 wait()方法，它才会重新回到等待池中。而竞争到对象锁的线程则继续往下执行，直到执行完了 synchronized 代码块，它会释放掉该对象锁，这时锁池中的线程会继续竞争该对象锁。

   

9. #### 线程的 run()和 start()有什么区别？

   每个线程都是通过某个特定Thread对象所对应的方法run()来完成其操作的，方法run()称为线程体。通过调用Thread类的start()方法来启动一个线程。

   start()方法来启动一个线程，真正实现了多线程运行。这时无需等待run方法体代码执行完毕，可以直接继续执行下面的代码； 这时此线程是处于就绪状态， 并没有运行。 然后通过此Thread类调用方法run()来完成其运行状态， 这里方法run()称为线程体，它包含了要执行的这个线程的内容， Run方法运行结束， 此线程终止。然后CPU再调度其它线程。

   run()方法是在本线程里的，只是线程里的一个函数,而不是多线程的。 如果直接调用run(),其实就相当于是调用了一个普通函数而已，直接待用run()方法必须等待run()方法执行完毕才能执行下面的代码，所以执行路径还是只有一条，根本就没有线程的特征，所以在多线程执行时要使用start()方法而不是run()方法。

   

10. #### 创建线程池有哪几种方式？

    **（1）newFixedThreadPool(int nThreads)**

    创建一个固定长度的线程池，每当提交一个任务就创建一个线程，直到达到线程池的最大数量，这时线程规模将不再变化，当线程发生未预期的错误而结束时，线程池会补充一个新的线程。

    **（2）newCachedThreadPool()**

    创建一个可缓存的线程池，如果线程池的规模超过了处理需求，将自动回收空闲线程，而当需求增加时，则可以自动添加新线程，线程池的规模不存在任何限制。

    **（3） newSingleThreadExecutor()**

    这是一个单线程的Executor，它创建单个工作线程来执行任务，如果这个线程异常结束，会创建一个新的来替代它；它的特点是能确保依照任务在队列中的顺序来串行执行。

    **（4）newScheduledThreadPool(int corePoolSize)**

    创建了一个固定长度的线程池，而且以延迟或定时的方式来执行任务，类似于Timer。

    

11. #### 线程池都有哪些状态？

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86s9pxlitj30sp0baaas.jpg)

    

12. #### 线程池中 submit()和 execute()方法有什么区别？

    - execute和submit都属于线程池的方法，execute只能提交Runnable类型的任务，而submit既能提交Runnable类型任务也能提交Callable类型任务。

    - execute会直接抛出任务执行时的异常，submit会吃掉异常，可通过Future的get方法将任务执行时的异常重新抛出。

    - execute所属顶层接口是Executor,submit所属顶层接口是ExecutorService，实现类ThreadPoolExecutor重写了execute方法,抽象类AbstractExecutorService重写了submit方法。

      

13. #### 在 java 程序中怎么保证多线程的运行安全？

    （1）使用synchronied关键字，可以用于代码块，方法（静态方法，同步锁是当前字节码对象；实例方法，同步锁是实例对象）

    （2）使用volatile 关键字，防止指令重排，被volatile修饰的变量的值，将不会被本地线程缓存，所有对该变量的读写都是直接操作共享内存，从而确保多个线程能正确的处理该变量

    （3）lock锁机制

    （4）使用线程安全的类，比如Vector、HashTable、StringBuffer

    原子性：提供互斥访问，同一时刻只能有一个线程对数据进行操作，（atomic,synchronized）；

    可见性：一个线程对主内存的修改可以及时地被其他线程看到，（synchronized,volatile）；

    有序性：一个线程观察其他线程中的指令执行顺序，由于指令重排序，该观察结果一般杂乱无序，（happens-before原则）

    

14. #### 多线程锁的升级原理是什么？

    在Java中，锁共有4种状态，级别从低到高依次为：**无状态锁，偏向锁，轻量级锁和重量级锁状态**，这几个状态会随着竞争情况逐渐升级。锁可以升级但不能降级。

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sbqww9jj30nq0d5t9v.jpg)

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sbyzgbvj30u10b63zp.jpg)

    **（1）偏向锁：**

    - **产生原因：**在大多时候不需要所竞争，通常是一个线程持续获得某一锁对象。为了降低竞争获取锁的代价，设置了偏向锁。

    - **偏向锁的升级：**当线程1访问代码块并获取锁对象时，会在对象头中记录该线程的ThreadID。由于偏向锁不会自动释放锁，所以在Thread1下次继续访问锁对象时，比较当前线程的ThreadID与存储的ThreadID是否相同。如果一致（还是线程1获取锁对象），则无需使用CAS来加锁、解锁；如果不一致（其他线程，如线程2要竞争锁对象，而偏向锁不会主动释放，因此还是存储的线程1的threadID），那么需要查看Java对象头中记录的线程1是否存活，如果没有存活，那么锁对象被重置为无锁状态，其它线程（线程2）可以竞争将其设置为偏向锁；如果存活，那么立刻查找该线程（线程1）的栈帧信息，如果还是需要继续持有这个锁对象，那么暂停当前线程1，撤销偏向锁，升级为轻量级锁，如果线程1不再使用该锁对象，那么将锁对象状态设为无锁状态，重新偏向新的线程。

    - **偏向锁的取消：**偏向锁是默认开启的，而且开始时间一般是比应用程序启动慢几秒，如果不想有这个延迟，那么可以使用-XX:BiasedLockingStartUpDelay=0；

      如果不想要偏向锁，那么可以通过-XX:-UseBiasedLocking = false来设置；

    **（2）轻量级锁：**

    - **产生原因：**轻量级锁考虑的是竞争锁对象的线程不多，而且线程持有锁的时间也不长的情景。因为阻塞线程需要CPU从用户态转到内核态，代价较大，如果刚刚阻塞不久这个锁就被释放了，那这个代价就有点得不偿失了，因此这个时候就干脆不阻塞这个线程，让它自旋这等待锁释放。

    - **轻量级锁的升级：**线程1获取轻量级锁时会先把锁对象的对象头MarkWord复制一份到线程1的栈帧中创建用于存储锁记录的空间（称为DisplacedMarkWord），然后使用CAS把对象头中的内容替换为线程1存储的锁记录（DisplacedMarkWord）的地址；

      如果在线程1复制对象头的同时（在线程1CAS之前），线程2也准备获取锁，复制了对象头到线程2的锁记录空间中，但是在线程2CAS的时候，发现线程1已经把对象头换了，线程2的CAS失败，那么线程2就尝试使用**自旋锁**来等待线程1释放锁。

      但是如果自旋的时间太长也不行，因为自旋是要消耗CPU的，因此自旋的次数是有限制的，比如10次或者100次，如果自旋次数到了线程1还没有释放锁，或者线程1还在执行，线程2还在自旋等待，这时又有一个线程3过来竞争这个锁对象，那么这个时候轻量级锁就会膨胀为重量级锁。**重量级锁把除了拥有锁的线程都阻塞，防止CPU空转**。

      ***注意：**为了避免无用的自旋，轻量级锁一旦膨胀为重量级锁就不会再降级为轻量级锁了；偏向锁升级为轻量级锁也不能再降级为偏向锁。一句话就是锁可以升级不可以降级，但是偏向锁状态可以被重置为无锁状态。

    **（3）锁粗化：**

    按理来说，同步块的作用范围应该尽可能小，仅在共享数据的实际作用域中才进行同步，这样做的目的是为了使需要同步的操作数量尽可能缩小，缩短阻塞时间，如果存在锁竞争，那么等待锁的线程也能尽快拿到锁。 
    但是加锁解锁也需要消耗资源，如果存在一系列的连续加锁解锁操作，可能会导致不必要的性能损耗。 

    锁粗化就是将多个连续的加锁、解锁操作连接在一起，扩展成一个范围更大的锁，避免频繁的加锁解锁操作。

    **（4）锁消除：**

    Java虚拟机在JIT编译时(可以简单理解为当某段代码即将第一次被执行时进行编译，又称即时编译)，通过对运行上下文的扫描，经过逃逸分析，去除不可能存在共享资源竞争的锁，通过这种方式消除没有必要的锁，可以节省毫无意义的请求锁时间。

    


15. #### 什么是死锁？

    死锁是指两个或两个以上的进程在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。是操作系统层面的一个错误，是进程死锁的简称，最早在 1965 年由 Dijkstra 在研究银行家算法时提出的，它是计算机操作系统乃至整个并发程序设计领域最难处理的问题之一。

    

16. #### 怎么防止死锁？

    https://blog.csdn.net/qq_40949465/article/details/88722600#%C2%A0%E4%BA%8C%E3%80%81%E6%AD%BB%E9%94%81%E7%9A%84%E5%A4%84%E7%90%86%E7%AD%96%E7%95%A5

    死锁的四个必要条件：

    - **互斥条件**：进程对所分配到的资源不允许其他进程进行访问，若其他进程访问该资源，只能等待，直至占有该资源的进程使用完成后释放该资源
    - **请求和保持条件**：进程获得一定的资源之后，又对其他资源发出请求，但是该资源可能被其他进程占有，此事请求阻塞，但又对自己获得的资源保持不放
    - **不可剥夺条件**：是指进程已获得的资源，在未完成使用之前，不可被剥夺，只能在使用完后自己释放
    - **环路等待条件**：是指进程发生死锁后，若干进程之间形成一种头尾相接的循环等待资源关系

    这四个条件是死锁的必要条件，只要系统发生死锁，这些条件必然成立，而只要上述条件之 一不满足，就不会发生死锁。理解了死锁的原因，尤其是产生死锁的四个必要条件，就可以最大可能地避免、预防和解除死锁。

    - **预防死锁**。破坏死锁产生的四个必要条件中的一个或几个
    - **避免死锁**。用某种方法阻止系统进入不安全状态，从而避免死锁（银行家算法）
    - **死锁的检测和解除**。允许死锁的发生，不过操作系统负责检测出死锁的发生，然后采取某种措施解除死锁

    

17. #### ThreadLocal 是什么？有哪些使用场景？

    线程局部变量是局限于线程内部的变量，属于线程自身所有，不在多个线程间共享。Java提供ThreadLocal类来支持线程局部变量，是一种实现线程安全的方式。但是在管理环境下（如 web 服务器）使用线程局部变量的时候要特别小心，在这种情况下，工作线程的生命周期比任何应用变量的生命周期都要长。任何线程局部变量一旦在工作完成后没有释放，Java 应用就存在内存泄露的风险。

    

18. #### 说一下 synchronized 底层实现原理？（重量级锁）

    我们知道对象是存放在堆区中的，对象由三部分组成：对象头，实例变量和填充字节。

    - 对象头主要由Markword和Klass Point(类型指针)组成，其中Klass Point是是对象指向它的类元数据的指针，虚拟机通过这个指针来确定这个对象是哪个类的实例。MarkWord用于存储对象自身的运行时数据。如果对象是数组对象，那么对象头占用3个字宽（Word），如果对象是非数组对象，那么对象头占用2个字宽。（1word = 2 Byte = 16 bit）
    - 实例变量存储是的对象的属性信息，包含父类的属性信息，4字节对齐；
    - 填充字符，因为虚拟机要求对象字节必须是8字节的整数倍，填充字符就是用于凑齐这个整数倍的。

    Synchronized的锁对象的相关信息就存放在对象头的MarkWord中。在64位的jvm中的锁对象信息如下：

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sclvte1j30sz088wfe.jpg)

    - 当synchronized的方法修饰同步代码块时，通过monitorentry标识进入同步代码块，通过monitorexit标识退出。
    - 在修饰同步方法时，由方法调用指令来读取运行时常量池中的ACC_SYNCHRONIZED标志隐式实现的。如果方法表结构（method_info Structure）中的ACC_SYNCHRONIZED标志被设置，那么线程在执行方法前会先去获取对象的monitor对象，如果获取成功则执行方法代码，执行完毕后释放monitor对象，如果monitor对象已经被其它线程获取，那么当前线程被阻塞。

    **标准答案：**

    synchronized可以保证方法或者代码块在运行时，同一时刻只有一个方法可以进入到临界区，同时它还可以保证共享变量的内存可见性。

    Java中每一个对象都可以作为锁，这是synchronized实现同步的基础：

    - 普通同步方法，锁是当前实例对象
    - 静态同步方法，锁是当前类的class对象
    - 同步方法块，锁是括号里面的对象

    

19. #### Volatile的原理？（轻量级锁）

    **（1）保证共享变量对所有线程的可见性：**

    ​	将一个变量声明为volatile，代表这个变量是共享的。如：当开启两个线程时，Thread1修改了变量的值，volatile可以保证在Thread2读取该变量之前，将该变量写入主存中，Thread2通过读取主存获取变量值。

    **（2）禁止指令重排序优化：**

    - 当第二个操作是voaltile写时，无论第一个操作是什么，都不能进行重排序
    - 当地一个操作是volatile读时，不管第二个操作是什么，都不能进行重排序
    - 当第一个操作是volatile写时，第二个操作是volatile读时，不能进行重排序

    同时需要注意的是，volatile对于单个的共享变量的读/写具有原子性，但是像num++这种复合操作，volatile无法保证其原子性。

    

20. #### synchronized 和 volatile 的区别是什么？

    - volatile本质是在告诉jvm当前变量在寄存器（工作内存）中的值是不确定的，需要从主存中读取； synchronized则是锁定当前变量，只有当前线程可以访问该变量，其他线程被阻塞住。

    - volatile仅能使用在变量级别；synchronized则可以使用在变量、方法、和类级别的。

    - volatile仅能实现变量的修改可见性，不能保证原子性；而synchronized则可以保证变量的修改可见性和原子性。

      原子性：如果你了解事务，那这个概念应该好理解。原子性通常指多个操作不存在只执行一部分的情况，如果全部执行完成那没毛病，如果只执行了一部分，那对不起，你得撤销(即事务中的回滚)已经执行的部分。

      可见性：当多个线程访问同一个变量x时，线程1修改了变量x的值，线程1、线程2...线程n能够立即读取到线程1修改后的值。

      有序性：即程序执行时按照代码书写的先后顺序执行。在Java内存模型中，允许编译器和处理器对指令进行重排序，但是重排序过程不会影响到单线程程序的执行，却会影响到多线程并发执行的正确性。(本文不对指令重排作介绍，但不代表它不重要，它是理解JAVA并发原理时非常重要的一个概念)。

    - volatile不会造成线程的阻塞；synchronized可能会造成线程的阻塞。

    - volatile标记的变量不会被编译器优化；synchronized标记的变量可以被编译器优化。

    

21. #### synchronized 和 Lock 有什么区别？

    - synchronized是java内置关键字，在jvm层面；Lock是个java类。
    - synchronized无法判断是否获取锁的状态；Lock可以判断是否获取到锁。
    - synchronized会自动释放锁(a 线程执行完同步代码会释放锁 ；b 线程执行过程中发生异常会释放锁)；Lock需在finally中手工释放锁（unlock()方法释放锁），否则容易造成线程死锁。
    - synchronized会自动释放锁(a 线程执行完同步代码会释放锁 ；b 线程执行过程中发生异常会释放锁)；Lock需在finally中手工释放锁（unlock()方法释放锁），否则容易造成线程死锁；
    - 用synchronized关键字的两个线程1和线程2，如果当前线程1获得锁，线程2线程等待。如果线程1阻塞，线程2则会一直等待下去，而Lock锁就不一定会等待下去，如果尝试获取不到锁，线程可以不用一直等待就结束了。
    - synchronized的锁可重入、不可中断、非公平；Lock锁可重入、可判断、可公平（两者皆可）。
    - Lock锁适合大量同步的代码的同步问题，synchronized锁适合代码少量的同步问题。

    

22. ####  ReentrantLock实现原理？

    https://blog.csdn.net/u011212394/article/details/82314489

    ReentrantLock内部封装了sync，继承于AQS(AbstractQueueSynchronizer)，实现公平锁和非公平锁。

    **（1）AQS内部：**

    同步器依赖内部的同步队列（一个FIFO双向队列）来完成同步状态的管理，当前线程获取同步状态失败时，同步器会将当前线程以及等待状态等信息构造成为一个节点（Node）并将其加入同步队列，同时会阻塞当前线程，当同步状态释放时，会把首节点中的线程唤醒，使其再次尝试获取同步状态。

23. #### synchronized 和 ReentrantLock 区别是什么？

    （1）synchronized是和if、else、for、while一样的关键字，ReentrantLock是类，这是二者的本质区别。

    （2）ReentrantLock是类，那么它就提供了比synchronized更多更灵活的特性，可以被继承、可以有方法、可以有各种各样的类变量，ReentrantLock比synchronized的扩展性体现在几点上：

    - ReentrantLock可以对获取锁的等待时间进行设置，这样就避免了死锁 
    - ReentrantLock可以获取各种锁的信息
    - ReentrantLock可以灵活地实现多路通知  

    （3）二者的锁机制其实也是不一样的:ReentrantLock底层调用的是Unsafe的park方法加锁，synchronized操作的应该是对象头中mark word。

    

24. #### 说一下 atomic 的原理？

    Atomic包中的类基本的特性就是在多线程环境下，当有**多个线程同时对单个（包括基本类型及引用类型）变量进行操作**时，具有排他性，即当多个线程同时对该变量的值进行更新时，**仅有一个线程能成功**，而**未成功的线程可以向自旋锁一样，继续尝试**，一直等到执行成功。

    Atomic系列的类中的核心方法都会调用unsafe类中的几个本地方法。我们需要先知道一个东西就是Unsafe类，全名为：sun.misc.Unsafe，这个类包含了大量的对C代码的操作，包括很多直接内存分配以及原子操作的调用，而它之所以标记为非安全的，是告诉你这个里面大量的方法调用都会存在安全隐患，需要小心使用，否则会导致严重的后果，例如在通过unsafe分配内存的时候，如果自己指定某些区域可能会导致一些类似C++一样的指针越界到其他进程的问题。

    

25. #### 什么是CAS?

    #### CAS,compare and swap的缩写，中文翻译成比较并交换**。

    在JDK 5之前Java语言是靠synchronized关键字保证同步的，这会导致有锁

    锁机制存在以下问题：

    （1）在多线程竞争下，加锁、释放锁会导致比较多的上下文切换和调度延时，引起性能问题。

    （2）一个线程持有锁会导致其它所有需要此锁的线程挂起。

    （3）如果一个优先级高的线程等待一个优先级低的线程释放锁会导致优先级倒置，引起性能风险。

    volatile是不错的机制，但是volatile不能保证原子性。因此对于同步最终还是要回到锁机制上来。

    独占锁是一种悲观锁，synchronized就是一种独占锁，会导致其它所有需要锁的线程挂起，等待持有锁的线程释放锁。而另一个更加有效的锁就是乐观锁。所谓乐观锁就是，**每次不加锁而是假设没有冲突而去完成某项操作，如果因为冲突失败就重试，直到成功为止**。乐观锁用到的机制就是CAS，Compare and Swap。

    CAS 操作包含三个操作数 —— 内存位置（V）、预期原值（A）和新值(B)。 如果内存位置的值与预期原值相匹配，那么处理器会自动将该位置值更新为新值 。否则，处理器不做任何操作。无论哪种情况，它都会在 CAS 指令之前返回该位置的值。（在 CAS 的一些特殊情况下将仅返回 CAS 是否成功，而不提取当前值。）CAS 有效地说明了“我认为位置 V 应该包含值 A；如果包含该值，则将 B 放到这个位置；否则，不要更改该位置，只告诉我这个位置现在的值即可。”

    通常将 CAS 用于同步的方式是从地址 V 读取值 A，执行多步计算来获得新值 B，然后使用 CAS 将 V 的值从 A 改为 B。如果 V 处的值尚未同时更改，则 CAS 操作成功。

    类似于 CAS 的指令允许算法执行读-修改-写操作，而无需害怕其他线程同时修改变量，因为如果其他线程修改变量，那么 CAS 会检测它（并失败），算法 可以对该操作重新计算。

    



## **4. 反射**

1. #### 什么是反射？

   反射主要是指程序可以访问、检测和修改它本身状态或行为的一种能力，在运行时期，动态的获取一个类中的成员信息。Java反射机制主要提供了以下功能：

   - 在运行时判断任意一个对象所属的类。
   - 在运行时构造任意一个类的对象。
   - 在运行时判断任意一个类所具有的成员变量和方法。
   - 在运行时调用任意一个对象的方法。

   

2. #### 什么是 java 序列化？什么情况下需要序列化？

   就是把java对象变为二进制对象，便于存储和在网络上传输。简单说就是为了保存在内存中的各种对象的状态（也就是实例变量，不是方法），并且可以把保存的对象状态再读出来。虽然你可以用你自己的各种各样的方法来保存object states，但是Java给你提供一种应该比你自己好的保存对象状态的机制，那就是序列化。

   什么情况下需要序列化：

   - 当你想把的内存中的对象状态保存到一个文件中或者数据库中时候；
   - 当你想用套接字在网络上传送对象的时候；
   - 当你想通过RMI传输对象的时候；

   

3. #### 动态代理是什么？有哪些应用？

   动态代理：

   当想要给实现了某个接口的类中的方法，加一些额外的处理。比如说加日志，加事务等。可以给这个类创建一个代理，故名思议就是创建一个新的类，这个类不仅包含原来类方法的功能，而且还在原来的基础上添加了额外处理的新类。这个代理类并不是定义好的，是动态生成的。具有解耦意义，灵活，扩展性强。

   应用：SpringAop，加事务，加权限，加日志

   

4. #### 怎么实现动态代理？

   - 存在一个接口以及其实现类

   - 创建一个继承于InvocationHandle的类MyInvocationHandle，传入的参数为需要代理的类，并重写其中的invoke()方法，实现需要完成的操作。

   - 用被代理类的对象接収调用Proxys.newInstance()方法生成的对象，MyInvocationHandle作为参数传入其中。

     

   

## **5. 对象拷贝**

1. #### 为什么要使用克隆？

   想对一个对象进行处理，又想保留原有的数据进行接下来的操作，就需要克隆了，Java语言中克隆针对的是类的实例。

2. 如何实现对象克隆？

   有两种方式：

   （1）实现Cloneable接口并重写Object类中的clone()方法；

   （2）实现Serializable接口，通过对象的序列化和反序列化实现克隆，可以实现真正的深度克隆，代码如下：

   import java.io.ByteArrayInputStream;
   import java.io.ByteArrayOutputStream;
   import java.io.ObjectInputStream;
   import java.io.ObjectOutputStream;
   import java.io.Serializable;
   public class MyUtil {

   ```java
   import java.io.ByteArrayInputStream;
   import java.io.ByteArrayOutputStream;
   import java.io.ObjectInputStream;
   import java.io.ObjectOutputStream;
   import java.io.Serializable;
   public class MyUtil {
       private MyUtil() {
           throw new AssertionError();
       }
       @SuppressWarnings("unchecked")
       public static <T extends Serializable> T clone(T obj) throws Exception {
           ByteArrayOutputStream bout = new ByteArrayOutputStream();
           ObjectOutputStream oos = new ObjectOutputStream(bout);
           oos.writeObject(obj);
           ByteArrayInputStream bin = new ByteArrayInputStream(bout.toByteArray());
           ObjectInputStream ois = new ObjectInputStream(bin);
           return (T) ois.readObject();
           // 说明：调用ByteArrayInputStream或ByteArrayOutputStream对象的close方法没有任何意义
           // 这两个基于内存的流只要垃圾回收器清理对象就能够释放资源，这一点不同于对外部资源（如文件流）的释放
       }
   }
   
   ```

   **注意：**基于序列化和反序列化实现的克隆不仅仅是深度克隆，更重要的是通过泛型限定，可以检查出要克隆的对象是否支持序列化，这项检查是编译器完成的，不是在运行时抛出异常，这种是方案明显优于使用Object类的clone方法克隆对象。让问题在编译的时候暴露出来总是好过把问题留到运行时。

   

3. #### 深拷贝和浅拷贝区别是什么？

   浅拷贝只是复制了对象的引用地址，两个对象指向同一个内存地址，所以修改其中任意的值，另一个值都会随之变化，这就是浅拷贝（例：assign()）

   深拷贝是将对象及值复制过来，两个对象修改其中任意的值另一个值不会改变，这就是深拷贝（例：JSON.parse()和JSON.stringify()，但是此方法无法复制函数类型）

   

## **6. Java Web**

1. #### jsp 和 servlet 有什么区别？

   - jsp经编译后就变成了Servlet.（JSP的本质就是Servlet，JVM只能识别java的类，不能识别JSP的代码，Web容器将JSP的代码编译成JVM能够识别的java类）
   - jsp更擅长表现于页面显示，servlet更擅长于逻辑控制。
   - Servlet中没有内置对象，Jsp中的内置对象都是必须通过HttpServletRequest对象，HttpServletResponse对象以及HttpServlet对象得到。
   - Jsp是Servlet的一种简化，使用Jsp只需要完成程序员需要输出到客户端的内容，Jsp中的Java脚本如何镶嵌到一个类中，由Jsp容器完成。而Servlet则是个完整的Java类，这个类的Service方法用于生成对客户端的响应。

   

2. ####  jsp 有哪些内置对象？作用分别是什么？

   JSP有9个内置对象：

   - request：封装客户端的请求，其中包含来自GET或POST请求的参数；
   - response：封装服务器对客户端的响应；
   - pageContext：通过该对象可以获取其他对象；
   - session：封装用户会话的对象；
   - application：封装服务器运行环境的对象；
   - out：输出服务器响应的输出流对象；
   - config：Web应用的配置对象；
   - page：JSP页面本身（相当于Java程序中的this）；
   - exception：封装页面抛出异常的对象。

   

3. #### 说一下 jsp 的 4 种作用域？

   JSP中的四种作用域包括page、request、session和application，具体来说：

   - page代表与一个页面相关的对象和属性。
   - request代表与Web客户机发出的一个请求相关的对象和属性。一个请求可能跨越多个页面，涉及多个Web组件；需要在页面显示的临时数据可以置于此作用域。
   - session代表与某个用户与服务器建立的一次会话相关的对象和属性。跟某个用户相关的数据应该放在用户自己的session中。
   - application代表与整个Web应用程序相关的对象和属性，它实质上是跨越整个Web应用程序，包括多个页面、请求和会话的一个全局作用域。

   

4. #### Servlet的生命周期

   - 实例化

   - init()：初始化，只初始化一次，读取web.xml中的信息

   - service()：解析客户端请求—》执行业务逻辑—》返回结果

   - destroy()：释放资源

     

5. #### session 和 cookie 有什么区别？

   **session：**是服务端技术，基于cookie实现的。每一个用户都会在服务端创建一个session，然后生成JSEESIONID以cookie形式返回给浏览器

   **cookie：**是客户端技术，服务端把每个用户的数据以cookie形式返回给浏览器，当用户再次访问就带着cookie来访问

   - **由于HTTP协议是无状态的协议**，所以**服务端需要记录用户的状态时**，就需要用某种机制来识具体的用户，这个机制就是**Session**。典型的场景比如购物车，当你点击下单按钮时，由于HTTP协议无状态，所以并不知道是哪个用户操作的，所以服务端要为特定的用户创建了特定的Session，用用于标识这个用户，并且跟踪用户，这样才知道购物车里面有几本书。这个Session是保存在服务端的，有一个唯一标识。在服务端保存Session的方法很多，内存、数据库、文件都有。集群的时候也要考虑Session的转移，在大型的网站，一般会有专门的Session服务器集群，用来保存用户会话，这个时候 Session 信息都是放在内存的，使用一些缓存服务比如Memcached之类的来放 Session。
   - **服务端使用cookie识别特定的用户**。每次HTTP请求的时候，客户端都会发送相应的Cookie信息到服务端。实际上大多数的应用都是用 Cookie 来实现Session跟踪的。第一次创建Session的时候，服务端会在HTTP协议中告诉客户端，需要在 Cookie 里面记录一个Session ID，以后每次请求把这个会话ID发送到服务器，我就知道你是谁了。有人问，如果客户端的浏览器禁用了 Cookie 怎么办？一般这种情况下，会使用一种叫做**URL重写的技术来进行会话跟踪**，即每次HTTP交互，URL后面都会被附加上一个诸如 sid=xxxxx 这样的参数，服务端据此来识别用户。
   - Cookie其实还可以用在一些方便用户的场景下，设想你某次登陆过一个网站，下次登录的时候不想再次输入账号了，怎么办？这个信息可以写到Cookie里面，访问网站的时候，网站页面的脚本可以读取这个信息，就自动帮你把用户名给填了，能够方便一下用户。这也是Cookie名称的由来，给用户的一点甜头。所以，总结一下：**Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式**

   

6. #### 说一下 session 的工作原理？

   获取用户传输到服务端的数据封装称session对象，然后生成JSESSIONID以cookie的形式返回给浏览器，就是图中Set-Cookie

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sdg7bj2j30hn06umxu.jpg)

   其实session是一个存在服务器上的类似于一个散列表格的文件。里面存有我们需要的信息，在我们需要用的时候可以从里面取出来。类似于一个大号的map吧，里面的键存储的是用户的sessionid，用户向服务器发送请求的时候会带上这个sessionid。这时就可以从中取出对应的值了。

   

7. #### 如果客户端禁止 cookie 能实现 session 还能用吗？

   Cookie与 Session，一般认为是两个独立的东西，Session采用的是在服务器端保持状态的方案，而Cookie采用的是在客户端保持状态的方案。但为什么禁用Cookie就不能得到Session呢？因为Session是用Session ID来确定当前对话所对应的服务器Session，而Session ID是通过Cookie来传递的，禁用Cookie相当于失去了Session ID，也就得不到Session了。

   假定用户关闭Cookie的情况下使用Session，其实现途径有以下几种：

   - 设置php.ini配置文件中的“session.use_trans_sid = 1”，或者编译时打开打开了“--enable-trans-sid”选项，让PHP自动跨页传递Session ID。
   - 手动通过URL传值、隐藏表单传递Session ID。
   - 用文件、数据库等形式保存Session ID，在跨页过程中手动调用。

   

8. #### spring mvc 和 struts 的区别是什么？

   **（1）拦截机制的不同**
   Struts2是类级别的拦截，每次请求就会创建一个Action，和Spring整合时Struts2的ActionBean注入作用域是原型模式prototype，然后通过setter，getter吧request数据注入到属性。Struts2中，一个Action对应一个request，response上下文，在接收参数时，可以通过属性接收，这说明属性参数是让多个方法共享的。Struts2中Action的一个方法可以对应一个url，而其类属性却被所有方法共享，这也就无法用注解或其他方式标识其所属方法了，只能设计为多例。

   SpringMVC是方法级别的拦截，一个方法对应一个Request上下文，所以方法直接基本上是独立的，独享request，response数据。而每个方法同时又何一个url对应，参数的传递是直接注入到方法中的，是方法所独有的。处理结果通过ModeMap返回给框架。在Spring整合时，SpringMVC的Controller Bean默认单例模式Singleton，所以默认对所有的请求，只会创建一个Controller，有应为没有共享的属性，所以是线程安全的，如果要改变默认的作用域，需要添加@Scope注解修改。

   Struts2有自己的拦截Interceptor机制，SpringMVC这是用的是独立的Aop方式，这样导致Struts2的配置文件量还是比SpringMVC大。

   **（2）底层框架的不同**　
   Struts2采用Filter（StrutsPrepareAndExecuteFilter）实现，SpringMVC（DispatcherServlet）则采用Servlet实现。Filter在容器启动之后即初始化；服务停止以后坠毁，晚于Servlet。Servlet在是在调用时初始化，先于Filter调用，服务停止后销毁

   **（3）性能方面**
   Struts2是类级别的拦截，每次请求对应实例一个新的Action，需要加载所有的属性值注入，SpringMVC实现了零配置，由于SpringMVC基于方法的拦截，有加载一次单例模式bean注入。所以，SpringMVC开发效率和性能高于Struts2。

   **（4）配置方面**

   spring MVC和Spring是无缝的。从这个项目的管理和安全上也比Struts2高。

   

9. #### 如何避免 sql 注入？

   - PreparedStatement（简单又有效的方法）

   - 使用正则表达式过滤传入的参数

   - 字符串过滤

   - JSP中调用该函数检查是否包函非法字符

   - JSP页面判断代码

     

10. #### 什么是 XSS 攻击，如何避免？

    XSS攻击又称CSS,全称Cross Site Script  （跨站脚本攻击），其原理是攻击者向有XSS漏洞的网站中输入恶意的 HTML 代码，当用户浏览该网站时，这段 HTML 代码会自动执行，从而达到攻击的目的。XSS 攻击类似于 SQL 注入攻击，SQL注入攻击中以SQL语句作为用户输入，从而达到查询/修改/删除数据的目的，而在xss攻击中，通过插入恶意脚本，实现对用户游览器的控制，获取用户的一些信息。 XSS是 Web 程序中常见的漏洞，XSS 属于被动式且用于客户端的攻击方式。

    XSS防范的总体思路是：对输入(和URL参数)进行过滤，对输出进行编码。

    

11. #### 什么是 CSRF 攻击，如何避免？

    CSRF（Cross-site request forgery）也被称为 one-click attack或者 session riding，中文全称是叫跨站请求伪造。一般来说，攻击者通过伪造用户的浏览器的请求，向访问一个用户自己曾经认证访问过的网站发送出去，使目标网站接收并误以为是用户的真实操作而去执行命令。常用于盗取账号、转账、发送虚假消息等。攻击者利用网站对请求的验证漏洞而实现这样的攻击行为，网站能够确认请求来源于用户的浏览器，却不能验证请求是否源于用户的真实意愿下的操作行为。

    **如何避免：**

    **（1）验证 HTTP Referer 字段**

    HTTP头中的Referer字段记录了该 HTTP 请求的来源地址。在通常情况下，访问一个安全受限页面的请求来自于同一个网站，而如果黑客要对其实施 CSRF攻击，他一般只能在他自己的网站构造请求。因此，可以通过验证Referer值来防御CSRF 攻击。

    **（2）使用验证码**
    关键操作页面加上验证码，后台收到请求后通过判断验证码可以防御CSRF。但这种方法对用户不太友好。

    **（3）在请求地址中添加token并验证**
    CSRF 攻击之所以能够成功，是因为黑客可以完全伪造用户的请求，该请求中所有的用户验证信息都是存在于cookie中，因此黑客可以在不知道这些验证信息的情况下直接利用用户自己的cookie 来通过安全验证。要抵御 CSRF，关键在于在请求中放入黑客所不能伪造的信息，并且该信息不存在于 cookie 之中。可以在 HTTP 请求中以参数的形式加入一个随机产生的 token，并在服务器端建立一个拦截器来验证这个 token，如果请求中没有token或者 token 内容不正确，则认为可能是 CSRF 攻击而拒绝该请求。这种方法要比检查 Referer 要安全一些，token 可以在用户登陆后产生并放于session之中，然后在每次请求时把token 从 session 中拿出，与请求中的 token 进行比对，但这种方法的难点在于如何把 token 以参数的形式加入请求。
    对于 GET 请求，token 将附在请求地址之后，这样 URL 就变成 http://url?csrftoken=tokenvalue。
    而对于 POST 请求来说，要在 form 的最后加上 <input type="hidden" name="csrftoken" value="tokenvalue"/>，这样就把token以参数的形式加入请求了。

    **（4）在HTTP 头中自定义属性并验证**
    这种方法也是使用 token 并进行验证，和上一种方法不同的是，这里并不是把 token 以参数的形式置于 HTTP 请求之中，而是把它放到 HTTP 头中自定义的属性里。通过 XMLHttpRequest 这个类，可以一次性给所有该类请求加上 csrftoken 这个 HTTP 头属性，并把 token 值放入其中。这样解决了上种方法在请求中加入 token 的不便，同时，通过 XMLHttpRequest 请求的地址不会被记录到浏览器的地址栏，也不用担心 token 会透过 Referer 泄露到其他网站中去。

    

## **7. 异常**

1. #### throw 和 throws 的区别？

   throw：是手动抛出异常，只能抛出一个异常：throw new MyException();

   throws：是用于类上来抛出异常，表示不处理当前异常：Class  A  throws Exception

   

2. #### final、finally、finalize 有什么区别？

   - final可以修饰类、变量、方法，修饰类表示该类不能被继承、修饰方法表示该方法不能被重写、修饰变量表示该变量是一个常量不能被重新赋值。

   - finally一般作用在try-catch代码块中，在处理异常的时候，通常我们将一定要执行的代码方法finally代码块中，表示不管是否出现异常，该代码块都会执行，一般用来存放一些关闭资源的代码。

   - finalize是一个方法，属于Object类的一个方法，而Object类是所有类的父类，该方法一般由垃圾回收器来调用，当我们调用System的gc()方法的时候，由垃圾回收器调用finalize(),回收垃圾。 

     

3. #### try-catch-finally 中哪个部分可以省略？

   catch 可以省略

   **原因：**

   更为严格的说法其实是：try只适合处理运行时异常，try+catch适合处理运行时异常+普通异常。也就是说，如果你只用try去处理普通异常却不加以catch处理，编译是通不过的，因为编译器硬性规定，普通异常如果选择捕获，则必须用catch显示声明以便进一步处理。而运行时异常在编译时没有如此规定，所以catch可以省略，你加上catch编译器也觉得无可厚非。


   理论上，编译器看任何代码都不顺眼，都觉得可能有潜在的问题，所以你即使对所有代码加上try，代码在运行期时也只不过是在正常运行的基础上加一层皮。但是你一旦对一段代码加上try，就等于显示地承诺编译器，对这段代码可能抛出的异常进行捕获而非向上抛出处理。如果是普通异常，编译器要求必须用catch捕获以便进一步处理；如果运行时异常，捕获然后丢弃并且+finally扫尾处理，或者加上catch捕获以便进一步处理。

   至于加上finally，则是在不管有没捕获异常，都要进行的“扫尾”处理。

   ​

4. #### try-catch-finally 中，如果 catch 中 return 了，finally 还会执行吗？

   会执行，在return之前执行。

   

5. #### 常见的异常类有哪些？

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sdpe7hlj30hj0h1750.jpg)

RuntimeException又称为免检异常，不需要用try-catch包住的异常，是程序员写的代码的逻辑错误。

包括：

          ArithmeticException:算术异常

          NullPointerException:空指针异常

          ArrayIndexOutOfBoundsException:数组索引越界

          StringIndexOutOfBoundsException:String操作中索引越界

         NumberFormatException:数字格式化异常

          ClassCastException:类型强制转换异常

其他的异常都需要try-catch进行包裹，如IOException，SQLException。



## **8. 网络**

1. ####  http 响应码 301 和 302 代表的是什么？有什么区别？

   301，302 都是HTTP状态的编码，都代表着某个URL发生了转移。

   区别：

   301 redirect: 301 代表永久性转移(Permanently Moved)。

   302 redirect: 302 代表暂时性转移(Temporarily Moved )。 

   

2. #### forward 和 redirect 的区别？

   Forward和Redirect代表了两种请求转发方式：直接转发和间接转发。

   直接转发方式（Forward），客户端和浏览器只发出一次请求，Servlet、HTML、JSP或其它信息资源，由第二个信息资源响应该请求，在请求对象request中，保存的对象对于每个信息资源是共享的。

   间接转发方式（Redirect）实际是两次HTTP请求，**服务器端在响应第一次请求的时候，让浏览器再向另外一个URL发出请求**，从而达到转发的目的。

   举个通俗的例子：

   直接转发就相当于：“A找B借钱，B说没有，B去找C借，借到借不到都会把消息传递给A”；　

   间接转发就相当于："A找B借钱，B说没有，让A去找C借"。

   

3. #### 简述 tcp 和 udp的区别？

   - TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接。
   - TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP尽最大努力交付，即不保证可靠交付。
   - Tcp通过校验和，重传控制，序号标识，滑动窗口、确认应答实现可靠传输。如丢包时的重发控制，还可以对次序乱掉的分包进行顺序控制；UDP具有较好的实时性，工作效率比TCP高，适用于对高速传输和实时性有较高的通信或广播通信。
   - 每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信。
   - TCP对系统资源要求较多，UDP对系统资源要求较少

   

4. #### tcp 为什么要三次握手，两次不行吗？为什么？

   为了确定客户端和服务端的收发信能力。两次不行，只能证明客户端的收发信能力。

   **标准答案：**

   为了实现可靠数据传输， TCP 协议的通信双方， 都必须维护一个序列号， 以标识发送出去的数据包中， 哪些是已经被对方收到的。 三次握手的过程即是通信双方相互告知序列号起始值， 并确认对方已经收到了序列号起始值的必经步骤。

   （1）如果只是两次握手， 至多只有连接发起方的起始序列号能被确认， 另一方选择的序列号则得不到确认。

   （2）第三次握手是为了防止失效的连接请求到达服务器，让服务器错误打开连接。

   客户端发送的连接请求如果在网络中滞留，那么就会隔很长一段时间才能收到服务器端发回的连接确认。客户端等待一个超时重传时间之后，就会重新请求连接。但是这个滞留的连接请求最后还是会到达服务器，如果不进行三次握手，那么服务器就会打开两个连接。如果有第三次握手，客户端会忽略服务器之后发送的对滞留连接请求的连接确认，不进行第三次握手，因此就不会再次打开连接。

   

5. #### tcp的四次挥手？

   - A 发送连接释放报文，FIN=1。

   - B 收到之后发出确认，此时 TCP 属于半关闭状态，B 能向 A 发送数据但是 A 不能向 B 发送数据。

   - 当 B 不再需要连接时，发送连接释放报文，FIN=1。

   - A 收到后发出确认，进入 TIME-WAIT 状态，等待 2 MSL（最大报文存活时间）后释放连接。

   - B 收到 A 的确认后释放连接。

     **四次挥手的原因**

     客户端发送了 FIN 连接释放报文之后，服务器收到了这个报文，就进入了 CLOSE-WAIT 状态。这个状态是为了让服务器端发送还未传送完毕的数据，传送完毕之后，服务器会发送 FIN 连接释放报文。

     **TIME_WAIT**

     客户端接收到服务器端的 FIN 报文后进入此状态，此时并不是直接进入 CLOSED 状态，还需要等待一个时间计时器设置的时间 2MSL。这么做有两个理由：

     - 确保最后一个确认报文能够到达。如果 B 没收到 A 发送来的确认报文，那么就会重新发送连接释放请求报文，A 等待一段时间就是为了处理这种情况的发生。

     - 等待一段时间是为了让本连接持续时间内所产生的所有报文都从网络中消失，使得下一个新的连接不会出现旧的连接请求报文。

       

6. #### 说一下 tcp 粘包是怎么产生的？

   **(1)发送方产生粘包**

   采用TCP协议传输数据的客户端与服务器经常是保持一个长连接的状态（一次连接发一次数据不存在粘包），双方在连接不断开的情况下，可以一直传输数据；但当发送的数据包过于的小时，那么TCP协议默认的会启用Nagle算法，将这些较小的数据包进行合并发送（缓冲区数据发送是一个堆压的过程）；这个合并过程就是在发送缓冲区中进行的，也就是说数据发送出来它已经是粘包的状态了。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86se70gw8j30n0088t9c.jpg)

   **(2)接收方产生粘包**

   接收方采用TCP协议接收数据时的过程是这样的：数据到底接收方，从网络模型的下方传递至传输层，传输层的TCP协议处理是将其放置接收缓冲区，然后由应用层来主动获取（C语言用recv、read等函数）；这时会出现一个问题，就是我们在程序中调用的读取数据函数不能及时的把缓冲区中的数据拿出来，而下一个数据又到来并有一部分放入的缓冲区末尾，等我们读取数据时就是一个粘包。（放数据的速度 > 应用层拿数据速度） 

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sf43apaj30u00hdabe.jpg)

   

7. #### OSI 的七层模型都有哪些？

   - 应用层：网络服务与最终用户的一个接口。
   - 表示层：数据的表示、安全、压缩。
   - 会话层：建立、管理、终止会话。
   - 传输层：定义传输数据的协议端口号，以及流控和差错校验。
   - 网络层：进行逻辑地址寻址，实现不同网络之间的路径选择。
   - 数据链路层：建立逻辑连接、进行硬件地址寻址、差错校验等功能。
   - 物理层：建立、维护、断开物理连接。

   

8. #### get 和 post 请求有哪些区别？

   - GET在浏览器回退时是无害的，而POST会再次提交请求。
   - GET请求会被浏览器主动cache，而POST不会，除非手动设置。
   - GET请求只能进行url编码，而POST支持多种编码方式。
   - GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。
   - GET请求在URL中传送的参数是有长度限制的，而POST么有。
   - 对参数的数据类型，GET只接受ASCII字符，而POST没有限制。
   - GET比POST更不安全，因为参数直接暴露在URL上，所以不能用来传递敏感信息。
   - GET参数通过URL传递，POST放在Request body中。

   

9. #### 如何实现跨域？

   **（1）JSONP跨域**

   JSONP（JSON with Padding）是数据格式JSON的一种“使用模式”，可以让网页从别的网域要数据。根据 XmlHttpRequest 对象受到同源策略的影响，而利用 <script>元素的这个开放策略，网页可以得到从其他来源动态产生的JSON数据，而这种使用模式就是所谓的 JSONP。用JSONP抓到的数据并不是JSON，而是任意的JavaScript，用 JavaScript解释器运行而不是用JSON解析器解析。所有，通过Chrome查看所有JSONP发送的Get请求都是js类型，而非XHR。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sji078dj30u0068mxr.jpg)

   

   **缺点：**

   - 只能使用Get请求
   - 不能注册success、error等事件监听函数，不能很容易的确定JSONP请求是否失败
   - JSONP是从其他域中加载代码执行，容易受到跨站请求伪造的攻击，其安全性无法确保

   **（2）CORS**

   Cross-Origin Resource Sharing（CORS）跨域资源共享是一份浏览器技术的规范，提供了 Web 服务从不同域传来沙盒脚本的方法，以避开浏览器的同源策略，确保安全的跨域数据传输。现代浏览器使用CORS在API容器如XMLHttpRequest来减少HTTP请求的风险来源。与 JSONP 不同，CORS 除了 GET 要求方法以外也支持其他的 HTTP 要求。服务器一般需要增加如下响应头的一种或几种：

   ```
   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: POST, GET, OPTIONS
   Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
   Access-Control-Max-Age: 86400
   
   ```

   

10. ####  JSONP 实现原理？

    jsonp 即 json+padding，动态创建script标签，利用script标签的src属性可以获取任何域下的js脚本，通过这个特性(也可以说漏洞)，服务器端不在返回json格式，而是返回一段调用某个函数的js代码，在src中进行了调用，这样实现了跨域。

    

## **9. 设计模式**

1. #### 说一下你熟悉的设计模式？

   **（1）创建型：**简单工厂，工厂方法，抽象工厂，建造者，原型，单例

   **（2）结构型：**外观，适配器，代理，装饰，桥接，组合，享元

   **（3）行为型：**模板方法，观察者，状态，职责链，命令，访问者，策略，备忘录，迭代器，解释器

   单例模式：

   ```java
   public class Singleton {
   
       private Singleton() {
       }
   
       //饿汉式
       private static Singleton singleton1 = new Singleton();
   
       public static Singleton createSingleton1() {
           return singleton1;
       }
   
       //线程不安全的懒汉式
       private static Singleton singleton2;
   
       public static Singleton createSingleton2() {
           if (singleton2 == null) {
               singleton2 = new Singleton();
           }
           return singleton2;
       }
   
       //线程安全的懒汉式
       public synchronized static Singleton createSingleton3() {
           if (singleton2 == null) {
               singleton2 = new Singleton();
           }
           return singleton2;
       }
   }
   
   ```

2. ####  简单工厂和抽象工厂有什么区别？

   简单工厂：

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sjqn2nfj30fg05raai.jpg)

   抽象工厂：

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sjtqxzhj30pk0eawgo.jpg)

   

   可以这么说，它和工厂方法模式的区别就在于需要创建对象的复杂程度上。而且抽象工厂模式是三个里面最为抽象、最具一般性的。抽象工厂模式的用意为：给客户端提供一个接口，可以创建多个产品族中的产品对象。

   相比于简单工厂方法，抽象工厂方法将工厂抽象为接口，工厂方法的时间放在具体的子工厂中去实现。这种做法降低了简单工厂方法在代码扩展时频繁修改工厂类的缺点，只需扩展子工厂类进行功能完善。缺点在于代码量较多。



## **10. Spring/Spring MVC**

1. #### 为什么要使用 spring？

   为开源框架，为了解决企业应用开发的复杂性而创建的，是一个轻量级的控制反转（IOC）和面向切面的（AOP）的容器框架

   - 软件系统日趋复杂

   - 重用度高，开发效率和质量提高

   - 软件设计人员要专注对领域的了解，使需求分析更充分

   - 易于上手、快速解决问题

     

2. #### 解释一下什么是 aop？

   AOP（Aspect-Oriented Programming，面向方面编程），可以说是OOP（Object-Oriented Programing，面向对象编程）的补充和完善。

   AOP技术则恰恰相反，它利用一种称为“横切”的技术，剖解开封装的对象内部，并将那些影响了多个类的公共行为封装到一个可重用模块，并将其名为“Aspect”，即方面。所谓“方面”，简单地说，就是将那些与业务无关，却为业务模块所共同调用的逻辑或责任封装起来，便于减少系统的重复代码，降低模块间的耦合度，并有利于未来的可操作性和可维护性。AOP代表的是一个横向的关系，如果说“对象”是一个空心的圆柱体，其中封装的是对象的属性和行为；那么面向方面编程的方法，就仿佛一把利刃，将这些空心圆柱体剖开，以获得其内部的消息。而剖开的切面，也就是所谓的“方面”了。然后它又以巧夺天功的妙手将这些剖开的切面复原，不留痕迹。

   使用“横切”技术，AOP把软件系统分为两个部分：核心关注点和横切关注点。业务处理的主要流程是核心关注点，与之关系不大的部分是横切关注点。横切关注点的一个特点是，他们经常发生在核心关注点的多处，而各处都基本相似。比如权限认证、日志、事务处理。Aop 的作用在于分离系统中的各种关注点，将核心关注点和横切关注点分离开来。正如Avanade公司的高级方案构架师Adam Magee所说，AOP的核心思想就是“将应用程序中的商业逻辑同对其提供支持的通用服务进行分离。”

   

3. #### 解释一下什么是 ioc？

   控制权的转移，应用程序本身不负责依赖对象的创建和维护，而是由外部容器负责创建和维护。 

   思想是反转资源获取的方向。当某个角色需要另外一个角色协助的时候，在传统的程序设计过程中，通常由调用者来创建被调用者的实例。应用IOC后，但在spring中创建被调用者的工作不再由调用者来完成，因此称为控制反转。容器主动地将资源推送给它所管理的组件，组件所要做的仅仅是选择一种合适的方式来接受资源，这种行为也被称为查找的被动形式。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sk0p7gbj30cw08mdg6.jpg)

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sk5znhmj30c90ek0tu.jpg)

   因此也称为依赖注入。 spring以动态灵活的方式来管理对象，注入的两种方式，属性注入（需要空构造方法）和构造注入。 属性注入的优点：直观，自然；构造注入的优点：可以在构造器中决定依赖关系的顺序。

   **理解DI的关键是：“谁依赖谁，为什么需要依赖，谁注入谁，注入了什么”，那我们来深入分析一下：**

   **谁依赖于谁：**当然是应用程序依赖于IoC容器；

   **为什么需要依赖：**应用程序需要IoC容器来提供对象需要的外部资源；

   **谁注入谁：**很明显是IoC容器注入应用程序某个对象，应用程序依赖的对象；

   **注入了什么：**就是注入某个对象所需要的外部资源（包括对象、资源、常量数据）。

   

4. #### spring 有哪些主要模块？

   Spring框架至今已集成了20多个模块。这些模块主要被分如下图所示的核心容器、数据访问/集成,、Web、AOP（面向切面编程）、工具、消息和测试模块

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86skbz2jgj30ja0dkdh0.jpg)

   

5. #### spring 常用的注入方式有哪些？

   - 构造器注入

   - setter方法注入

   - 基于注解的注入

     

6. #### spring 中的 bean 是线程安全的吗？

   Spring容器中的Bean是否线程安全，容器本身并没有提供Bean的线程安全策略，因此可以说spring容器中的Bean本身不具备线程安全的特性，但是具体还是要结合具体scope的Bean去研究。

   

7. #### spring 支持几种 bean 的作用域？

   当通过spring容器创建一个Bean实例时，不仅可以完成Bean实例的实例化，还可以为Bean指定特定的作用域。Spring支持如下5种作用域：

   - singleton：单例模式，在整个Spring IoC容器中，使用singleton定义的Bean将只有一个实例
   - prototype：原型模式，每次通过容器的getBean方法获取prototype定义的Bean时，都将产生一个新的Bean实例
   - request：对于每次HTTP请求，使用request定义的Bean都将产生一个新实例，即每次HTTP请求将会产生不同的Bean实例。只有在Web应用中使用Spring时，该作用域才有效
   - session：对于每次HTTP Session，使用session定义的Bean都将产生一个新实例。同样只有在Web应用中使用Spring时，该作用域才有效
   - globalsession：每个全局的HTTP Session，使用session定义的Bean都将产生一个新实例。典型情况下，仅在使用portlet context的时候有效。同样只有在Web应用中使用Spring时，该作用域才有效

   其中比较常用的是singleton和prototype两种作用域。对于singleton作用域的Bean，每次请求该Bean都将获得相同的实例。容器负责跟踪Bean实例的状态，负责维护Bean实例的生命周期行为；如果一个Bean被设置成prototype作用域，程序每次请求该id的Bean，Spring都会新建一个Bean实例，然后返回给程序。在这种情况下，Spring容器仅仅使用new 关键字创建Bean实例，一旦创建成功，容器不在跟踪实例，也不会维护Bean实例的状态。

   如果不指定Bean的作用域，Spring默认使用singleton作用域。Java在创建Java实例时，需要进行内存申请；销毁实例时，需要完成垃圾回收，这些工作都会导致系统开销的增加。因此，prototype作用域Bean的创建、销毁代价比较大。而singleton作用域的Bean实例一旦创建成功，可以重复使用。因此，除非必要，否则尽量避免将Bean被设置成prototype作用域。

   

8. #### spring 自动装配 bean 有哪些方式？

   Spring容器负责创建应用程序中的bean同时通过ID来协调这些对象之间的关系。作为开发人员，我们需要告诉Spring要创建哪些bean并且如何将其装配到一起。

   spring中bean装配有两种方式：

   - 隐式的bean发现机制和自动装配
   - 在java代码或者XML中进行显示配置

   当然这些方式也可以配合使用。

   

9. #### spring 事务实现方式有哪些？

   （1）编程式事务管理对基于 POJO 的应用来说是唯一选择。我们需要在代码中调用beginTransaction()、commit()、rollback()等事务管理相关的方法，这就是编程式事务管理。

   （2）基于 TransactionProxyFactoryBean 的声明式事务管理

   （3）基于 @Transactional 的声明式事务管理

   （4）基于 Aspectj AOP 配置事务

   

10. #### 说一下 spring 的事务隔离？

    事务隔离级别指的是一个事务对数据的修改与另一个并行的事务的隔离程度，当多个事务同时访问相同数据时，如果没有采取必要的隔离机制，就可能发生以下问题：

    - 脏读：一个事务读到另一个事务未提交的更新数据。
    - 幻读：例如第一个事务对一个表中的数据进行了修改，比如这种修改涉及到表中的“全部数据行”。同时，第二个事务也修改这个表中的数据，这种修改是向表中插入“一行新数据”。那么，以后就会发生操作第一个事务的用户发现表中还存在没有修改的数据行，就好象发生了幻觉一样。
    - 不可重复读：比方说在同一个事务中先后执行两条一模一样的select语句，期间在此次事务中没有执行过任何DDL语句，但先后得到的结果不一致，这就是不可重复读。

    因此，针对上述可能发生的问题，我们设置了以下事务隔离级别：

    - ISOLOCATION_DEFAULT:  数据库默认级别

    - ISOLOCATION_READ_UNCOMMITTED: 允许读取未提交的读， 可能导致脏读，不可重复读，幻读

    - ISOLOCATION_READ_COMMITTED:  允许读取已提交的读，可能导致不可重复读，幻读

    - ISOLOCATION_REPEATABLE_READ : 不能读取另一个事务修改表单的尚未提交(回滚)的数据，可能引起幻读

    - ISOLOCATION_SERIALIZABLE: 序列执行效率低

      



11. #### 说一下 spring mvc 运行流程？

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86skmb84oj30rs0h8wfm.jpg)

    （1）用户向服务器发送请求，请求被Spring 前端控制Servelt DispatcherServlet捕获；

    （2）DispatcherServlet对请求URL进行解析，得到请求资源标识符（URI）。然后根据该URI，调用HandlerMapping获得该Handler配置的所有相关的对象（包括Handler对象以及Handler对象对应的拦截器），最后以HandlerExecutionChain对象的形式返回； 

    （3）DispatcherServlet 根据获得的Handler，选择一个合适的HandlerAdapter；（附注：如果成功获得HandlerAdapter后，此时将开始执行拦截器的preHandler(...)方法）

    （4）提取Request中的模型数据，填充Handler入参，开始执行Handler（Controller)。 在填充Handler的入参过程中，根据你的配置，Spring将帮你做一些额外的工作：

    - HttpMessageConveter： 将请求消息（如Json、xml等数据）转换成一个对象，将对象转换为指定的响应信息
    - 数据转换：对请求消息进行数据转换。如String转换成Integer、Double等
    - 数据根式化：对请求消息进行数据格式化。 如将字符串转换成格式化数字或格式化日期等
    - 数据验证： 验证数据的有效性（长度、格式等），验证结果存储到BindingResult或Error中

    （5）Handler执行完成后，向DispatcherServlet 返回一个ModelAndView对象；

    （6）根据返回的ModelAndView，选择一个适合的ViewResolver（必须是已经注册到Spring容器中的ViewResolver)返回给DispatcherServlet ；

    （7）ViewResolver 结合Model和View，来渲染视图；

    （8）将渲染结果返回给客户端。

    

12. #### spring mvc 有哪些组件？

    - DispatcherServlet：中央控制器，把请求给转发到具体的控制类

    - Controller：具体处理请求的控制器

    - HandlerMapping：映射处理器，负责映射中央处理器转发给controller时的映射策略

    - ModelAndView：服务层返回的数据和视图层的封装类

    - ViewResolver：视图解析器，解析具体的视图

    - Interceptors ：拦截器，负责拦截我们定义的请求然后做处理工作

      

13. ####  @RequestMapping 的作用是什么？

    RequestMapping是一个用来处理请求地址映射的注解，可用于类或方法上。用于类上，表示类中的所有响应请求的方法都是以该地址作为父路径。

    RequestMapping注解有六个属性，下面我们把她分成三类进行说明。

    **value， method：**

    - value：指定请求的实际地址，指定的地址可以是URI Template 模式（后面将会说明）；
    - method：指定请求的method类型， GET、POST、PUT、DELETE等；

    **consumes，produces**

    - consumes：指定处理请求的提交内容类型（Content-Type），例如application/json, text/html；
    - produces：指定返回的内容类型，仅当request请求头中的(Accept)类型中包含该指定类型才返回；

    **params，headers**

    - params： 指定request中必须包含某些参数值是，才让该方法处理。

    - headers：指定request中必须包含某些指定的header值，才能让该方法处理请求。

      

14. #### @Autowired 的作用是什么？

    对属性进行自动装配。当我们抽象出表现层，服务层，数据层时，少不了层级之间类的相互引用。@Autowired给我们提供了相互引用的自动装配，使我们可以不去考虑具体的成员之间的依赖是如何实现的。

    在程序编写时，常有类之间的互相引用，比如控制层引用服务层，服务层又引用持久层。所以，使用@Autowire的方式可满足在以注解为配置bean方式下的引用问题。

    可在类内定义上，set方法上对编写@Autowire。

    

## 11. Spring Boot/Spring Cloud

1. #### 什么是 spring boot？

   在Spring框架这个大家族中，产生了很多衍生框架，比如 Spring、SpringMvc框架等，Spring的核心内容在于控制反转(IOC)和依赖注入(DI),所谓控制反转并非是一种技术，而是一种思想，在操作方面是指在spring配置文件中创建，依赖注入即为由spring容器为应用程序的某个对象提供资源，比如 引用对象、常量数据等。

   SpringBoot是一个框架，一种全新的编程规范，他的产生简化了框架的使用，所谓简化是指简化了Spring众多框架中所需的大量且繁琐的配置文件，所以 SpringBoot是一个服务于框架的框架，服务范围是简化配置文件。

   

2. #### 为什么要用 spring boot？

   Spring Boot使编码变简单

   Spring Boot使配置变简单

   Spring Boot使部署变简单

   Spring Boot使监控变简单

   

3. #### spring boot 核心配置文件是什么？

   - properties文件

   - yml文件

     

4. #### spring boot 配置文件有哪几种类型？它们有什么区别？

   Spring Boot提供了两种常用的配置文件，分别是properties文件和yml文件。相对于properties文件而言，yml文件更年轻，也有很多的坑。可谓成也萧何败萧何，yml通过空格来确定层级关系，使配置文件结构跟清晰，但也会因为微不足道的空格而破坏了层级关系。

   

5. #### spring boot 有哪些方式可以实现热部署？

   springboot有3中热部署方式：

   （1）使用springloaded配置pom.xml文件，使用mvn spring-boot:run启动

   （2）使用springloaded本地加载启动，配置jvm参数

   -javaagent:<jar包地址> -noverify

   （3）使用devtools工具包，操作简单，但是每次需要重新部署

   在项目的pom文件中添加依赖：

   ```xml
    <!--热部署jar-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
    </dependency>
   
   ```

   然后：使用 shift+ctrl+alt+"/" （IDEA中的快捷键） 选择"Registry" 然后勾选 compiler.automake.allow.when.app.running

   https://blog.csdn.net/chachapaofan/article/details/88697452

   

6. #### jpa 和 hibernate 有什么区别？

   - JPA Java Persistence API，是Java EE 5的标准ORM接口，也是ejb3规范的一部分。

   - Hibernate，当今很流行的ORM框架，是JPA的一个实现，但是其功能是JPA的超集。

   - JPA和Hibernate之间的关系，可以简单的理解为JPA是标准接口，Hibernate是实现。那么Hibernate是如何实现与JPA的这种关系的呢。Hibernate主要是通过三个组件来实现的，及hibernate-annotation、hibernate-entitymanager和hibernate-core。

   - ibernate-annotation是Hibernate支持annotation方式配置的基础，它包括了标准的JPA annotation以及Hibernate自身特殊功能的annotation。

   - hibernate-core是Hibernate的核心实现，提供了Hibernate所有的核心功能。

   - hibernate-entitymanager实现了标准的JPA，可以把它看成hibernate-core和JPA之间的适配器，它并不直接提供ORM的功能，而是对hibernate-core进行封装，使得Hibernate符合JPA的规范。

     

7. #### 什么是 spring cloud？

   从字面理解，Spring Cloud 就是致力于分布式系统、云服务的框架。

   Spring Cloud 是整个 Spring 家族中新的成员，是最近云服务火爆的必然产物。

   Spring Cloud 为开发人员提供了快速构建分布式系统中一些常见模式的工具，例如：

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sli24k6j306s0b7aaj.jpg)

   使用 Spring Cloud 开发人员可以开箱即用的实现这些模式的服务和应用程序。这些服务可以任何环境下运行，包括分布式环境，也包括开发人员自己的笔记本电脑以及各种托管平台。

   

8. ####  spring cloud 断路器的作用是什么？

   在Spring Cloud中使用了Hystrix 来实现断路器的功能，断路器可以防止一个应用程序多次试图执行一个操作，即很可能失败，允许它继续而不等待故障恢复或者浪费 CPU 周期，而它确定该故障是持久的。断路器模式也使应用程序能够检测故障是否已经解决，如果问题似乎已经得到纠正，应用程序可以尝试调用操作。

   断路器增加了稳定性和灵活性，以一个系统，提供稳定性，而系统从故障中恢复，并尽量减少此故障的对性能的影响。它可以帮助快速地拒绝对一个操作，即很可能失败，而不是等待操作超时（或者不返回）的请求，以保持系统的响应时间。如果断路器提高每次改变状态的时间的事件，该信息可以被用来监测由断路器保护系统的部件的健康状况，或以提醒管理员当断路器跳闸，以在打开状态。

   

9. #### spring cloud 的核心组件有哪些？

   ①. 服务发现——Netflix Eureka

   一个RESTful服务，用来定位运行在AWS地区（Region）中的中间层服务。由两个组件组成：Eureka服务器和Eureka客户端。Eureka服务器用作服务注册服务器。Eureka客户端是一个java客户端，用来简化与服务器的交互、作为轮询负载均衡器，并提供服务的故障切换支持。Netflix在其生产环境中使用的是另外的客户端，它提供基于流量、资源利用率以及出错状态的加权负载均衡。

   ②. 客服端负载均衡——Netflix Ribbon

   Ribbon，主要提供客户侧的软件负载均衡算法。Ribbon客户端组件提供一系列完善的配置选项，比如连接超时、重试、重试算法等。Ribbon内置可插拔、可定制的负载均衡组件。

   ③. 断路器——Netflix Hystrix

   断路器可以防止一个应用程序多次试图执行一个操作，即很可能失败，允许它继续而不等待故障恢复或者浪费 CPU 周期，而它确定该故障是持久的。断路器模式也使应用程序能够检测故障是否已经解决。如果问题似乎已经得到纠正，应用程序可以尝试调用操作。

   ④. 服务网关——Netflix Zuul

   类似nginx，反向代理的功能，不过netflix自己增加了一些配合其他组件的特性。

   ⑤. 分布式配置——Spring Cloud Config

   这个还是静态的，得配合Spring Cloud Bus实现动态的配置更新。

   

## **12. Hibernate**

1. #### 为什么要使用 hibernate？

   - 对JDBC访问数据库的代码做了封装，大大简化了数据访问层繁琐的重复性代码。

   - Hibernate是一个基于JDBC的主流持久化框架，是一个优秀的ORM实现。他很大程度的简化DAO层的编码工作

   - hibernate使用Java反射机制，而不是字节码增强程序来实现透明性。

   - hibernate的性能非常好，因为它是个轻量级框架。映射的灵活性很出色。它支持各种关系数据库，从一对一到多对多的各种复杂关系。

     

2. #### 什么是 ORM 框架？

   对象-关系映射（Object-Relational Mapping，简称ORM），面向对象的开发方法是当今企业级应用开发环境中的主流开发方法，关系数据库是企业级应用环境中永久存放数据的主流数据存储系统。对象和关系数据是业务实体的两种表现形式，业务实体在内存中表现为对象，在数据库中表现为关系数据。内存中的对象之间存在关联和继承关系，而在数据库中，关系数据无法直接表达多对多关联和继承关系。因此，对象-关系映射(ORM)系统一般以中间件的形式存在，主要实现程序对象到关系数据库数据的映射。

   

3. #### hibernate 中如何在控制台查看打印的 sql 语句？

   [blog.csdn.net/Randy_Wang_/article/details/79460306](http://blog.csdn.net/Randy_Wang_/article/details/79460306)

   

4. #### hibernate 有几种查询方式？

   - hql查询

   - sql查询

   - 条件查询

     hql查询，sql查询，条件查询

     ```java
     HQL:  Hibernate Query Language. 面向对象的写法:
     Query query = session.createQuery("from Customer where name = ?");
     query.setParameter(0, "老师");
     Query.list();
     
     ```



     QBC:  Query By Criteria.(条件查询)
     Criteria criteria = session.createCriteria(Customer.class);
     criteria.add(Restrictions.eq("name", "花姐"));
     List<Customer> list = criteria.list();




     SQL:
     SQLQuery query = session.createSQLQuery("select * from customer");
     List<Object[]> list = query.list();
    
     SQLQuery query = session.createSQLQuery("select * from customer");
     query.addEntity(Customer.class);
     List<Customer> list = query.list();
     ```
    
     Hql： 具体分类
     1、 属性查询 2、 参数查询、命名参数查询 3、 关联查询 4、 分页查询 5、 统计函数
    
     ​
    
     HQL和SQL的区别
    
     HQL是面向对象查询操作的，SQL是结构化查询语言 是面向数据库表结构的
    
     ​


5. #### hibernate 实体类可以被定义为 final 吗？

   可以将Hibernate的实体类定义为final类，但这种做法并不好。因为Hibernate会使用代理模式在延迟关联的情况下提高性能，如果你把实体类定义成final类之后，因为 Java不允许对final类进行扩展，所以Hibernate就无法再使用代理了，如此一来就限制了使用可以提升性能的手段。不过，如果你的持久化类实现了一个接口而且在该接口中声明了所有定义于实体类中的所有public的方法轮到话，你就能够避免出现前面所说的不利后果。

   

6. #### 在 hibernate 中使用 Integer 和 int 做映射有什么区别？

   在Hibernate中，如果将OID定义为Integer类型，那么Hibernate就可以根据其值是否为null而判断一个对象是否是临时的，如果将OID定义为了int类型，还需要在hbm映射文件中设置其unsaved-value属性为0。

   

7. #### hibernate 是如何工作的？

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86slttnu0j30j108qq4w.jpg)

   

8. #### get()和 load()的区别？

   - load() 没有使用对象的其他属性的时候，没有SQL 延迟加载

   - get() 没有使用对象的其他属性的时候，也生成了SQL 立即加载

     

9. #### 说一下 hibernate 的缓存机制？

   Hibernate中的缓存分为一级缓存和二级缓存。

   一级缓存就是 Session 级别的缓存，在事务范围内有效是,内置的不能被卸载。二级缓存是 SesionFactory级别的缓存，从应用启动到应用结束有效。是可选的，默认没有二级缓存，需要手动开启。保存数据库后，缓存在内存中保存一份，如果更新了数据库就要同步更新。

   什么样的数据适合存放到第二级缓存中？

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sm0arrtj308n03sq35.jpg)

   扩展：hibernate的二级缓存默认是不支持分布式缓存的。使用 memcahe,redis等中央缓存来代替二级缓存。

   

10. #### hibernate 对象有哪些状态？

    hibernate里对象有三种状态：

    - Transient（瞬时）：对象刚new出来，还没设id，设了其他值。
    - Persistent（持久）：调用了save()、saveOrUpdate()，就变成Persistent，有id。
    - etached（脱管）：当session close()完之后，变成Detached。

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86smbkv2nj30ir0c20t8.jpg)

    

11. #### 在 hibernate 中 getCurrentSession 和 openSession 的区别是什么？

    openSession 从字面上可以看得出来，是打开一个新的session对象，而且每次使用都是打开一个新的session，假如连续使用多次，则获得的session不是同一个对象，并且使用完需要调用close方法关闭session。

    getCurrentSession ，从字面上可以看得出来，是获取当前上下文一个session对象，当第一次使用此方法时，会自动产生一个session对象，并且连续使用多次时，得到的session都是同一个对象，这就是与openSession的区别之一，简单而言，getCurrentSession 就是：如果有已经使用的，用旧的，如果没有，建新的。

    注意：在实际开发中，往往使用getCurrentSession多，因为一般是处理同一个事务（即是使用一个数据库的情况），所以在一般情况下比较少使用openSession或者说openSession是比较老旧的一套接口了。

    

12. #### hibernate 实体类必须要有无参构造函数吗？为什么？

    必须，因为hibernate框架会调用这个默认构造方法来构造实例对象，即Class类的newInstance方法，这个方法就是通过调用默认构造方法来创建实例对象的。

    另外再提醒一点，如果你没有提供任何构造方法，虚拟机会自动提供默认构造方法（无参构造器），但是如果你提供了其他有参数的构造方法的话，虚拟机就不再为你提供默认构造方法，这时必须手动把无参构造器写在代码里，否则new Xxxx()是会报错的，所以默认的构造方法不是必须的，只在有多个构造方法时才是必须的，这里“必须”指的是“必须手动写出来”。

    

## **13. Mybatis**

1. #### mybatis 中 #{}和 ${}的区别是什么？

   {}是预编译处理，${}是字符串替换；

   Mybatis在处理#{}时，会将sql中的#{}替换为?号，调用PreparedStatement的set方法来赋值；

   Mybatis在处理${}时，就是把{}替换成变量的值。

   使用#{}可以有效的防止SQL注入，提高系统安全性。${}用于分表时。

   

2. #### mybatis 有几种分页方式？

   **（1）数组分页**

   查询出全部数据，然后再list中截取需要的部分。

   mybatis接口

   ```
   List<Student> queryStudentsByArray();
   
   ```

   xml配置文件

   ```
    <select id="queryStudentsByArray"  resultMap="studentmapper">
           select * from student
    </select>
   
   ```

   service

   ```
   接口
   List<Student> queryStudentsByArray(int currPage, int pageSize);
   实现接口
    @Override
       public List<Student> queryStudentsByArray(int currPage, int pageSize) {
           //查询全部数据
           List<Student> students = studentMapper.queryStudentsByArray();
           //从第几条数据开始
           int firstIndex = (currPage - 1) * pageSize;
           //到第几条数据结束
           int lastIndex = currPage * pageSize;
           return students.subList(firstIndex, lastIndex); //直接在list中截取
       }
   
   ```

   controller

   ```
       @ResponseBody
       @RequestMapping("/student/array/{currPage}/{pageSize}")
       public List<Student> getStudentByArray(@PathVariable("currPage") int currPage, @PathVariable("pageSize") int pageSize) {
           List<Student> student = StuServiceIml.queryStudentsByArray(currPage, pageSize);
           return student;
       }
   
   ```

   **（2）sql分页**

   mybatis接口

   ```
   List<Student> queryStudentsBySql(Map<String,Object> data);
   
   ```

   xml文件

   ```
   <select id="queryStudentsBySql" parameterType="map" resultMap="studentmapper">
           select * from student limit #{currIndex} , #{pageSize}
   </select>
   
   ```

   service

   ```
   接口
   List<Student> queryStudentsBySql(int currPage, int pageSize);
   实现类
   public List<Student> queryStudentsBySql(int currPage, int pageSize) {
           Map<String, Object> data = new HashedMap();
           data.put("currIndex", (currPage-1)*pageSize);
           data.put("pageSize", pageSize);
           return studentMapper.queryStudentsBySql(data);
       }
   
   ```

   **（3）拦截器分页**

   创建拦截器，拦截mybatis接口方法id以ByPage结束的语句

   ```
   package com.autumn.interceptor;
   
   import org.apache.ibatis.executor.Executor;
   import org.apache.ibatis.executor.parameter.ParameterHandler;
   import org.apache.ibatis.executor.resultset.ResultSetHandler;
   import org.apache.ibatis.executor.statement.StatementHandler;
   import org.apache.ibatis.mapping.MappedStatement;
   import org.apache.ibatis.plugin.*;
   import org.apache.ibatis.reflection.MetaObject;
   import org.apache.ibatis.reflection.SystemMetaObject;
   
   import java.sql.Connection;
   import java.util.Map;
   import java.util.Properties;
   
   /**
    * @Intercepts 说明是一个拦截器
    * @Signature 拦截器的签名
    * type 拦截的类型 四大对象之一( Executor,ResultSetHandler,ParameterHandler,StatementHandler)
    * method 拦截的方法
    * args 参数,高版本需要加个Integer.class参数,不然会报错
    */
   @Intercepts({@Signature(type = StatementHandler.class, method = "prepare", args = {Connection.class})})
   public class MyPageInterceptor implements Interceptor {
   
       //每页显示的条目数
       private int pageSize;
       //当前现实的页数
       private int currPage;
       //数据库类型
       private String dbType;
   
   ```


        @Override
        public Object intercept(Invocation invocation) throws Throwable {
            //获取StatementHandler，默认是RoutingStatementHandler
            StatementHandler statementHandler = (StatementHandler) invocation.getTarget();
            //获取statementHandler包装类
            MetaObject MetaObjectHandler = SystemMetaObject.forObject(statementHandler);
    
            //分离代理对象链
            while (MetaObjectHandler.hasGetter("h")) {
                Object obj = MetaObjectHandler.getValue("h");
                MetaObjectHandler = SystemMetaObject.forObject(obj);
            }
    
            while (MetaObjectHandler.hasGetter("target")) {
                Object obj = MetaObjectHandler.getValue("target");
                MetaObjectHandler = SystemMetaObject.forObject(obj);
            }
    
            //获取连接对象
            //Connection connection = (Connection) invocation.getArgs()[0];



            //object.getValue("delegate");  获取StatementHandler的实现类
    
            //获取查询接口映射的相关信息
            MappedStatement mappedStatement = (MappedStatement) MetaObjectHandler.getValue("delegate.mappedStatement");
            String mapId = mappedStatement.getId();
    
            //statementHandler.getBoundSql().getParameterObject();
    
            //拦截以.ByPage结尾的请求，分页功能的统一实现
            if (mapId.matches(".+ByPage$")) {
                //获取进行数据库操作时管理参数的handler
                ParameterHandler parameterHandler = (ParameterHandler) MetaObjectHandler.getValue("delegate.parameterHandler");
                //获取请求时的参数
                Map<String, Object> paraObject = (Map<String, Object>) parameterHandler.getParameterObject();
                //也可以这样获取
                //paraObject = (Map<String, Object>) statementHandler.getBoundSql().getParameterObject();
    
                //参数名称和在service中设置到map中的名称一致
                currPage = (int) paraObject.get("currPage");
                pageSize = (int) paraObject.get("pageSize");
    
                String sql = (String) MetaObjectHandler.getValue("delegate.boundSql.sql");
                //也可以通过statementHandler直接获取
                //sql = statementHandler.getBoundSql().getSql();
    
                //构建分页功能的sql语句
                String limitSql;
                sql = sql.trim();
                limitSql = sql + " limit " + (currPage - 1) * pageSize + "," + pageSize;
    
                //将构建完成的分页sql语句赋值个体'delegate.boundSql.sql'，偷天换日
                MetaObjectHandler.setValue("delegate.boundSql.sql", limitSql);
            }
            //调用原对象的方法，进入责任链的下一级
            return invocation.proceed();
        }



        //获取代理对象
        @Override
        public Object plugin(Object o) {
            //生成object对象的动态代理对象
            return Plugin.wrap(o, this);
        }
    
        //设置代理对象的参数
        @Override
        public void setProperties(Properties properties) {
            //如果项目中分页的pageSize是统一的，也可以在这里统一配置和获取，这样就不用每次请求都传递pageSize参数了。参数是在配置拦截器时配置的。
            String limit1 = properties.getProperty("limit", "10");
            this.pageSize = Integer.valueOf(limit1);
            this.dbType = properties.getProperty("dbType", "mysql");
        }
    }
    ```
    
     配置文件SqlMapConfig.xml
    
    ```
    <configuration>
    
        <plugins>
            <plugin interceptor="com.autumn.interceptor.MyPageInterceptor">
                <property name="limit" value="10"/>
                <property name="dbType" value="mysql"/>
            </plugin>
        </plugins>
    
    </configuration>
    ```
    
    mybatis配置
    
    ```
    <!--接口-->
    List<AccountExt> getAllBookByPage(@Param("currPage")Integer pageNo,@Param("pageSize")Integer pageSize);
    <!--xml配置文件-->
      <sql id="getAllBooksql" >
        acc.id, acc.cateCode, cate_name, user_id,u.name as user_name, money, remark, time
      </sql>
      <select id="getAllBook" resultType="com.autumn.pojo.AccountExt" >
        select
        <include refid="getAllBooksql" />
        from account as acc
      </select>
    ```
    
    service
    
    ```
        public List<AccountExt> getAllBookByPage(String pageNo,String pageSize) {
            return accountMapper.getAllBookByPage(Integer.parseInt(pageNo),Integer.parseInt(pageSize));
        }
    ```
    
    controller
    
    ```
        @RequestMapping("/getAllBook")
        @ResponseBody
        public Page getAllBook(String pageNo,String pageSize,HttpServletRequest request,HttpServletResponse response){
            pageNo=pageNo==null?"1":pageNo;   //当前页码
            pageSize=pageSize==null?"5":pageSize;   //页面大小
            //获取当前页数据
            List<AccountExt> list = bookService.getAllBookByPage(pageNo,pageSize);
            //获取总数据大小
            int totals = bookService.getAllBook();
            //封装返回结果
            Page page = new Page();
            page.setTotal(totals+"");
            page.setRows(list);
            return page;
        }
    ```
    
    Page实体类
    
    ```
    package com.autumn.pojo;
    
    import java.util.List;
    
    /**
     * Created by Autumn on 2018/6/21.
     */
    public class Page {
        private String pageNo = null;
        private String pageSize = null;
        private String total = null;
        private List rows = null;
    
        public String getTotal() {
            return total;
        }
    
        public void setTotal(String total) {
            this.total = total;
        }
    
        public List getRows() {
            return rows;
        }
    
        public void setRows(List rows) {
            this.rows = rows;
        }
    
        public String getPageNo() {
            return pageNo;
        }
    
        public void setPageNo(String pageNo) {
            this.pageNo = pageNo;
        }
    
        public String getPageSize() {
            return pageSize;
        }
    
        public void setPageSize(String pageSize) {
            this.pageSize = pageSize;
        }
    
    }
    ```
    
    前端
    
    bootstrap-table接受数据格式
    
    ```
    {
      "total": 3,
      "rows": [
        {
          "id": 0,
          "name": "Item 0",
          "price": "$0"
        },
        {
          "id": 1,
          "name": "Item 1",
          "price": "$1"
        }
      ]
    }
    ```
    
    boostrap-table用法
    
    ```
            var $table = $('#table');
            $table.bootstrapTable({
            url: "/${appName}/manager/bookController/getAllBook",
            method: 'post',
            contentType: "application/x-www-form-urlencoded",
            dataType: "json",
            pagination: true, //分页
            sidePagination: "server", //服务端处理分页
            pageList: [5, 10, 25],
            pageSize: 5,
            pageNumber:1,
            //toolbar:"#tb",
            singleSelect: false,
            queryParamsType : "limit",
            queryParams: function queryParams(params) {   //设置查询参数
              var param = {
                pageNo: params.offset/params.limit+1,  //offset为数据开始索引,转换为显示当前页
                pageSize: params.limit  //页面大小
              };
              console.info(params);   //查看参数是什么
              console.info(param);   //查看自定义的参数
              return param;
            },
            cache: false,
            //data-locale: "zh-CN", //表格汉化
            //search: true, //显示搜索框
            columns: [
                    {
                        checkbox: true
                    },
                    {
                        title: '消费类型',
                        field: 'cate_name',
                        valign: 'middle'
                    },
                    {
                        title: '消费金额',
                        field: 'money',
                        valign: 'middle',
                        formatter:function(value,row,index){
                            if(!isNaN(value)){   //是数字
                                return value/100;
                            }
                        }
                    },
                    {
                        title: '备注',
                        field: 'remark',
                        valign: 'middle'
                    },
                    {
                        title: '消费时间',
                        field: 'time',
                        valign: 'middle'
                    },
                    {
                        title: '操作',
                        field: '',
                        formatter:function(value,row,index){
                            var f = '<a href="#" class="btn btn-gmtx-define1" onclick="delBook(\''+ row.id +'\')">删除</a> ';
                            return f;
                           }
                    }
                ]
              });
          });
    ```
    
    **（4）RowBounds分页**
    
    数据量小时，RowBounds不失为一种好办法。但是数据量大时，实现拦截器就很有必要了。
    
    mybatis接口加入RowBounds参数
    
    public List<UserBean> queryUsersByPage(String userName, RowBounds rowBounds);
    
    service
    
    ```
        @Override
        @Transactional(isolation = Isolation.READ_COMMITTED, propagation = Propagation.SUPPORTS)
        public List<RoleBean> queryRolesByPage(String roleName, int start, int limit) {
            return roleDao.queryRolesByPage(roleName, new RowBounds(start, limit));
        }
    ```
    
    ​


3. #### RowBounds 是一次性查询全部结果吗？为什么？

   是的，是属于逻辑分页
   RowBounds 在分页的时候，是把所有的数据都查询出来，然后通过RowBounds在内存进行分页，通过源码查看,也是通过ResuleSet结果集进行分页

   

4. #### mybatis 逻辑分页和物理分页的区别是什么？

   - 逻辑分页 内存开销比较大,在数据量比较小的情况下效率比物理分页高;在数据量很大的情况下,内存开销过大,容易内存溢出,不建议使用

   - 物理分页 内存开销比较小,在数据量比较小的情况下效率比逻辑分页还是低,在数据量很大的情况下,建议使用物理分页

     

5. #### mybatis 是否支持延迟加载？延迟加载的原理是什么？

   延迟加载其实就是将数据加载时机推迟，比如推迟嵌套查询的执行时机。在Mybatis中经常用到关联查询，但是并不是任何时候都需要立即返回关联查询结果。比如查询订单信息，并不一定需要及时返回订单对应的产品信息，查询商品分类信息并不一定要及时返回该类别下有哪些产品，这种情况一下需要一种机制，当需要查看时，再执行查询，返回需要的结果集，这种需求在Mybatis中可以使用延迟加载机制来实现。延迟加载可以实现先查询主表，按需实时做关联查询，返回关联表结果集，一定程度上提高了效率。

   Mybatis配置文件中通过两个属性lazyLoadingEnabled和aggressiveLazyLoading来控制延迟加载和按需加载。

   lazyLoadingEnabled：是否启用延迟加载，mybatis默认为false，不启用延迟加载。lazyLoadingEnabled属性控制全局是否使用延迟加载，特殊关联关系也可以通过嵌套查询中fetchType属性单独配置（fetchType属性值lazy或者eager）。

   aggressiveLazyLoading：是否按需加载属性，默认值false，lazyLoadingEnabled属性启用时只要加载对象，就会加载该对象的所有属性；关闭该属性则会按需加载，即使用到某关联属性时，实时执行嵌套查询加载该属性。

   延迟加载的好处：
   先从单表查询、需要时再从关联表去关联查询，大大提高 数据库性能，因为查询单表要比关联查询多张表速度要快。
   如果查询订单并且关联查询用户信息。如果先查询订单信息即可满足要求，当我们需要查询用户信息时再查询用户信息。把对用户信息的按需去查询就是延迟加载。

   

6. #### 说一下 mybatis 的一级缓存和二级缓存？

   **（1）一级缓存**
   　　Mybatis对缓存提供支持，但是在没有配置的默认情况下，它只开启一级缓存，一级缓存只是相对于同一个SqlSession而言。所以在参数和SQL完全一样的情况下，我们使用同一个SqlSession对象调用一个Mapper方法，往往只执行一次SQL，因为使用SelSession第一次查询后，MyBatis会将其放在缓存中，以后再查询的时候，如果没有声明需要刷新，并且缓存没有超时的情况下，SqlSession都会取出当前缓存的数据，而不会再次发送SQL到数据库。
   一级缓存的生命周期：
   MyBatis在开启一个数据库会话时，会 创建一个新的SqlSession对象，SqlSession对象中会有一个新的Executor对象。Executor对象中持有一个新的PerpetualCache对象；当会话结束时，SqlSession对象及其内部的Executor对象还有PerpetualCache对象也一并释放掉。

   **（2）二级缓存**
   　　MyBatis的二级缓存是Application级别的缓存，它可以提高对数据库查询的效率，以提高应用的性能

   SqlSessionFactory层面上的二级缓存默认是不开启的，二级缓存的开席需要进行配置，实现二级缓存的时候，MyBatis要求返回的POJO必须是可序列化的。 也就是要求实现Serializable接口，配置方法很简单，只需要在映射XML文件配置就可以开启缓存了<cache/>，如果我们配置了二级缓存就意味着：

   - 映射语句文件中的所有select语句将会被缓存

   - 射语句文件中的所有insert、update和delete语句会刷新缓存。

   - 缓存会使用默认的Least Recently Used（LRU，最近最少使用的）算法来收回。

   - 根据时间表，比如No Flush Interval,（CNFI没有刷新间隔），缓存不会以任何时间顺序来刷新。

   - 缓存会存储列表集合或对象(无论查询方法返回什么)的1024个引用

   - 缓存会被视为是read/write(可读/可写)的缓存，意味着对象检索不是共享的，而且可以安全的被调用者修改，不干扰其他调用者或线程所做的潜在修改。

     

7. #### mybatis 和 hibernate 的区别有哪些？

   （1）hibernate是全自动，而mybatis是半自动

   hibernate完全可以通过对象关系模型实现对数据库的操作，拥有完整的JavaBean对象与数据库的映射结构来自动生成sql。而mybatis仅有基本的字段映射，对象数据以及对象实际关系仍然需要通过手写sql来实现和管理。

   （2）hibernate数据库移植性远大于mybatis

   hibernate通过它强大的映射结构和hql语言，大大降低了对象与数据库(oracle、mysql等)的耦合性，而mybatis由于需要手写sql，因此与数据库的耦合性直接取决于程序员写sql的方法，如果sql不具通用性而用了很多某数据库特性的sql语句的话，移植性也会随之降低很多，成本很高。

   （3）hibernate拥有完整的日志系统，mybatis则欠缺一些

   hibernate日志系统非常健全，涉及广泛，包括：sql记录、关系异常、优化警告、缓存提示、脏数据警告等;而mybatis则除了基本记录功能外，功能薄弱很多。

   （4）mybatis相比hibernate需要关心很多细节

   hibernate配置要比mybatis复杂的多，学习成本也比mybatis高。但也正因为mybatis使用简单，才导致它要比hibernate关心很多技术细节。mybatis由于不用考虑很多细节，开发模式上与传统jdbc区别很小，因此很容易上手并开发项目，但忽略细节会导致项目前期bug较多，因而开发出相对稳定的软件很慢，而开发出软件却很快。hibernate则正好与之相反。但是如果使用hibernate很熟练的话，实际上开发效率丝毫不差于甚至超越mybatis。

   （5）sql直接优化上，mybatis要比hibernate方便很多

   由于mybatis的sql都是写在xml里，因此优化sql比hibernate方便很多。而hibernate的sql很多都是自动生成的，无法直接维护sql;虽有hql，但功能还是不及sql强大，见到报表等变态需求时，hql也歇菜，也就是说hql是有局限的;hibernate虽然也支持原生sql，但开发模式上却与orm不同，需要转换思维，因此使用上不是非常方便。总之写sql的灵活度上hibernate不及mybatis。

   - mybatis：

   1. 入门简单，即学即用，提供了数据库查询的自动对象绑定功能，而且延续了很好的SQL使用经验，对于没有那么高的对象模型要求的项目来说，相当完美。
   2. 可以进行更为细致的SQL优化，可以减少查询字段。
   3. 缺点就是框架还是比较简陋，功能尚有缺失，虽然简化了数据绑定代码，但是整个底层数据库查询实际还是要自己写的，工作量也比较大，而且不太容易适应快速数据库修改。
   4. 二级缓存机制不佳。

   - hibernate：

   1. 功能强大，数据库无关性好，O/R映射能力强，如果你对Hibernate相当精通，而且对Hibernate进行了适当的封装，那么你的项目整个持久层代码会相当简单，需要写的代码很少，开发速度很快，非常爽。

   2. 有更好的二级缓存机制，可以使用第三方缓存。

   3. 缺点就是学习门槛不低，要精通门槛更高，而且怎么设计O/R映射，在性能和对象模型之间如何权衡取得平衡，以及怎样用好Hibernate方面需要你的经验和能力都很强才行。

       

8. #### mybatis 有哪些执行器（Executor）？

   Mybatis有三种基本的Executor执行器:SimpleExecutor、ReuseExecutor、BatchExecutor。

   - SimpleExecutor：每执行一次update或select，就开启一个Statement对象，用完立刻关闭Statement对象。
   - ReuseExecutor：执行update或select，以sql作为key查找Statement对象，存在就使用，不存在就创建，用完后，不关闭Statement对象，而是放置于Map内，供下一次使用。简言之，就是重复使用Statement对象。
   - BatchExecutor：执行update（没有select，JDBC批处理不支持select），将所有sql都添加到批处理中（addBatch()），等待统一执行（executeBatch()），它缓存了多个Statement对象，每个Statement对象都是addBatch()完毕后，等待逐一执行executeBatch()批处理。与JDBC批处理相同。

   作用范围：Executor的这些特点，都严格限制在SqlSession生命周期范围内。

   这些就是mybatis的三种执行器。你可以通过配置文件的settings里面的元素defaultExecutorType，配置它，默认是采用SimpleExecutor如果你在Spring运用它，那么你可以这么配置它：

   ```
   <bean id="sqlSessionTemplateBatch" class="org.mybatis.spring.SqlSessionTemplate">     
   <constructor-arg index="0" ref="sqlSessionFactory" />  
   <!--更新采用批量的executor -->  
   <constructor-arg index="1" value="BATCH"/>  
   </bean> 
   
   ```

   

9. #### mybatis 分页插件的实现原理是什么？

   Mybatis采用的是逻辑分页,而非物理分页,那么,市场上就出现了可以实现物理分页的Mybatis的分页插件。

   要实现物理分页,就需要对Stringsql进行拦截并增强,Mybatis通过BoundSql对象存储String sql,而BoundSql则由StatementHandler对象获取。

   public interface StatementHandler {
   List query(Statement statement, ResultHandler resultHandler) throws SQLException;
   BoundSql getBoundSql();
   }
   public class BoundSql {
   public String getSql() {
   return sql;
   }
   }

   因此,就需要编写一个针对StatementHandler的query方法拦截器,然后获取到sql,对sql进行重写增强。
   这里添加一个demo，通过对 MyBatis org.apache.ibatis.executor.statement.StatementHandler 中的prepare 方法进行拦截，用来把Mybatis所有执行的sql都记录下来

   ```
   package com.bytebeats.mybatis3.interceptor;
   import org.apache.ibatis.executor.statement.StatementHandler;
   import org.apache.ibatis.mapping.BoundSql;
   import org.apache.ibatis.plugin.*;
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   import java.sql.Connection;
   import java.util.Properties;
   
   ```


   @Intercepts({ @Signature(type = StatementHandler.class, method = "prepare", args = { Connection.class, Integer.class}) })
   public class SQLStatsInterceptor implements Interceptor {
       private final Logger logger = LoggerFactory.getLogger(this.getClass());

       @Override
       public Object intercept(Invocation invocation) throws Throwable {
    
           StatementHandler statementHandler = (StatementHandler) invocation.getTarget();
           BoundSql boundSql = statementHandler.getBoundSql();
           String sql = boundSql.getSql();
           logger.info("mybatis intercept sql:{}", sql);
           return invocation.proceed();
       }
    
       @Override
       public Object plugin(Object target) {
           return Plugin.wrap(target, this);
       }
    
       @Override
       public void setProperties(Properties properties) {
           String dialect = properties.getProperty("dialect");
           logger.info("mybatis intercept dialect:{}", dialect);
       }


   }


   ​

10. #### mybatis 如何编写一个自定义插件？

    Mybatis自定义插件针对Mybatis四大对象（Executor、StatementHandler 、ParameterHandler 、ResultSetHandler ）进行拦截，具体拦截方式为：
    1、Executor：拦截执行器的方法(log记录)
    2、StatementHandler ：拦截Sql语法构建的处理
    3、ParameterHandler ：拦截参数的处理
    4、ResultSetHandler ：拦截结果集的处理
    前两种应用较为广泛。

    Mybatis自定义插件必须实现Interceptor接口：

    public interface Interceptor {
        Object intercept(Invocation invocation) throws Throwable;
        Object plugin(Object target);
        void setProperties(Properties properties);
    }


  ```
  intercept方法：拦截器具体处理逻辑方法
  plugin方法：根据签名signatureMap生成动态代理对象
  setProperties方法：设置Properties属性


  ```

  // ExamplePlugin.java
  @Intercepts({@Signature(
    type= Executor.class,
    method = "update",
    args = {MappedStatement.class,Object.class})})
  public class ExamplePlugin implements Interceptor {
    public Object intercept(Invocation invocation) throws Throwable {
    Object target = invocation.getTarget(); //被代理对象
    Method method = invocation.getMethod(); //代理方法
    Object[] args = invocation.getArgs(); //方法参数
    // do something ...... 方法拦截前执行代码块
    Object result = invocation.proceed();
    // do something .......方法拦截后执行代码块
    return result;
    }
    public Object plugin(Object target) {
      return Plugin.wrap(target, this);
    }
    public void setProperties(Properties properties) {
    }
  }

  一个@Intercepts可以配置多个@Signature，@Signature中的参数定义如下：
  type：表示拦截的类，这里是Executor的实现类
  method：表示拦截的方法，这里是拦截Executor的update方法
  args：表示方法参数




## **14. RabbitMQ**

\135. rabbitmq 的使用场景有哪些？

\136. rabbitmq 有哪些重要的角色？

\137. rabbitmq 有哪些重要的组件？

\138. rabbitmq 中 vhost 的作用是什么？

\139. rabbitmq 的消息是怎么发送的？

\140. rabbitmq 怎么保证消息的稳定性？

141.rabbitmq 怎么避免消息丢失？

\142. 要保证消息持久化成功的条件有哪些？

\143. rabbitmq 持久化有什么缺点？

\144. rabbitmq 有几种广播类型？

\145. rabbitmq 怎么实现延迟消息队列？

\146. rabbitmq 集群有什么用？

\147. rabbitmq 节点的类型有哪些？

\148. rabbitmq 集群搭建需要注意哪些问题？

\149. rabbitmq 每个节点是其他节点的完整拷贝吗？为什么？

\150. rabbitmq 集群中唯一一个磁盘节点崩溃了会发生什么情况？

\151. rabbitmq 对集群节点停止顺序有要求吗？

## **15. Kafka**

\152. kafka 可以脱离 zookeeper 单独使用吗？为什么？

\153. kafka 有几种数据保留的策略？

\154. kafka 同时设置了 7 天和 10G 清除数据，到第五天的时候消息达到了 10G，这个时候 kafka 将如何处理？

\155. 什么情况会导致 kafka 运行变慢？

\156. 使用 kafka 集群需要注意什么？

## **16. Zookeeper**

\157. zookeeper 是什么？

\158. zookeeper 都有哪些功能？

\159. zookeeper 有几种部署模式？

\160. zookeeper 怎么保证主从节点的状态同步？

\161. 集群中为什么要有主节点？

\162. 集群中有 3 台服务器，其中一个节点宕机，这个时候 zookeeper 还可以使用吗？

\163. 说一下 zookeeper 的通知机制？




 **17. MySql**

1. #### 数据库的三范式是什么？

   - 第一范式：强调的是列的原子性，即数据库表的每一列都是不可分割的原子数据项。

   - 第二范式：要求实体的属性完全依赖于主关键字。所谓完全依赖是指不能存在仅依赖主关键字一部分的属性。

   - 第三范式：任何非主属性不依赖于其它非主属性。

     

2. #### 一张自增表里面总共有 7 条数据，删除了最后 2 条数据，重启 mysql 数据库，又插入了一条数据，此时 id 是几？

   - 表类型如果是 MyISAM ，那 id 就是 18。
   - 表类型如果是 InnoDB，那 id 就是 15。

   InnoDB 表只会把自增主键的最大 id 记录在内存中，所以重启之后会导致最大 id 丢失。

   

3. #### 如何获取当前数据库版本？

   使用 select version() 获取当前 MySQL 数据库版本。

   

4. #### 说一下 ACID 是什么？

   - Atomicity（原子性）：一个事务（transaction）中的所有操作，或者全部完成，或者全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被恢复（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。即，事务不可分割、不可约简。

   - Consistency（一致性）：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设约束、触发器、级联回滚等。

   - Isolation（隔离性）：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

   - Durability（持久性）：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

     

5. #### char 和 varchar 的区别是什么？

   **（1）char(n) ：**固定长度类型，比如订阅 char(10)，当你输入"abc"三个字符的时候，它们占的空间还是 10 个字节，其他 7 个是空字节。

   chat 优点：效率高；缺点：占用空间；适用场景：存储密码的 md5 值，固定长度的，使用 char 非常合适。

   **（2）varchar(n) ：**可变长度，存储的值是每个值占用的字节再加上一个用来记录其长度的字节的长度。

   所以，从空间上考虑 varcahr 比较合适；从效率上考虑 char 比较合适，二者使用需要权衡。

   

6. #### float 和 double 的区别是什么？

   - float 最多可以存储 8 位的十进制数，并在内存中占 4 字节。

   - double 最可可以存储 16 位的十进制数，并在内存中占 8 字节。

     

7. #### mysql 的内连接、左连接、右连接有什么区别？

   内连接关键字：inner join；左连接：left join；右连接：right join。

   内连接是把匹配的关联数据显示出来；左连接是左边的表全部显示出来，右边的表显示出符合条件的数据；右连接正好相反。

   

8. #### mysql 索引是怎么实现的？

   索引是满足某种特定查找算法的数据结构，而这些数据结构会以某种方式指向数据，从而实现高效查找数据。

   具体来说 MySQL 中的索引，不同的数据引擎实现有所不同，但目前主流的数据库引擎的索引都是 B+ 树实现的，B+ 树的搜索效率，可以到达二分法的性能，找到数据区域之后就找到了完整的数据结构了，所有索引的性能也是更好的。

   

9. #### 怎么验证 mysql 的索引是否满足需求？

   使用 explain 查看 SQL 是如何执行查询语句的，从而分析你的索引是否满足需求。

   explain 语法：explain select * from table where type=1。

   

10. #### 说一下数据库的事务隔离？

    MySQL 的事务隔离是在 MySQL. ini 配置文件里添加的，在文件的最后添加：transaction-isolation = REPEATABLE-READ

    可用的配置值：READ-UNCOMMITTED、READ-COMMITTED、REPEATABLE-READ、SERIALIZABLE。

    - READ-UNCOMMITTED：未提交读，最低隔离级别、事务未提交前，就可被其他事务读取（会出现幻读、脏读、不可重复读）。
    - READ-COMMITTED：提交读，一个事务提交后才能被其他事务读取到（会造成幻读、不可重复读）。
    - REPEATABLE-READ：可重复读，默认级别，保证多次读取同一个数据时，其值都和事务开始时候的内容是一致，禁止读取到别的事务未提交的数据（会造成幻读）。
    - SERIALIZABLE：序列化，代价最高最可靠的隔离级别，该隔离级别能防止脏读、不可重复读、幻读。

    脏读 ：表示一个事务能够读取另一个事务中还未提交的数据。比如，某个事务尝试插入记录 A，此时该事务还未提交，然后另一个事务尝试读取到了记录 A。

    不可重复读 ：是指在一个事务内，多次读同一数据。

    幻读 ：指同一个事务内多次查询返回的结果集不一样。比如同一个事务 A 第一次查询时候有 n 条记录，但是第二次同等条件下查询却有 n+1 条记录，这就好像产生了幻觉。发生幻读的原因也是另外一个事务新增或者删除或者修改了第一个事务结果集里面的数据，同一个记录的数据内容被修改了，所有数据行的记录就变多或者变少了。

    

11. #### 说一下 mysql 常用的引擎？

    **InnoDB 引擎：**InnoDB 引擎提供了对数据库 acid 事务的支持，并且还提供了行级锁和外键的约束，它的设计的目标就是处理大数据容量的数据库系统。MySQL 运行的时候，InnoDB 会在内存中建立缓冲池，用于缓冲数据和索引。但是该引擎是不支持全文搜索，同时启动也比较的慢，它是不会保存表的行数的，所以当进行 select count(*) from table 指令的时候，需要进行扫描全表。由于锁的粒度小，写操作是不会锁定全表的,所以在并发度较高的场景下使用会提升效率的。

    **MyIASM 引擎：**MySQL 的默认引擎，但不提供事务的支持，也不支持行级锁和外键。因此当执行插入和更新语句时，即执行写操作的时候需要锁定这个表，所以会导致效率会降低。不过和 InnoDB 不同的是，MyIASM 引擎是保存了表的行数，于是当进行 select count(*) from table 语句时，可以直接的读取已经保存的值而不需要进行扫描全表。所以，如果表的读操作远远多于写操作时，并且不需要事务的支持的，可以将 MyIASM 作为数据库引擎的首选。

    

12. #### 说一下 mysql 的行锁和表锁？

    MyISAM 只支持表锁，InnoDB 支持表锁和行锁，默认为行锁。

    - 表级锁：开销小，加锁快，不会出现死锁。锁定粒度大，发生锁冲突的概率最高，并发量最低。

    - 行级锁：开销大，加锁慢，会出现死锁。锁力度小，发生锁冲突的概率小，并发度最高。

      

13. #### 说一下乐观锁和悲观锁？

    - 乐观锁：每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在提交更新的时候会判断一下在此期间别人有没有去更新这个数据。
    - 悲观锁：每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会阻止，直到这个锁被释放。

    数据库的乐观锁需要自己实现，在表里面添加一个 version 字段，每次修改成功值加 1，这样每次修改的时候先对比一下，自己拥有的 version 和数据库现在的 version 是否一致，如果不一致就不修改，这样就实现了乐观锁。

    

14. #### mysql 问题排查都有哪些手段？

    - 使用 show processlist 命令查看当前所有连接信息。

    - 使用 explain 命令查询 SQL 语句执行计划。

    - 开启慢查询日志，查看慢查询的 SQL。

      

15. #### 如何做 mysql 的性能优化？

    - 为搜索字段创建索引。

    - 避免使用 select *，列出需要查询的字段。

    - 垂直分割分表。

    - 选择正确的存储引擎。

      

## **18. Redis**

1. redis 是什么？都有哪些使用场景？

2. redis 有哪些功能？

3. redis 和 memecache 有什么区别？

4. redis 为什么是单线程的？

5. 什么是缓存穿透？怎么解决？

6. redis 支持的数据类型有哪些？

7. redis 支持的 java 客户端都有哪些？

8. jedis 和 redisson 有哪些区别？

9. 怎么保证缓存和数据库数据的一致性？

10. redis 持久化有几种方式？

11. redis 怎么实现分布式锁？

12. redis 分布式锁有什么缺陷？

13. redis 如何做内存优化？

14. redis 淘汰策略有哪些？

15. redis 常见的性能问题有哪些？该如何解决？

  ​    

## **19. JVM**

1. #### 说一下 jvm 的主要组成部分？及其作用？

   - 类加载器（ClassLoader）
   - 运行时数据区（Runtime Data Area）
   - 执行引擎（Execution Engine）
   - 本地库接口（Native Interface）

   组件的作用： 首先通过类加载器（ClassLoader）会把 Java 代码转换成字节码，运行时数据区（Runtime Data Area）再把字节码加载到内存中，而字节码文件只是 JVM 的一套指令集规范，并不能直接交给底层操作系统去执行，因此需要特定的命令解析器执行引擎（Execution Engine），将字节码翻译成底层系统指令，再交由 CPU 去执行，而这个过程中需要调用其他语言的本地库接口（Native Interface）来实现整个程序的功能。（类加载器+java文件——>运行时数据区+字节码文件+内存——>命令解析器执行引擎+字节码文件——>底层系统指令+本地库接口+cpu）

   

2. #### 说一下 jvm 运行时数据区？

   有的区域随着虚拟机进程的启动而存在，有的区域则依赖用户进程的启动和结束而创建和销毁。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86sn4dsc8j30d70b2wey.jpg)

   **（1）程序计数器**
   ​	程序计数器（Program Counter Register）是一块较小的内存空间。它可以视为**当前线程**所执行的**行号	指示器**，指令在执行时，需要通过改变这个计数器来选取下一条需要执行的指令。Java虚拟机的多线程是通过轮流切换并分配处理器执行时间的方式来实现的，在一个确定的时刻只有一个处理器执行一条线程中的指令，**为了在线程切换后能恢复到正确的执行位置，每个线程都会有一个独立的程序计数器**，因此，**程序计数器是线程私有的**。

   **（2）Java虚拟机栈**
   ​	Java虚拟机栈（Java Virtual Machine Stacks)，和程序计数器一样也是**线程私有**的，它的生命周期与线程相同，与线程是同时创建的。

   ​	Java虚拟机栈**存储线程中Java方法调用的状态**，包括局部变量、参数、返回值以及运算的中间结果等。**一个Java虚拟机栈包含了多个栈帧，一个栈帧用来存储局部变量表、操作数栈、动态链接、方法出口等信息**。当线程调用一个Java方法时，虚拟机压入一个新的栈帧到该线程的Java栈中，当该方法执行完成，这个栈帧就从Java栈中弹出。我们平常所说的**栈内存（Stack）指的就是Java虚拟机栈**。 

   **（3）本地方法栈**
   ​	本地方法栈（Native Method Stack）与Java虚拟机栈的作用非常类似，他们的区别就是Java虚拟机栈为虚拟机执行Java方法而服务，**本地方法栈则是为虚拟机用到本地Native方法而服务**。

   ​	在Java虚拟机规范中对本地方法栈的语言和数据结构等没有强制规定，因此具体的Java虚拟机可以自由实现它，比如HotSpot VM**将本地方法栈和Java虚拟机栈合二为一**。

   **（4）Java堆**

   ​	Java堆（Java Heap）是Java虚拟机所**管理内存中最大的一块**，被所有**线程共享的一块内存区域**，在虚拟机启动时创建。

   ​	Java**堆存储的对象被垃圾收集器管理**，这些受管理的对象无需也无法显示的销毁。从内存回收的角度，Java堆可以粗略的分为新生代和老年代。从内存分配的角度Java堆中可能划分出多个线程私有的分配缓冲区。根据Java虚拟机规范规定，Java堆的所使用的内存在物理上不需要连续，逻辑上连续即可。 如果在堆中没有足够的内存来完成实例分配，并且堆也无法进行扩展时，则会抛出OutOfMemoryError异常。

   **（5）方法区**
   ​	方法区（Method Area）也是被所有**线程共享的运行时内存区域**。用来存储**已经被Java虚拟机加载的类的结构信息、常量、静态变量和即时编译器编译后的代码等数据**。如果方法区的内存空间不满足内存分配需求时，Java虚拟机会抛出OutOfMemoryError异常。

   **（6）运行时常量池**
   ​	运行时常量池（Runtime Constant Pool）是方法区的一部分。Class文件不仅包含了类的版本、接口、字段和方法等信息，还包含了常量池，它用来存放编译时期生成的字面量和符号引用，这些内容会在类加载后存放在方法区的运行时常量池中。运行时常量池可以理解为是类或接口的常量池的运行时表现形式。 

   

3. #### 说一下堆栈的区别？

   （1）栈内存存储的是局部变量而堆内存存储的是实体；

   （2）栈内存的更新速度要快于堆内存，因为局部变量的生命周期很短；

   （3）栈内存存放的变量生命周期一旦结束就会被释放，而堆内存存放的实体会被垃圾回收机制不定时的回   收。

   

4. #### 队列和栈是什么？有什么区别？

   - 队列和栈都是被用来预存储数据的。

   - 队列允许先进先出检索元素，但也有例外的情况，Deque 接口允许从两端检索元素。

   - 栈和队列很相似，但它运行对元素进行后进先出进行检索。

     

5. #### 什么是双亲委派模型？

   在介绍双亲委派模型之前先说下类加载器。对于任意一个类，都需要由加载它的类加载器和这个类本身一同确立在 JVM 中的唯一性，每一个类加载器，都有一个独立的类名称空间。类加载器就是根据指定全限定名称将 class 文件加载到 JVM 内存，然后再转化为 class 对象。

   类加载器分类：

   - 启动类加载器（Bootstrap ClassLoader），核心类加载器。是虚拟机自身的一部分，用来加载Java_HOME/lib/目录中的，或者被 -Xbootclasspath 参数所指定的路径中并且被虚拟机识别的类库；
   - 其他类加载器：
   - 扩展类加载器（Extension ClassLoader）：JRE扩展目录中jar包的加载；lib目录下的ext目录。
   - 应用程序类加载器（Application ClassLoader）。负责加载用户类路径（classpath）上的指定类库，我们可以直接使用这个类加载器。一般情况，如果我们没有自定义类加载器默认就是用这个加载器。

   双亲委派模型：如果一个类加载器收到了类加载的请求，它首先不会自己去加载这个类，而是把这个请求委派给父类加载器去完成，每一层的类加载器都是如此，这样所有的加载请求都会被传送到顶层的启动类加载器中，只有当父加载无法完成加载请求（它的搜索范围中没找到所需的类）时，子加载器才会尝试去加载类。

   （先交给父类加载器去加载，当父类无法完成加载时，交由子类加载）

   

6. #### 说一下类加载的执行过程？

   （1）加载：根据查找路径找到相应的 class 文件然后导入；

   （2）检查：检查加载的 class 文件的正确性；

   （3）准备：给类中的静态变量分配内存空间；

   （4）解析：虚拟机将常量池中的符号引用替换成直接引用的过程。符号引用就理解为一个标示，而**在直接引用直接指向内存中的地址**；

   （5）初始化：对静态变量和静态代码块执行初始化工作。

   

7. #### 怎么判断对象是否可以被回收？

   - **引用计数器：**为每个对象创建一个引用计数，有对象引用时计数器 +1，引用被释放时计数 -1，当计数器为 0 时就可以被回收。它有一个缺点**不能解决循环引用的问题**；

   - **可达性分析：**从 GC Roots 开始向下搜索，搜索所走过的路径称为引用链。当一个对象到 GC Roots 没有任何引用链相连时，则证明此对象是可以被回收的。

     在进行可达性分析后，若其没有连接在GC Roots上时，并不会马上执行gc操作，可能会处于“死缓”状态。针对执行过可达性分析后的对象，要进行判断其是否有必要进行finalize()操作。当对象没有重写finalize()方法和finalize()方法已被调用过，则不需要进行finalize()操作。

8. #### java 中都有哪些引用类型？

   **（1）强引用**

   被强引用关联的对象**不会被回收**。

   使用 new 一个新对象的方式来创建强引用。
   ```

   Object obj = new Object();
   ```

   **（2）软引用**
   
   被软引用关联的对象只有**在内存不够的情况下才会被回收**。
   
   使用 SoftReference 类来创建软引用。
   
   ```
   Object obj = new Object();
   SoftReference<Object> sf = new SoftReference<Object>(obj);
   obj = null;  // 使对象只被软引用关联

   ```
   **（3）弱引用**
   
   被弱引用关联的对象**一定会被回收**，也就是说它只能存活到下一次垃圾回收发生之前。
   
   使用 WeakReference 类来实现弱引用。
   
   
   ```

   Object obj = new Object();
   WeakReference<Object> wf = new WeakReference<Object>(obj);
   obj = null;

   ```
   **（4）虚引用（幽灵引用/幻影引用）**
   
   又称为幽灵引用或者幻影引用。一个对象是否有虚引用的存在， 完全**不会对其生存时间构成影响**，也无法通过虚引用取得一个对象。
   
   为一个对象设置虚引用关联的唯一目的就是能**在这个对象被回收时收到一个系统通知**。
   
   使用 PhantomReference 来实现虚引用。
   
   
   ```

   Object obj = new Object();
   PhantomReference<Object> pf = new PhantomReference<Object>(obj);
   obj = null;
   ```


   ​

9. #### 说一下 jvm 有哪些垃圾回收算法？

   **（1）标记-清除算法**

   标记-清除（Mark-Sweep）算法可以算是最基础的垃圾收集算法，该算法主要分为“标记”和“清除”两个阶段。先标记可以被清除的对象，然后统一回收被标记要清除的对象，这个标记过程采用的就是可达性分析算法。

   标记清除算法最大的缺点是在垃圾回收之后会产生大量的内存碎片，而如果内存碎片多了，当我们再创建一个占用内存比较大的对象时就没有足够的内存来分配，那么这个时候虚拟机就还要再次触发GC来清理内存后来给新的对象分配内存。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86snhptlwj30ew0c5t96.jpg)

   **（2）复制算法**

   为了解决效率问题及标记清除算法的缺点，一种称为“复制”（Copying）的收集算法出现了，它将可用内存按容量划分为大小相等的两块，每次只使用其中一块，当这一块用完了，触发GC操作将存活的对象复制到另一个区域当中，然后再把使用过的内存空间一次清理掉。这样使得每次都对整个半区进行内存回收，内存分配也不用考虑内存碎片的问题，只要移动堆顶指针，按顺序分配内存即可，实现简单，运行高效。

   这种算法最大的缺点是将原有内存分成了两块，每次只能使用区中一块，也就是损失了50%的内存空间，代价有点大。 

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86snmwmczj30fh0cnmxp.jpg)

   **（3）标记-整理算法**

   复制算法在对象存活率较高的情况下需要进行较多的复制操作，这样效率也会变低，更关键的是还需要浪费50%的内存空间，为了解决这些问题，于是“标记-整理”（Mark-Compact）算法就出来了，标记过程仍然使用可达性算法来判断，后续步骤不是直接对可回收对象进行清理，而是让所有存活的对象向一端移动，然后直接清理边界以外的内存。标记-整理算法比较适合年老代的算法实现，至于什么是年老代接下来分带收集算法会讲解。

   ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86snruo7qj30hv09taae.jpg)

   **（4）分代算法**

   当前商业虚拟机的垃圾回收都是采用“分代收集”（Generational Collection）算法，这种算法其实并没有什么新的思想，只是根据对象的存活周期的不同将内存划分为几块。一般把Java堆分为新生代和老年代，然后根据不同年代的特点采用适当的收集算法。例如在新生代，一般情况下每次垃圾收集都会有大量的对象死去，只有少量的存活，这时候一般使用复制算法，而对于年老代，由于对象存活率高，没有额外空间对它跟配担保，因此一般采用“标记-清理”或“标记-整理”算法来实现。

   

10. #### 说一下 jvm 有哪些垃圾回收器？

    **（1）Serial：**最早的单线程串行垃圾回收器

    Serial收集器是最基本、发展历史最悠久的收集器，在jdk1.3.1之前，曾是虚拟机新生代收集的唯一选择。它是一个单线程的收集器，单线程的意思不全是因为它只会使用一个CPU或一条线程去工作，最主要是它在工作的时候，会暂停其他所有的工作线程。想必大家已经能够看出来，这种收集器最大的缺陷就是当收集器在做垃圾回收过程中会让用户工作线程停止掉，这对大多数应用（用户）是很难接受的，例如你的计算机每运行一个小时就暂停响应几分钟。

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86snwmpzjj30kw04qgly.jpg)

    （2）Serial Old：Serial 垃圾回收器的老年版本，同样也是单线程的，可以作为 CMS 垃圾回收器的备选预案

    **（3）ParNew：**是 Serial 的多线程版本。

    ParNew收集器其实就是Serial收集器的多线程版本,除了使用多线程进行垃圾收集外，其他的基本都和Serial收集器一样，包括控制参数、收集算法、Stop The World、对象分配规则、回收策略等。

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86so1cpyuj30ko04k74l.jpg)

    （4）Parallel 和 ParNew 收集器类似是多线程的，但 Parallel 是吞吐量优先的收集器，可以牺牲等待时间换取系统的吞吐量。

    （5）Parallel Old 是 Parallel 老生代版本，Parallel 使用的是复制的内存回收算法，Parallel Old 使用的是标记-整理的内存回收算法。

    **（6）CMS：**一种以获得最短停顿时间为目标的收集器，非常适用 B/S 系统。

    JDK1.5的时候，HotSpot推出了一款认为有划时代意义的垃圾收集器-CMS(Concurrent Mark Sweep)，这个收集器做到了部分动作可以和用户线程同时工作。它是基于标记-清除算法实现的，运作过程相对于前面几种更负责。

    分为4个步骤： 
    初始标记（CMS initial mark）：初始标记只是标记一下GC Roots能直接关联的对象，暂停用户线程

    并发标记（CMS concurrent mark）:并发标记就是GC RootsTracing的过程，可以和用户线程同时执行。

    重新标记（CMS remark）：重新标记是为了修正并发标记期间因为用户线程继续运行而导致标记变化的对象，暂停用户线程。

    并发清除：清理经过重新标记后的对象内存，可以和用户线程同时执行。

    由于耗时最长的并发标记和并发清除过程都可以和用户线程一起执行，所有从整体来说CMS收集器是可以和用户线程一起并发执行的。

    ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g86so6jnwqj30md057aaj.jpg)

    （7）G1：一种兼顾吞吐量和停顿时间的 GC 实现，是 JDK 9 以后的默认 GC 选项。

    

11. #### 详细介绍一下 CMS 垃圾回收器？

    CMS 是英文 Concurrent Mark-Sweep 的简称，是以牺牲吞吐量为代价来获得最短回收停顿时间的垃圾回收器。对于要求服务器响应速度的应用上，这种垃圾回收器非常适合。在启动 JVM 的参数加上“-XX:+UseConcMarkSweepGC”来指定使用 CMS 垃圾回收器。

    CMS 使用的是标记-清除的算法实现的，所以在 gc 的时候回产生大量的内存碎片，当剩余内存不能满足程序运行要求时，系统将会出现 Concurrent Mode Failure，临时 CMS 会采用 Serial Old 回收器进行垃圾清除，此时的性能将会被降低。

    

12. #### 新生代垃圾回收器和老生代垃圾回收器都有哪些？有什么区别？

    - 新生代回收器：Serial、ParNew、Parallel Scavenge
    - 老年代回收器：Serial Old、Parallel Old、CMS
    - 整堆回收器：G1

    新生代垃圾回收器一般采用的是复制算法，复制算法的优点是效率高，缺点是内存利用率低；老年代回收器一般采用的是标记-整理的算法进行垃圾回收。

    

13. #### 简述分代垃圾回收器是怎么工作的？

    分代回收器有两个分区：老生代和新生代，新生代默认的空间占比总空间的 1/3，老生代的默认占比是 2/3。

    新生代使用的是复制算法，新生代里有 3 个分区：Eden、To Survivor、From Survivor，它们的默认占比是 8:1:1，它的执行流程如下：

    - 把 Eden + From Survivor 存活的对象放入 To Survivor 区；
    - 清空 Eden 和 From Survivor 分区；
    - From Survivor 和 To Survivor 分区交换，From Survivor 变 To Survivor，To Survivor 变 From Survivor。

    每次在 From Survivor 到 To Survivor 移动时都存活的对象，年龄就 +1，当年龄到达 15（默认配置是 15）时，升级为老生代。大对象也会直接进入老生代。

    老生代当空间占用到达某个值之后就会触发全局垃圾收回，一般使用标记整理的执行算法。以上这些循环往复就构成了整个分代垃圾回收的整体执行流程。

    

14. #### 说一下 jvm 调优的工具？

    JDK 自带了很多监控工具，都位于 JDK 的 bin 目录下，其中最常用的是 jconsole 和 jvisualvm 这两款视图监控工具。

    - jconsole：用于对 JVM 中的内存、线程和类等进行监控；

    - jvisualvm：JDK 自带的全能分析工具，可以分析：内存快照、线程快照、程序死锁、监控内存的变化、gc 变化等。

      

15. #### 常用的 jvm 调优的参数都有哪些？

    - -Xms2g：初始化推大小为 2g；
    - -Xmx2g：堆最大内存为 2g；
    - -XX:NewRatio=4：设置年轻的和老年代的内存比例为 1:4；
    - -XX:SurvivorRatio=8：设置新生代 Eden 和 Survivor 比例为 8:2；
    - –XX:+UseParNewGC：指定使用 ParNew + Serial Old 垃圾回收器组合；
    - -XX:+UseParallelOldGC：指定使用 ParNew + ParNew Old 垃圾回收器组合；
    - -XX:+UseConcMarkSweepGC：指定使用 CMS + Serial Old 垃圾回收器组合；
    - -XX:+PrintGC：开启打印 gc 信息；
    - -XX:+PrintGCDetails：打印 gc 详细信息。



