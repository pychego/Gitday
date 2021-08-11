## JavaScript特性

JavaScript由ECMAScript、DOM、BOM组成

JavaScript是解释型语言，解释器解释一句，执行一句



​	

## 快速入门

### 基本语法

js很多语法类似C语言

注释

```javascript
// 这是单行注释
/*这是
多行注释*/
```



### 数据类型和变量

#### 基本数据类型

Number、Boolean、String、Undefined、Null对应的默认值分别是0、false、""、undefined（未定义）、null（空值）

八进制：数字前面加0表示八进制数

十六进制：数字前面加0x

Number.MAX_VALUE和Number.MIN_VALUE分别表示最大值和最小值

常量  Infinity 无穷大   NaN 非数值  

iaNaN() 判断是不是NaN

##### String

转义符和C语言基本一样

length属性：str.length

字符串拼接特性：字符串 + `任何类型` = 新字符串

##### Boolean

包含true和false，参与加法运算时，分别看作1和0

##### Undefined

未定义数据类型

`typeof`用于获取数据类型，是关键字

#### 数据类型转换

1. to字符串
   - ele.toString()方法
   - String() 强制转换
2. to数字型
   - parseInt(string) 向下取整
   - parseFloat(string)
   - Number() 强制转换  
3. 利用-、*、/隐式转换。'12' - 0 === 12
4. to布尔值：Boolean()函数，代表空、否定的值转换为false，其余全为true

#### 运算符 operator

算数运算符：+、-、*、/、%(取余)，，，浮点数有精度问题。不能直接判断两个浮点数相等

递增/减：必须配合变量使用，与C语言相同

```javascript
e = 10;
b = e++ + ++e;   //b === 22
```

比较运算符：<、>、>=、<=、==（会转变数据类型）

=== （全等）、值和数据类型均相等

逻辑运算符：不一定返回布尔值

&&：若表达式1为真，则返回表达式2；若表达式1为假，则返回表达式1.

||：表达式1为真，则返回表达式1；表达式1为假，返回表达式2.

！

```javascript
b = 123 && 456; // b === 123
```

**短路运算**：（逻辑中断）当有多个表达式时，如果左侧表达式可以确定结果，就不再判断后面表达式

赋值运算符：`+=`、`-=`、`*=`、`/=`、`%=`

**优先级**：（）> 一元运算符 > 算术运算符 > 关系运算符 > 相等运算符 > 逻辑运算符 > 赋值运算符  > 逗号运算符

&& 优先级高于||



### 字符串对象

String、Number、Boolen属于基本包装类型：把简单数据类型包装成复杂数据类型。比如，让String变量拥有了length属性

**简单类型和复杂类型（引用类型）**：

特殊地，null返回一个空对象object

**栈**：存放简单类型，存放的是值

**堆**：复杂类型在栈里存放地址，该地址指向堆的对象，真正的对象实例在堆中

简单类型传参：把实参的值复制一份给形参

复杂类型传参；其实在栈中也是复制了地址值给形参，但因两地址相同，因而形参和实参指向同一对象。整体传参和python类似（传入了引用的副本，两根鱼线钓到同一条鱼）

字符串不可变，字符串的重新赋值会开辟新空间，原地址并未释放。字符串的所有方法都不改变字符串本身，而是返回新字符串

```javascript
String.indexOf();  //参数1:要查找的字符， 可选参数2:起始查找位置
String.lastIndexOf(); 
/*上面两个方法根据字符返回索引， 下面的方法根据索引返回字符*/
String.charAt(index);
String.charCodeAt(index) ; //返回对应字符ASCII值，可以用来判断按下哪个键
str[index]     //等同String.charAt(index);
```

统计字符串中出现最多的字符：遍历每一字符，作为对象的键，若新对象无该属性，则赋值为1，否则++

```javascript
.concat(str1, str2, ...)   //等效于+
.substr(start, length)     //截取字符串
.replace('原字符', '新字符')  //只替换第一个
```

字符串--> 数组：`str.split('分隔符')` 这个用法基本和python一样（分隔符在数组中不存在）

### 数组

创建方式

- `var arr = new Array();`
- 数组字面量：`var arr = [1, 2, 3];`//可以放任何类型混合
- 访问元素从0开始，超过索引范围时返回`undefined`

数组的长度：`arr.length`

检测是否为数组： 1. `instance of` 运算符.   2. `Array.isArray()`

数组增加长度：可以手动修改`arr.length`，新增的元素为`undefined`

```javascript
var arr = new Array(); // 数组长度为2
var arr1 = new Array(2, 3)； //即 arr1 = [2, 3]
```

`.push()` 在数组末尾添加一个活多个数组元素，参数直接写数组元素

`.unshift()` 头部插入，用法同`.push()`

`.pop()` 删除数组的最后一个元素，返回值是删除的元素，直接修改数组

`.shift()` 删除数组的第一个元素

`.reverse()`    

`.sort()` 默认排序顺序是在将元素转换为字符串，然后比较它们的UTF-16代码单元值序列时构建的

数组索引方法：

```javascript
arr.indexOf();  // 返回第一个满足田间的索引，未找到返回-1
arr.lastIndexOF();  //从后面开始查找
```

数组去重方法：遍历旧数组，对于一个元素，如果新数组没有这个元素，就加入新数组。

数组转换为字符串：

- `.toString()`
- `arr.join(分隔符)`
- `concat()` 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。
- `slice()` 方法返回一个新的数组对象，这一对象是一个由 `begin` 和 `end` 决定的原数组的**浅拷贝**（包括 `begin`，不包括`end`）。原始数组不会被改变。
- `splice()`这个方法非常完备

### 对象

### 条件判断

和C语言相同

```javascript
if (expression1) {
	//	执行语句
} else if (expression2) {
	
} else {

}
```

```javascript
条件表达式 ? expression1 : expression2
```

```javascript
switch (expression) {
	case value1:
	//执行语句
	break;
	
	case value2:
	//执行语句
	break;
	
	default: 
	//都不匹配时执行
}
//表达式和value相匹配必须是全等才行
```

### 循环

三个循环语句`for`、`while`、`do while`用法和C语言完全一样

continue：用于跳出本次循环，进行下一次循环

break：跳出循环，执行循环下面的语句

```javascript
for (变量 in 对象)
{
    在此执行代码
}  //用于遍历对象的属性和方法
```



## 函数

```javascript
function name(参数 1, 参数 2, 参数 3) {
    //要执行的代码
}
```

实参数目多于形参：会忽略掉多余实参

实参数目少于形参：则形参被看作是不用声明的变量（是一个变量，但是没赋值，为undefined）；多余的参数定义为undefined，形参的默认值是undefined

数字 + undefined 得 NaN

`返回值`：同样是return，只能返回一个值，若有多个值用逗号隔开，返回最后一个值

函数没有return语句则返回undefined

`arguments`是当前函数的一个内置对象，其中存放l传递的所有实参，是一个伪数组，只有函数有arguments对象，每个函数都内置好了。利用该参数可以方便求出传入参数的最大值

`伪数组`：具有length属性、按照索引方式储存、没有真正数组的一些方法

函数可以调用另一个参数

**声明方式：**

- 命名函数：function关键字

- 匿名函数：即函数表达式

  ```javascript
  var name = function() {};
  ```

- 箭头函数： 待补充

**作用域**：

- 全局作用域：在整个script标签或者一个文件起作用
- 局部作用域：只在函数内部起作用
- js有没有块作用域？？？？？es6新增了块作用域

变量分为全局变量和局部变量

局部变量：var在函数内部声明的是局部变量；函数的形参也是局部变量；**函数内未声明直接赋值的是全局变量**

**作用域链**：内部函数访问外部变量，链式查找（就近原则）。方法：站在目标出发，一层一层往外查找，找到变量声明、变量初始化、变量赋值三者之一就停止

**预解析：**js引擎运行js，先进行预解析再执行代码

js引擎会把js里面的所有var声明和function提升到当前作用域的最前面

- 变量提升：把所有的变量声明提升到当前作用域的最前面，**不提升赋值**，包括匿名函数
- 函数提升：把函数提升到当前作用域的最前面，不调用函数（类似C语言）

```javascript
fun();
var fun = function() {

};   // 相当于
var fun;
fun();
fun = function() {

};  
//变量提升从最外层开始一层一层提升，看到代码先预解析
```

```javascript
var a = b = c = 9;  //相当于
var a = 9; b = 9; c = 9;

var a = 9, b = 9, c = 9; //集体声明，相当于
var a = 9;
var b = 9;
var c = 9;
```





## 标准对象

js对象是一组无序的相关属性和方法的集合。万物皆对象。字符串、数值、数组、函数...

**创建对象**：

- 字面量

  ```javascript
  var obj = {
    uname: '张三丰',
    age: 18,
    sayHi: function() {
      
    }
  };   //和python不同，python键需要引号
  ```

  调用属性的两种方法 `obj.uname`、 `obj['uname']`

- `new Object()`创建

  ```javascript
  var obj = new Object();
  obj.name = '张三丰'；
  obj.sayHi = function() {};
  ```

- 构造函数：里面封装的是对象，把对象里面一些相同的属性和方法抽象出来封装到函数里面。**具体怎么操作？？？？？？**

  ```javascript
  function 构造函数名(){
  	this.属性 = 值;
  	this.方法 = function() {
  	
  	};
  }  //构造函数名称首字母大写
  ```

  调用方法：`new 构造函数名()`

  - 构造函数不用return 返回就能返回对象；构造函数必须使用new；属性、方法前面必须加this
  - 构造函数类似python的class

### 内置对象

JS对象包括自定义对象、内置对象、浏览器对象

**Math对象**：不是构造函数，不需要用new调用

```javascript
Math.abs();
Math.max();
Math.floor();  //向下取整
Math.ceil();  //向上取整
Math.round();  //四舍五入，特殊地，.5往大的取。 -1.5 --> -1
Math.random(); // [0, 1)
```

**日期对象**：Date是一个构造函数，必须用new调用

```javascript
//date 几号；   day 星期几
var data1 = new Date()  //返回自1970年到现在的总毫秒数
//做倒计时效果，用将来的时间戳-现在的时间戳
```



