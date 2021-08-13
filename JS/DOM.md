BOM的根本对象是window；DOM的根本对象是document，即window.document

以下全部是获取文档element对象的方法

1. ID     2. 标签名     3. H5方法      4. 特殊元素

```javascript
document.getElementById(id)    //id是大小写敏感的String
//script标签要写到要获取的标签后面，返回的是DOM element对象
console.dir()     //打印返回的元素对象
/*==========标签名获取子元素==========*/
element.getElemntsByTagName()   //返回指定标签的集合，参数为"li"或"div"这类，伪数组，得到的元素是动态的
//当仅有一个元素时，返回还是伪数组；没有元素时，返回空伪数组
element.getElementsByClassName()  //根据类名获取元素集合，同上
document.querySelector('css选择器')   //返回指定选择器的第一个元素对象
document.querySelsctorAll('css选择器')  // ～所有～     document可以换成其他元素对象
/*==========特殊元素获取body，html==========*/
document.body    //获取body
document.documentElement   //获取html元素对象
```

## 事件：触发--响应机制

​	事件的三要素：事件源、事件类型、事件处理程序

```javascript
//一个例子
btn.onclick = function() {
  //事件处理
};   //在函数内this指向函数的调用者（btn）
```

**执行事件**：1、获取事件源    2、绑定(注册)事件    3、添加事件处理function

**改变元素属性和内容**：

```javascript
//操作普通盒子，这两个是可读写的属性
element.innerText = '新的元素内容';  //这个' '里面不识别html标签，去除空格和换行
element.innerHTML = '新的元素内容'; //' '里面识别html标签，保留空格和换行
//修改元素属性
element.src = ...
element.title = ...
```

**重要！！！**：**表单（input标签）**里面的值、文字内容是通过value来修改的；`input.value.length` 是表单的长度

表单事件获得焦点：`onfocus`  失去焦点：`onblur`

input标签有个checked（选中）属性，`checked = 'checked'`

要禁用按钮：btn.disabled = true



### 样式属性操作

1. `element.style. ....`  适用于样式少的修改，下面还有很多属性操作，采用驼峰命名法；比如，

   ```javascript
   this.style.backgroundColor = 'purple';  //JS修改样式是行内样式，权重高于css
   display: none;  隐藏元素
   display: block; 显示元素
   ```

2. `element.className = '类名'`，赋值将当前元素类名改为指定值，适合于修改样式较多。但是会覆盖原来的类名

   若要保存原来的类名，`element.className = '原类名 新类名'`， 这属于多类名选择器



**排他思想**：给所有元素清除样式，再给当前元素添加样式

注册事件之后，程序往下执行事件也能一直起作用（只管把工具拿出来，但是不管收起来）；事件一旦注册，就可以被多次触发。举个例子，

```
鼠标经过：onmouseover； 离开：onmouseout，如果要鼠标离开之后效果消失，还要注册鼠标离开事件
```



### 获取属性值

```javascript
element.属性     //用于获取内置属性（id、class等），可变属性可直接赋值修改
//特殊地。属性若为class，要写成 element.className
/*================*/
element.getAttribute('属性')    //获取自定义属性
element.setAttribute('属性', '值')
element.removeAttribute('属性')  //移除
```

### tab栏切换 pink B站 P224

​	自定义属性在tab栏切换很有用

​	H5规定自定义属性以`data-`开头，比如自定义属性`data-index`,获取属性，element.dataset.index



### 利用节点层级关系获取元素（父子兄弟）

网友中所有内容都是节点

​	节点的重要属性：nodeType、nodeName、nodeValue；其中nodeType的值，元素节点为1，属性节点为2，文本节点为3

```javascript
// 获取父节点
node.parentNode.   //得到的是最近的父亲，（亲爸爸），找不到返回null
//获取子节点
node.childNodes     //得到所有的子节点，包括文本节点，因此这个方法用处不大
node.children       //获取所有的子元素节点，常用
node.firstNode      //获取第一个子节点，包括文本节点
node.lastNode
node.firstElementNode. //第一个子元素节点
node.lastElementNode
node.children[node.children.length - 1]   //两个都选择最后一个子元素节点
//获取兄弟节点（用的不多）
node.nextSibling    //获取包括文本节点在内的下一个兄弟节点
node.previousSibling
node.nextElementSibling
node.previouselementSibling
```

### 动态操作节点

​	创建节点之后还要添加才可以

```javascript
document.createElement('ul');
node.appendChild(child);    //node是父亲， child是儿子;添加到末尾
node.insertBefore(new_child, old_child);
node.removeChild(child);    //删除节点
node.cloneNode()        //无参数表示浅复制，只复制标签没有内容。参数为true表示深复制，克隆之后要添加才能使用

```

------



## 事件高级

### 注册事件

​	注册事件有唯一性，后注册的事件会覆盖先前注册的

1. 第一种注册方法前面学过，on开头的...

2. 监听注册方式（同一事件可以添加多个监听器[即事件处理程序]）使用`addEventListener`

   ```javascript
   eventTarget.addEventListener(type, lister[, useCapture]);
   //该方法将指定的监听器注册到eventTarget
   /* type:事件类型字符串，注意加引号，并且没有on
      lister：事件处理函数（监听函数）
      useCapture: true为捕获阶段，false为冒泡阶段
    */
   ```

3. `attachEvent()` ie9之前的，不常用

### 解绑事件

​	在事件执行特定次数后不再执行

1. 传统解绑：`element.onclick = null;`

2. 监听注册解绑，例子

   ```javascript
   element.addEventListener('click', fn);
   function fn() {
   	alert(1);
   	element.removeEventListener('click', fn);
   }  // 事件触发一次就解绑
   ```

3. attachEvent() 对应 detachEvent(). 使用方法和上面的那个一样

### DOM事件流

​	三个阶段： 

1. **捕获阶段** 从大到小，从内到外

   比如，father（大盒子）和son（大盒子里面的小盒子）都注册相同事件，先执行father事件，后执行son

2. **冒泡阶段** 和捕获阶段相反， 冒泡事件用处更多

3. 当前目标阶段



### 事件对象

​	事件对象是侦听函数的形参，一般写作e或者event，是事件一系列相关数据的集合，有很多方法和属性；事件对象依靠事件存在

```javascript
e.target;   //返回触发事件的元素（即我们点击的那个对象）
//this返回的是绑定事件的对象元素
e.type;     // 事件类型
e.preventDefault();   // 阻止默认事件（使链接不跳转等）
e.stopPropagation();    // 阻止事件冒泡
e.clientX;           //返回鼠标在可视区的x坐标，同理得到y
e.pageX;             // 返回页面文档的x坐标
e.screenX;           // ~相对于电脑屏幕～
```

### 事件委托（代理、委派）

​	原理：不给每个子节点单独设置事件监听器，而是事件监听器设置在其父节点上，利用冒泡原理影响设置每个子节点。

​	优势：只需操作一次DOM

### 常用内容

​	contextmenu 右键菜单

1. 禁止右键菜单

   ```javascript
   document.addEventListener('contextmenu', 
   	function(e) {
   	e.preventDefault;
   	}
   );
   ```

2. 禁止选中文字  `selectstart`

### 键盘事件及事件对象

- `onkeyup`  键盘弹起触发
- `onkeydown` 按下触发，识别功能键
- `onkeypress`  按下触发，但是不识别功能键shift, ctrl 等

这三个事件的执行顺序2， 3， 1

​	键盘事件对象与鼠标事件对象类似

```javascript
e.keycode;    // 相应键的ascii码
//keyup和keydown事件不区分大小写，a和A都是65；keypress区别大小写
e.focus();    // input对象获得焦点
//down和press两个事件触发时，文字还没落入文本框，up字先落入文本框才触发事件
```



## 实用技巧

阻止链接跳转。 `href='javascript:;'`

left、top加px；

