---
layout: post
title: "Vue基础知识"
tags: Vue
author: Shenpotato
catalog: true
---



> 《前端基础必会教程-4 小时带你快速入门 vue》（https://www.bilibili.com/video/BV12J411m7MG?p=31）学习笔记
>
> 代码地址：https://github.com/Shenpotato/vuebasic



### 一、vue基础

Vue官网地址：https://cn.vuejs.org/

**使用时需导入：** <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

由于Vue是javascript的框架，因此，它遵循其语法规则。

El：在<script>中绑定某个<div>的工具。可以通过id绑定，类绑定，标签绑定。

data：类似于编程语言中的变量。包含数组，key-value等对应形式。html中可以**通过{{varaiableName}}访问**。

function：当进行某种操作时，需要调用的方法。在其中实现逻辑判断。**通过this访问定义的变量**。

```html
<div id ="app1">
  {{name}}
  <p>
    {{school.name}}
  </p>
  <p>
    {{relativs[0]}}
  </p>
</div>
<div class="app2"></div>
<p><p>
```



```javascript
<script>
	var app = new Vue({
		el: "#app1",			//id绑定
		//el: ".app2",			//类绑定
		//el: "p",					//标签绑定
    data:{
      name: "shenpotato",
      school:{
        name: "central south university",
        location: "ChangSha"
      },
      relatives:["shentomato","sheneggplant","shenwatermalon"]
    },
    functionExample1:function(param1,param2,...){
      
    }
	})
<script>
```



### 二、本地应用

#### 1. v-text

作用：输出数据。message和info都是Vue中定义的变量。

```html
<p v-text="message">深圳</p>
<p v-text="info">深圳</p>
<p>{{message + "!"}}深圳</p>
```



#### 2. v-html

作用：输出数据（保留html格式）

```html
<!-- v-html 保留html格式  -->
<p v-test="content"></p>
<p v-html="content"></p>

Vue:
content: "<a href='http://www.baidu.com'>百度网址</a>",
```



#### 3. v-on

作用：绑定事件。@click，@dblclick都是简写，分别代表点击和双击触发的事件。与Vue中定义的函数绑定。

```html
<input type="button" value="事件绑定" v-on:click="doIt" />
<input type="button" value="v-on简写" @click="doIt" />
<input type="button" value="双击事件" @dblclick="doIt" />
```



#### 4. v-show

作用：根据表达式真假切换元素的显示状态，通过修改元素的dispaly实现掩藏显示

```html
<h2>v-show：根据表达式真假切换元素的显示状态</h2>
<input type="button" value="切换显示状态" @click="changeStatus" />
<img v-show="isShow" src="img/cat.jpg" alt="" />
<p></p>
<p>现在的年龄：{{age}}，当年龄大于18时，显示图片</p>
<input type="button" value="添加年龄" @click="addAge" />
<img v-show="age>18" src="img/cat.jpg" alt="" />
```



#### 5. v-if

作用：根据表达式真假切换元素的显示。

```html
<input type="button" value="切换标签状态" @click="changeTagStatus" />
<p v-if="isTagShow">我是一个标签</p>
<p v-if="temperature>35">温度过高</p>
```

**与v-show的区别**

v-if是对标签进行操作，false时标签在dom树消失
v-show标签仍然存在于dom树



#### 6.v-bind

作用：设置元素的属性。其中imgSrc是定义在Vue中data的一个变量。

```html
<h2>v-bind设置元素的属性</h2>
<img v-bind:src="imgSrc" />
```



#### 7. v-for

作用：根据数据生成列表结构

````html
<h2>v-for：根据数据生成列表结构</h2>
<ul>
  <li v-for="(item, index) in arr">
      方位：{{item}} + {{index}}
  </li>
</ul>
````



#### 8. v-model

作用：将表单元素的之与Vue中data数据双向绑定。

```html
<h2>v-model 获取和设置表单元素的值</h2>
<input type="text" v-model="message" @keyup.enter="getMessage" />
<b v-text="message"></b>
<input type="button" @click="setMessage" value="改变message"></input>
```



### 三、网络应用

通过axios实现访问接口。

首先需要引入axios的script依赖：    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

axios通过get和post请求获取内容的方法。

```javascript
axios.get(url?key=value&key2=values).then(function(response){},function(err){})

axios.post(url,{key:value,key2:values}).then(function(response){},function(err){})
```

post实例：

```javascript
document.querySelector(".get").onclick = function () {
  .get("https://autumnfish.cn/api/reg", { username: "shenpotato" }).then(
    function (response) {
      console.log(response);
    },
    function (err) {
      console.log(err);
    }
  );
};
```

get实例：

```javascript
getJoke: function () {
  var that = this;
  axios.get("https://autumnfish.cn/api/joke").then(
    function (response) {
      that.joke = response.data;
    },
    function (err) {
      console.log(err);
    }
  );
},
```

**注意：我们需要定义that指向this，因为在axios中，this指向会发生变化。**



### 四、Vue的生命周期

Vue一共有10个生命周期函数，我们可以利用这些函数在vue的每个阶段都进行操作数据或者改变内容

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1gidu5dre4gj30u023zgpr.jpg" style="zoom: 67%;" />



