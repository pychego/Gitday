	BOM	浏览器对象模型，顶级对象是window；BOM包含DOM

定义在全局作用域的变量和方法自动变成window对象的属性和方法；window下有一特殊属性window.name。不要拿name作为变量名

### 窗口加载

1. `window.onload = function(){};`页面加载完毕才执行函数，这个事件传统注册方式只能注册一次addEventListener可以多次

2. `DOMContextLoaded`事件，仅当DOM加载完成（不包括图片，flash，CSS等）就执行事件

3. `load`事件需要等这些元素全加载完毕才执行

   调整窗口大小事件 `resize`,窗口大小发生变化可以触发这个事件

   `window.innerWidth` 当前屏幕宽度

### 定时器

1. `window.setTimeout(回调函数[,延迟ms数])`

   window可省略，如果省略时间，立即执行回调函数；回调函数可以写函数名，也可以用匿名函数

   定时器经常赋值给变量，以区分不同的定时器

   **停止定时器**：window.clearTimeout(定时器变量名)

2. `window.setInterval()` 两者参数形同，该方法反复调用，每隔一段时间调用一次

   **停止定时器**：clearInterval()

**this指向问题**

​	一般this的最终指向是调用它的对象

- 全局作用域或者普通函数中的this指向window，特别的，定时器回调函数中的this指向window，因为js定时器方法都是在window下的
- 方法调用中的this指向调用方法的对象
- 构造函数中的this指向构造函数的实例，类似python的self

### JS执行机制

1. 先执行**执行栈**中的同步任务

2. 异步任务（回调函数）放入任务队列

3. 同步任务执行结束之后会按照次序读取任务队列中的异步任务

   **事件循环**

### 常用的对象属性和方法

**location对象**

```javascript
.href     // 获取整个网页url
.host     // 返回域名
.search   //返回url参数
.assign() //不懂
.replace()
.reload()
```

**navigator对象**（导航）

包含有关浏览器信息，其中最知道的一个属性`.userAgent`

**history对象**

```javascript
.back()   // 相当于浏览器的默认后退箭头
.forward()
.go(参数)    //参数为1，前进一个页面；为-1，倒退一个页面
```

