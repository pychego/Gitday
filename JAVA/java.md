## 注释、标识符、关键字

### 注释

一定要写注释！！！

- 单行注释： `// 单行注释`
- 多行注释： `/* 多行注释 */`
- 文档注释：JavaDoc  `/** */`  

### 标识符

	关键字如下表

<img src="/Users/chegopy/Library/Application Support/typora-user-images/image-20210817205130621.png" alt="image-20210817205130621" style="zoom: 67%;" />

	标识符必须以字母、$、下划线开头，Java是大小写敏感的，可以使用中文命名变量，但是强烈建议不要这么干！！！

---

## 数据类型

Java数据类型包括基本类型和引用类型

###  primitive基本类型

- byte  占一个字节，范围-128 ～ 127
- short 两个字节， 范围 -32768 ～ 32767
- int 占四个字节
- long 占八个字节，long类型要在数字后面加L
- float 占四个字节，float类型需要在数字后面加上F
- double 占8个字节，浮点类型常用double
- char 占两个字节
- boolean **占一个位（bit）**

只有这八种是基本类型，其他全部是引用类型；二进制数以0b开头， 八进制以0开头，十六进制以0x开头

1G  = 1024MB

1 MB = 1024KB

1 KB = 1024 Byte

1 Byte = 8 bit

### **引用类型**

对于任意一个Java虚拟机来说，所有的对象引用都具有相同的大小，而不管它实际上所引用的对象大小

String 属于引用类型，`String`不是关键字

格式化字符串方法: `String.format()`, 使用时翻文档看用法，可以把这个函数当作C语言的`printf()`，足够用了,只是这个函数返回字符串，不会输出

```java
Date today = new Date();
String.format("%tA, %<tB %<tC", today); // < 表示重复使用前面使用过的参数
```



> 浮点数 

```java
float f = 0.1f;     
double d = 1.0 / 10;
System.out.println(f == d);   // false
float a = 2345467889f;
double b = a + 1;
System.out.println(a == b);   // true
```

浮点数有限 舍入误差 离散 大约 接近但不等于；避免使用浮点数进行比较

所有的字符本身都是数字， Unicode编码 每个占2字节， 

```java
String sa = new String("hello, world");
String sb = new String("hello, world");
System.out.println(sa == sb);    // false

String sc = "hello, world";
String sd = "hello, world";
System.out.println(sc == sd);    // true 
```

**boolen**

java 中**integer 和 boolean不相容**，不能用integer做条件测试，并且逻辑运算符的操作数必须是boolen；

还会有短路运算, 同理，三元运算符的问号前面必须是boolen类型，不能是int类型

### 类型转换

​	八种基本类型等级从低到高：byte, short, char -> int -> long -> float -> double(浮点数高于)

`Integer.parseInt("3") ` 将String转换为int

- 强制转换 ： `（类型）变量名`   从高到低转换
- 自动转换：  （隐含展开）`implicit widening` 这是从低到高；比如char转换为int

注意点：

1. 不能对布尔值进行转换，因为boolen占一个位（bit）
2. 不能把对象类型转换为不相干的类型
3. 在高容量转换为低容量时，需要强制转换
4. 转换可能会有内存溢出、精度损失 

```java
int money = 10_0000_0000;
int years = 20;
int total = money * years;
long total2 = money * years;  // 两个int的相乘默认是int，转换之前就有问题了
long total3 = money * (long)years; 
System.out.println(total);  // -1474836480
System.out.println(total2); // -1474836480
System.out.println(total3); // 20000000000
```

### 变量

#### 变量作用域

**局部变量**：作用域在两个{}之间

**实例变量**：从属于对象，如果不自行初始化，会使用该类型的默认值，一般的是0  0.0；布尔默认值false；除了基本类型其余默认值都是null

**类变量**：从属于所在的类，需要加static关键字

#### 常量

​	常量必须使用`final`修饰符，static也是修饰符，修饰符的顺序无所谓

```java
static final double PI = 3.14;
```



### 运算符

- 算数运算符：`+`、`-`、`*`、`/`、%、`++`、--
- 赋值运算符：`=`、+=、`-=`、*=、`\=`
- 关系运算符：`<`、`>`、`>=`、`<=`、==、`!=`、`instanceof`
- 逻辑运算符：`&&`、`||`、!
- 位运算符：`&`、`|`、`^`、`~`、`>>`、`<<`、`>>>`
- 三目运算符： ? :

`&& 、||`短路运算，是短运算符，`&、|`也可以作为逻辑与，或；这两个是强制两边都要计算

两个操作数进行加减乘除，其中一个为double，结果为double， 否则，其中一个为long，结果为long，其余情况都是int

`==` 比较的是栈中两个变量的字节组合是否相同，对于引用类型，== 判断他们是否指向同一对象。因为指向同一对象，在栈中两个变量存放的地址就一样。

```java
String a = "abc";
String b = "abc";
a == b;   // true        ,不懂这两个有什么不一样
String c = new String("abc");
String d = new String("abc");
c == d;   // false
```

**位运算**

`<<`  按位左移 `5<<2 == 20`，按位左移一次相当于`*2`

`>>` 按位右移，按位右移一相当于予以2

对于时钟来说，模为12， 因此，对于任意时刻，往前拨2小时和往后拨10个小时是等价的，因此，对于模为16的四位二进制来说，-1和+15是等价的；-2和+14是等价的；-3和+13是等价的；-4和+12是等价的，-5和+11是等价的，-6和+10是等价的，-7和+9是等价的，-8和+8是等价的！！！

所以，-3的补码是13；-4的补码是12，-8的补码是8

| 原码 |  0   | 1    | 2    | 3    |  4   | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   |
| ---- | :--: | ---- | ---- | ---- | :--: | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
| 补码 |  0   | 1    | 2    | 3    |  4   | 5    | 6    | 7    | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |
|      | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |



阿里巴巴开发手册

## 流程控制

   python通过`input`语句获取输入，Java通过`Scanner`类获取用户的输入

```java
Scanner s = new Scanner(System.in);
if (s.hasNext()) {
   // 执行语句
}
```

Scanner类的实例方法`hasNext() hasNextLine() hasNextInt()`等方法可以用来判断是否有符合调教的输入；相应地，可以用`next() nextLine() nextInt()` 获取输入

### 条件语句

```java
if (测试语句) {
  // 执行语句
} else if (测试语句) {
  // 执行语句
} else {
  // 执行语句
}
```

```java
switch (expression) {
  case value:
    // 执行语句1
    break;
  case value:
    // 执行语句2
    break;
  default:
    // 执行语句3
}  
```

switch 支持字符串，case标签**必须是字符串常量或字面量**，不能写成变量名。

### 循环语句

`for`，`while`，`do...while`，和C语言完全一样

增强for循环：类似于python的遍历

```java
int[] numbers = {2, 3, 4, 5};
for (int x: numbers) {
    System.out.println(x);
}
```

`break`和`continue`用法和C语言也一样

## 方法

Java没有函数的说法，只有方法。方法名和参数表共同构成方法签名，签名可以看成是函数的标识

- 修饰符：public，static
- 方法只能声明单一的返回值

静态方法和非静态方法：

前者有static修饰符，后者没有

静态方法是和类一起加载的，存在的很早，没有static修饰的普通方法是类实例化之后才存在的

Java传递参数的方式：和python是一样的（我没发现有什么区别），不说是按值传递或者是按引用传递了；**方法（函数）得到的是参数的副本，但是参数始终是引用。**举一个python的例子

可以把参数（或者说对象）当成鱼，引用当成鱼线

```python
def f1(arr):    
    arr.pop()
    
a = [1, 2, 3]
f1(a)
print(a)       
# [1, 2] 传递的是引用的副本，相当于复制了一条鱼线钓到同一条鱼
```

```python
def f2(arr):
  arr = [4, 5, 6]
  
a = [1, 2, 3]
f2(a)
print(a)     # [1, 2, 3]  重新绑定，相当于复制的鱼线钓到了另外一条鱼
```

保持方法的原子性：一个方法只完成一项功能，利于后期拓展 

### 重载

​	Java支持方法重载，重载的条件是要是**使用不同的参数**

- 返回类型可以不同
- 不能只改变fanhuileixing
- 可以更改存取权限

### 可变参数

​	可变参数在方法定义中当作数组来用，传递参数既可以传递数组也可以传递多个参数。和python一样，Java的可变参数必须放到一般参数的后面。

```java
public static void max(double... numbers) {
  // 返回数组中最大的元素
}
int[] a = {1, 2, 3};
max(a);
max(1, 2, 3);  // 功能相同
```

---

## 数组

​	数组声明、初始化这些和以前的不是太一样

### 数组声明、创建

```java
int[] a;
int b[];  // 声明，推荐第一种方式，声明并没有分配数组空间
```

```java
a = new int[3];  
b = new int[] {1, 2, 3};  // 创建数组（分配空间），默认初始值0,两种都行
```

```java
int[] a = {1, 2, 3};  // 初始化方式
int[] b = new int[10];
int[] c = new int[] {1, 2, 3};
```

使用数组字面量绝对不是~~{1, 2,  3}~~, 而是 `new int[] {1, 2, 3}`

, 注意，Array这个类基本不用，主要的是Arrays类

**特点：**

- 数组一旦创建，长度不可改变
- 数组中的元素必须是同一类， 可以是基本类型也可以是引用类型
- 数组属于引用类型，即对象

## 内存管理

Java中对象是在堆中存放的

**堆**：存放引用类型，可以被所有线程共享; 对象生存的空间

**栈** ：存放基本类型，以及引用类型的地址；方法调用及局部变量的生存空间

*实例变量*存在于对象所属的堆空间上，而*局部变量*的生命周期只限于方法被放在栈上的这段期间，即方法被调用到执行完毕为止。方法的参数也属于局部变量

## 面向对象编程

this指向当前类,此时方法不能加static, 属性可以加static， 原因不知道

实例变量有默认值，原始的默认值0/0.0/false，引用的默认值null。

实例变量与局部变量的区别：

实例变量声明在类中，局部变量声明在方法中，局部变量没有默认值，直接声明不初始化使用会报错！

### 构造函数

  构造函数不能标记为静态的。 构造函数，是为了将一个类实例化一个对象才需要使用的，进行一些必备的初始化操作。何为静态，类似全局的，已经初始化过的，静态函数就是指该函数不和具体对象相关，只和类相关，但是构造函数是和对象直接关联的，这两个东西从面向对象的概念上完全不可能融合在一起。

构造函数标记为private避免类被实例化，比如`Math`

使用new关键字，必须要有构造器，即构造方法，构造器没有返回值，创建对象时自动调用构造方法

唯一在构造函数之外能够调用构造函数的方式就是new一个对象。

构造器用来初始化值；构造器必须和类名相同，必须没有返回值

```java
public class Duck {
  
	public Duck () {
    // 构造函数，没有返回类型，名字必须和类名相同
    // 在对象被赋值给引用之前就执行
}
}
```

构造函数不会被继承,但是在创建新对象时，**所有继承下来的构造函数都会执行。按照继承连从最原始执行**,(这是因为对`super()`的调用必须是构造函数的第一个语句)

编译器两种涉入构造函数的方式：

- 如果没有编写构造函数

  ```java
  public className () {
  	super();
  }
  ```

- 如果有构造函数但是没有调用`super()`,会在每个重载版本的构造函数加上这种调用`super()`

**编译器加的一定是没有参数的版本**

这样的话，父类A没有无参数的构造函数，假如B类要继承A，在B类的构造函数中一定要显式调用父类的构造函数。

**this() 和 super() 的区别：**

​	this是对对象自身的引用，`this(参数列表);`这句话会调用同一个类的相应参数列表的重载的构造函数，所以`this()`只能在构造函数中调用，且必须是第一行语句，*`this()`和`super()`不能同时调用*

构造函数可以重载，即有参数和没参数，可以重载很多个; 一定要有不需参数的构造函数

Java可以有与类同名的方法而不会变成构造器，是因为方法注明了返回类型。

定义有参构造器之后，想要 使用无参构造需要重构（编译器只会在完全没有设定构造函数的时候才会调用无参构造）  

属性私有：在属性定义是加private关键字，外部不能直接获取

### 封装

​	封装的基本原则：将实例变量标记为私有的（private），并提供共有的getter和setter来控制存取动作。

```java
class Dog {
  private int size;
  
  public int getSize () {
    return size;
  }
  
  public void setSize (int s) {
    size = s;
  }
}   // 标准的写法
```



### 继承

子类继承父类，得到的是public protected 和不加修饰符的属性，加了private修饰符的属性子类访问不了

私有的（private）无法被继承 

子类的构造方法的第一行会默认调用父类的无参构造`super()`，如果父类没有无参构造（即只有有参构造，构造方法必须有，一般有参无参同时有），子类必须显式调用父类的有参构造

所有的类都直接或间接继承object类

Java只能单继承，即一个类不能同时直接继承多个类

子类中引用父类的方法并扩充功能

```java
public void roam() {
  super.roam();
  // 自定义功能
}
```

子类继承父类的成员（实例变量和方法），然而父类可以通过存取全县决定子类是否能够继承某些特定的成员 private不能被继承



### 方法重写

子类重写父类的方法，返回类型必须相同

不能降低方法的存取权限，只能相同或更高：public > prodected > default > private

抛出的异常可以缩小，不能扩大 

### 多态

​	多态是同一个行为具有多个不同表现形式或形态的能力；多态就是一个接口，使用不同的实例执行不同的操作

<img src="https://www.runoob.com/wp-content/uploads/2013/12/java-polymorphism-111.png" alt="img" style="zoom: 50%;" />

多态存在的三个必要条件：

- 继承
- 重写 (子类重写父类方法**,签名必须相同**)
- 父类引用指向子类对象：`Parent p = new Child();`

Parent p表示变量p在栈中存放的是父类的引用；这个引用指向堆中子类对象（实例）

当使用多态调用方法时，首先检查父类是否有该方法，如果没有则编译错误，如果有，就去调用子类同名方法。

*原理，编译器会寻找引用类型来决定你是否可以调用该引用的特定方法。但在执行期，Java虚拟机寻找的并不是引用所指的类型，而是在堆上的对象。*

因为这个p还是Parent类型的，如果Parent没有这个方法就会报错

除此之外，静态方法和非静态方法对多态有影响

static修饰的静态方法，属于类方法，不属于实例，还有final，private修饰的方法都没办法重写

类中的静态代码块只会执行一次，这个类实例化多次只会执行一次 

final修饰的类不能被继承

静态导入包

```java
import static java.lang.Math.random;
System.out.println(random());
// 可以不加Math直接使用 
```

一个Java类里面可以有多个`class`，但是只能有一个`public class`

### 抽象类

在类声明前面加上关键字abstract即可

抽象类不能初始化；抽象的类代表此类必须要被extends过，抽象的方法代表此方法一定要被覆盖过。

抽象方法没有实体

```java
public abstract void eat();   // 没有方法体
```

*如果你声明处一个抽象方法，就必须将类也标记为抽象类。不能在非抽象类中拥有抽象方法。*

抽象方法的意义在于定义出一组子类共同的协议。

### 接口interface

接口的定义：以interface关键字取代class关键字

```java
public interface Pet {...}
```

接口的实现：

```java
public class Dog extends Canine implements Pet, Saveable {...}
// 类可以实现多个接口
```

接口的方法默认是`public abstract`的

接口是100%的纯抽象类，可以用来解决多重继承的问题



## 易错知识

1. Java必须要有main函数才能运行。。。

 

## 常用的内置函数类

静态倒入包 `import static java.lang.Math.*`，使用静态方法直接写`max()`, 不用写`Math.max()`

### Arrays类

```java
Arrays.toString();
Arrays.sort();
```

### ArrayList类

类似python中的list，可以动态操作.只能携带对象而不是primitive主数据类型

```java
ArrayList<Egg> mylist = new ArrayList<Egg>();   // 不定长
// <Egg> 表示创造出的list存放Egg类型的元素,如果不写，默认为Object
.add(Object elem);   // 向list添加元素
.remove(int index);  // 移除索引对应的元素
.contains(Object elem);  // 返回boolen值
.isEmpty();
.indexOf(Object elem);  // 返回对象参数的索引或-1
.size();   // 长度
.get(int index);   // 返回当前索引对应的元素
```

### Date类和Calendar类

Date类的实例一般用来获取当前时间

Calendar用于操作日期

```java
Calendar cal = Calendar.getIntance() ; // 返回Calendar子类的实例
.add(int field, int amount); // 加减时间值
.get(int field);  // 取出指定字段的值
.getIntance();  // 返回Calendar，可指定地区
.getTimeInMillis();   // 以毫秒返回时间
.roll(int field, int value); // 加减指定字段时间，不进位
.set(int field, int value);  // 设置时间值
.set(year, month, dat, hour, minute);   // 完整时间值
.setTimeInMillis(long millis);   // 以毫秒设置时间
// 字段 DATE，HOUR，MILLISECOND，MINUTE，YEAR
```



## 数字与静态

**静态方法**：一种不依靠实例变量也就不需要对象的行为，Math类的所有方法都是静态方法，因此使用方法时，无需Math实例，直接使用类本身即可。

非静态方法依靠实例而存在

静态方法和非静态方法区别：以类的名称调用静态方法；以引用变量的名称调用非静态方法。

静态方法不能调用非静态的变量，也不能调用非静态的方法。静态变量在类被加载的时候初始化

静态项目初始化的两项保证：

- 静态变量会在该类的任何对象创建之前就完成初始化
- 静态变量会在该类的任何静态方法执行之前就初始化

静态变量也有默认值

静态变量：它的值对所有的实例来说都相同，即被同类的所有实例共享的变量。它只会在类第一次载入是被初始化，以后创建实例都和它没关系。

---

`final`的变量代表不能改变值，`final`的method不能被覆盖，`final`的类不能被继承

Java常量一般用`static final`修饰

```java
Math.pow()   // 幂运算 
```

`primitive`主数据类型的包装类型

- Boolean
- Character
- Byte
- Short
- Integer
- Long
- Float
- Double

String类型转换为primitive主数据类型用静态方法：`Integer.parseInt()`, `Double.parseDouble`等

primitive主数据类型转换为String，`Integer.toString()`, `Double.toString()`
