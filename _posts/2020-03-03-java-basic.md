---
layout: post
title:  "java基础知识散记"
tags: Java
author: Shenpotato
catalog: true
---



> 性能优化内容来自：https://www.cnblogs.com/chinafine/articles/1787118.html



1、数据类型转换

(1)string 与 int

```java
String s = '123';
int a = Integer.parseInt(s);

int a = 1234;
string s1 = a.toString();
```



(2)char 与int

```java
char a = '1';
int a = Character.character.getnumericvalue(a);
```



2、导入包的不同

```java
import org.junit.jupiter.api.Assertions;								//导入类

import static org.junit.jupiter.api.Assertions.*;				//导入类的静态方法
```

import static 可以省略类名，比如Assertions.assertEquals()中的Assertions，System.out.println()的System。

在要多次使用某一个类中的静态方法时，可以使用import static。但是要防止导入不同类时的冲突。如导入Integer类和Double类时，都定义了MAX_VALUE。



3、不使用 a % 2 == 1来判断是否为奇数，当a为负奇数时不成立

```java
(a % 2 == 0)				//判断是否为偶数
((a & 1) == 1)			//判断是否为奇数
```



### 二、性能优化

1. 避免在循环中使用复杂表达式

   ```java
   size = vector.size();
   for(int i = 0; i < size; i++){}
   ```

2. 如果已知容器所使用的空间大小，为容器定义初始大小

   ```java
   public Hashtable hashtable = new Hashtable(10);
   ```

3. 在finally块中关闭stream

```java
public void method () {
        try {
            fileinputstream fis = new fileinputstream ("cs.java");
            int count = 0;
            while (fis.read () != -1)
                count++;
            system.out.println (count);
            fis.close ();
        } catch (filenotfoundexception e1) {
        } finally{
        	fis.close();
     }
}
```

4. 使用system.arraycopy()代替循环复制数组

5. 访问实例内变量的getter/setter方法变成”final”

   ```java
   class daf_fixed {
       final public void setsize (int size) {
            _size = size;
       }
       private int _size;
   }
   ```

6. 避免不必要的instanceof操作和类型转换

7. 使用移位操作代替除号

   ```java
   int quotient1 = a >> 2;				// equals to a / 2
   int quotient2 = a >> 3; 			// euqals to a / 4
   int quotient3 = a / 3;				// 无法用移位操作完成
   ```

8. 字符串相加时，若一字符串只有一个字符，用' '

   ```java
   String str1 = "abc";
   String str2 = str1 + 'd';
   ```

9. 循环中

   - 不调用synchronized同步方法

     ```java
     public class syn {
         public synchronized void method (object o) {
         }
         private void test () {
             for (int i = 0; i < vector.size(); i++) {
                 method (vector.elementat(i));    // violation
             }
         }
         private vector vector = new vector (5, 5);
     }
     
     public class syn {
         public void method (object o) {
         }
     private void test () {
         synchronized{//在一个同步块中执行非同步方法
                 for (int i = 0; i < vector.size(); i++) {
                     method (vector.elementat(i));   
                 }
             }
         }
         private vector vector = new vector (5, 5);
     }
     ```

   - 将try/catch移出循环

     ```java
     public class try {
         void method (fileinputstream fis) {
             for (int i = 0; i < size; i++) {
                 try {                                      // violation
                     _sum += fis.read();
                 } catch (exception e) {}
             }
         }
         private int _sum;
     }
     
      void method (fileinputstream fis) {
             try {
                 for (int i = 0; i < size; i++) {
                     _sum += fis.read();
                 }
             } catch (exception e) {}
         }
     }
     ```

   - 不在循环中实例化变量

10. 对于boolean值，不要出现boolean == true这种判断

11. 使用条件操作符替代可以替代的if...else



### 三、容器使用

#### 1、PriorityQueue

https://blog.csdn.net/u010623927/article/details/87179364

底层维护一个表示二叉搜索树的数组。包含了

- 添加元素：add()，失败抛出异常；offer()，返回false
- 堆顶元素：element()，失败抛出异常；peek()，返回false
- 删除堆顶元素：remove()，失败抛出异常；poll()，返回null
- 删除指定元素：remove(Object o)；

PriorityQueue是一个线程不安全的集合类，PriorityBlockingQueue为PriorityQueue加上了ReentrantLock锁，实现了线程安全。

自定义类使用PriorityQueue时，需要实现比较器。

扩容的代码

```java
int newCapacity = oldCapacity + ((oldCapacity < 64) ?
                                 (oldCapacity + 2) :
                                 (oldCapacity >> 1));
```

降序实现代码：

```java
PriorityQueue<Integer> priorityQueue = new PriorityQueu((o1,o2) -> o2 - o1);
```

实现toArray()方法，转换为数组。



#### 2、HashMap