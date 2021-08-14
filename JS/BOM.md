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

**offset系列**

```javascript
element.offsetTop.   // 返回以带有定位的父亲为准，否则以body为准；返回值都不带单位
element.offsetLeft.  
element.offsetWidth. // 返回元素宽度是 padding + border + width
element.offsetParent. // 返回带有定位的父亲
```

offset和style属性的区别

- offset获得任何样式大小，得到的值只读，不可赋值；
- style仅可得到行内样式表的样式，可读写

**client元素可视区**

```javascript
element.clientWidth. // 不包含边框，包含padding
element.clientTop    // 返回元素上边框
element.clienyHeight 
```

**立即执行函数**

​	不用调用，立即执行；创建了独立的一个作用域；两种写法

- `(function () {})()`  最后的括号写实参
- `(function () {} ())`

**元素滚动系列**

```
element.scrollTop    // 元素被卷去的头部
scroll   // 滚动条变化触发事件
window.pageYOffset.  // 页面被卷去的头部
```

**动画原理**

​	定时器不断移动盒子位置，盒子必有定位，给不同的元素指定不同的定时器

 缓动动画原理：

​	`step = (目标值 - 当前值) / 10`

​	`step = step > 0 ? Math.ceil(step) : Math.floor(step) ;



## 移动端

**触屏事件**

​	`touchstart`  开始触摸

​	`touchmove`  在DOM元素上移动

​	`touchend`    手指离开

**触摸事件对象 e**

```javascript
e.touches   // 获取所有的触摸点（正在触摸）
e.targetTiuches
e.changedTouches
```









