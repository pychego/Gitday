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

事件的三要素：事件源、事件类型、事件处理程序

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
element。innerHTML = '新的元素内容'; //' '里面识别html标签，保留空格和换行
//修改元素属性
element.src = ...
element.title = ...
```

**重要！！！**：**表单（input标签）**里面的值、文字内容是通过value来修改的；`input.value.length` 是表单的长度

表单事件获得焦点：`onfocus`  失去焦点：`onblur`

input标签有个checked（选中）属性，`checked = 'checked'`

要禁用按钮：btn.disable = true

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

自定义属性在tab栏切换很有用

H5规定自定义属性以`data-`开头，比如自定义属性`data-index`,获取属性，element.dataset.index



### 利用节点层级关系获取元素（父子兄弟）

网友中所有内容都是节点

节点的重要属性：nodeType、nodeName、nodeValue；其中nodeType的值，元素节点为1，属性节点为2，文本节点为3

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















