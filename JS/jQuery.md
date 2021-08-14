页面DOM加载完成执行JS代码(相当于原生JS的DOMContentLoaded)

```javascript
$(document).ready(function(){
	
})   // 或者
$(function(){

})
```

jQuery的顶级对象`$`, 即`jQuery`,两种可以互换

可以把元素包装成`jQuery`，调用其方法。

与DOM的区别：

- DOM是通过原生JS获取的对象；用`$`获取的是`jQuery`对象
- 两者只能用各自的方法

jQuery -> DOM  

​	`$('div')[index]` 或 `$('div').get(index)`

DOM -> jQuery

​	$(DOM对象) 或  $('CSS选择器')

**隐式迭代**：jQuery可以直接为数组的所有元素改样式（遍历伪数组内部元素，执行相应方法）

`$('div').css('样式', '值'). 省去了for循环

jQuery**筛选方法**

```javascript
.parent()   // 返回亲爸爸
.chileren(selector)   // 返回亲儿子
.find(selector)      //  返沪里面所有满足条件的后代
.siblings(selector)    // 返回所有满足条件的兄弟，不包含自己
.nextAll()
.prevAll()
```

​	选择数组里面的第n个（索引从0开始）、

- `$('ul li: eq(n)')`
-  `.eq(n)`

**事件**

```
$('').mouseover(function(){
	$(this).hide()  // 隐藏这个元素
	$(this).show() 
})
```

