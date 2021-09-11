```bash
mysql -u root -proot   # 连接数据库
```

```bash
SET PASSWORD FOR root@localhost=PASSWORD('1234');  # 修改密码
```

mysql不区分大小写。

## 基本语法

```bash
create database db1;   # 创建数据库
use db1;  # 使用指定数据库
create table tb1 (empid varvhar(10), name varchar(10) ,age(int));   # 创建表格
insert into tb1 values(value1, value2, value3);    # 插入数据
```

```bash
show databases;
use db1;   # 指定数据库
select database();  # 显示当前使用的数据库
desc tb1; # 显示表格数据类型
select * from tb1;
```

几种常见的数据类型，int, double, char, varchar, text, date, datetime 

### 修改表alter table



| Field |     Type     | Null | Key  | Default | Extra |
| :---: | :----------: | :--: | :--: | :-----: | :---: |
| empid | varcahr(10)  | yes  |      |  null   |       |
| name  | varchar(100) | yes  |      |  null   |       |
|  age  |   int(11)    | yes  |      |  null   |       |
|       |              |      |      |         |       |



```bash
alter table tb1 modify name varchar(100);   # 修改列的数据类型
alter table tb1 add  briirth datetime;  # 在表格上追加列
insert into tb1 values("N111", "songtian", 38);  # 插入数据
insert into tb1 (name, age) values ('hello', 25); # 可以不插入全部数据
alter table tb1 add birth datetime first; # 在第一列加入新列
alter table tb1 add birth datetime after empid; # 在empid列后面添加列
alter table tb1 change birth birthday date;  # 修改列名和数据类型
alter table tb1 修改前的列名 修改后的列名 修改后的数据类型;
alter table tb1 drop 列名;  # 删除列
alter table tb1 modify name varchar(10) default '未输入名字'； # 设置默认值
alter table 原表名 rename 新表名；   # 重命名表格
```

主键条件： 没有重复值，不允许输入空值（null）

唯一值

默认值

索引：在设置了主键的情况下，索引会自动创建

```bash
create table t_pk (a int primary key, b varchar(10)); # 指定a为主键
create table t_uniq (a int unique, b varchar(10)); # 指定a列元素不可重复
create table t_series (a int auto_increment primary key, b varchar(10));
# a列具有自动连续编号功能
create index 索引名 on 表名（列名）; # 在表格的指定列创建索引
```

### 复制、删除表和记录

```bash
create table 新表名 select * from 原表名；  # 复制整个表的结构
create table 新表名 like 原表名；  # 只复制结构，不复制内容
insert into 表名 select * from 原表名； # 向已有的相同结构的表中复制元素
insert into 表名(列名) select 列名 from 原表名；# 选择某一列复制，如果数据类型不相同，复制可能会失败
```

### 删除表、数据库和记录

```mysql
drop table 表名；   # 删除表
drop database 数据库名；  # 删除数据库时里面内容同时清空
delete from 表名；   # 删除表中所有记录，打回empty set
```

```mysql
delete from tb where 条件;
```



delete 只删除记录，不删除表的列结构。删除表本身使用drop table；

## 熟练使用mysql

`select`相当于打印语句，`*`是通配符，可以代替任意字符。

### 函数

`count(x)`用于计算除null以外列x的值的个数， `count(*)`记录的个数包含null

`avg()` 返回指定列数据的平均值

`sum()` 返回指定列数据总和

`pi()` 返回圆周率

`database()` 返回当前数据库

`concat(a, b, c)` 拼接多个字符串

`substring(列名， 2， 3)` 从指定列的第二个字符开始连续显示3个字符

`revrese()` 反转字符串

`now()`返回当前日期和时间

**设置别名**

```mysql
select 列名1 as 别名1, 列名2 as 别名2 from 表名;
```

**算数运算符**

`+`, `-`, `*`, `/`,`div`(a除以b取整)，`%`取模

操作数是列名

### 对数据进行筛选过滤

```mysql
select 列名 from 表名 limit 3;   # 显示前三条数据
```

```mysql
select 列名 from 表名 where 条件;  # where 设置条件并取出条件相匹配的记录
```

**比较运算符**

|             =             |      等于      |
| :-----------------------: | :------------: |
|    >    <     >=    <=    |                |
|            <>             |     不等于     |
|         o   IN  x         |  o 在x列表中   |
|       o  NOT IN  x        | o 不在x列表中  |
|   o  BETWEEN  x AND  xx   |  o在x和xx之间  |
| o  NOT BETWEEN  x AND  xx | o不在x和xx之间 |

例子如下

```mysql
select * from tb where month in (5, 6);    # 列month的值等于5或6
```

**使用字符串作为条件**

```mysql
select * from tb where empid = 'A101';  # 必须完全匹配才能选择出来
```

```mysql
select * from tb where empid like '%1%';  # 如果不使用通配符，like也相当于完全匹配
```

| %    | 任意字符串   |
| ---- | ------------ |
| _    | 任意一个字符 |

```mysql
select * from tb where empid not like 'A101'; # 提取不相符的数据
```

使用null**作为条件**

```mysql
select * from tb where name is null ;    #  提取name列值为null的记录
```

注意，提取列值非null的条件是 `is not null`, 当提取值为null的记录时，即使条件设为`where name = null`也无法提取出相应的数据。

同一列相同的数据只提取一次，使用`distinct`关键词

```mysql
select distinct empid from tb;
```

指定多个条件进行查询

使用and和or进行连接；当同时出现两者，**优先处理or**，可以使用括号指定优先级

`case when `语句可以根据不同条件选择出来的数据进行不同的评定。

#### 排序

默认使用升序（asc）排序，可以指定降序（desc），关键词`order by`

```mysql
select * from tb order by age desc;
```

#### 指定记录的显示范围

```mysql
select * from tb order by age desc limit 2 offset 3;
```

降序排序之后，选出第4，5条数据。`offset 3` 代表从第一条记录开始移动三位，从第四条数据开始显示

#### 分组显示 group by

普通的使用group by没有什么用，因为分组之后每组只会显示一条记录

```mysql
select empid, avg(sales) from tb group by empid; # 显示各组的平均值
```

### 设置条件分组显示

- 先分组，再根据分组结果选出符合条件的组

  ```mysql
  select 
  	empid, sum(sales)
  from tb
  	group by empid 
  having sum(sales) >= 200;
  ```

- 先进行筛选，根据结果进行分组

  ```mysql
  select 
  	empid, avg(sales)
  from tb
  	where sales >= 50
  group by empid;
  ```

- 另外还有分组之后排序

`where   group by   order by`三者在语句中的顺序：where第一，group by第二，order by第三

### 操作数据

```mysql
update tb set name = '无名氏';  # 瞬间把表格这一列的数据全部改为无名氏
update tb set name = '无名氏' where name = null;  
insert into tb2 select * from tb where 条件;  # 复制数据到以存在的表格
```

**删除指定数据**

delete 只删除记录，不删除表的列结构。删除表本身使用drop table；

```mysql
delete from tb where 条件;   # 删除指定记录
```



### 使用多个表

使用union上下联合(**纵连接**)多个表，一般来说，联合的表具有相同的结构，结构不同结构可能出乎意料

```mysql
select * from tb1 union select * from tb2;  
```

```mysql
	(select * from tb1 where 条件1)
union 
	(select * from tb2 where 条件2)
union 
	(select * from tb3 where 条件3);  # union可以联合多个表格
```

`union`默认会消除重复记录，数据集很大时可能会浪费时间，可以使用 'union all'不消除重复记录。



### 使用join进行横连接

```mysql
select tb.empid, tb1.name from tb join tb1 using(empid);
```

 必须指定连接键，相同时使用using函数，当连个表的连接列名不相同时，使用`on tb.empid=tb1.name`而且select后面的列名必须指定表名。

join默认是內连接，即只有两个表都有这个数据才会显示。left join是左外连接，即左侧表格的都会显示，不管右边表格有没有相应数据。与之相对的是right join。full join全外连接

### 自连接

将自身和自身连接在一起，联合之后会有平方个次数据。这和普通的连接不一样.因为**一般的join连接都指定了连接条件，自连接没有**。如果不指定普通连接的连接条件，结构就和自连接一样。

自连接必须为表指定别名。

```mysql
select * from tb as a join tb1 as b;
```

自连接进行排序

```mysql
select a.name, a.age, count(*) from tb as a join tb as b where a.age<=b.age group by a.empid;
```

这里count函数计算的是分组之后每个组的个数。最难以理解的是条件判断。这里是a表格的age每个值都先和b表格中的age第一个值比较；然后a表格age列的每个值在和b表格age的第二个值比较，以此类推。



### 视图

​	视图是指向基表数据的窗口，可以通过视图修改基表的数据。同时，修改了原表的数据，视图会动态地根据原表数据进行更新。

​	视图没有实体，只是一个虚拟表。

向视图进行写入数据有所限制，在使用union，join，自查询的视图中，不能修改视图数据。

而一般的视图，插入或修改数据，会在原表中显示出来，但如果数据不满足视图的筛选条件，就不会在视图中显示。

```mysql
create view v1 asa select * from tb where 条件;
```



为了避免这种情况，在创建视图时可以指定`with check option`,

```mysql
create view v4 
	as
select * from tb
	where sales > 100
with check option;
```

### 替换、修改或删除视图

当视图可能已经存在时，下面的操作会覆盖原视图：

```mysql
create or replace view v1 as select * from tb;
```

直接修改整个视图的结构和内容：

```mysql
alter view v1 as select * from tb1;
```

mysql中删除某个对象使用drop命令。删除表格，视图，数据库都是类似的

```mysql
drop view v1;
```

### 储存过程

无参版本

```mysql
delimiter //   # 将分隔符改为//，避免写一句输出一句
create procedure pr1()
begin
sql语句1 ;
sql语句2 ;
end
//
delimiter ;
```

有参数版本`create procedure pr2(d int)`, 注意参数名在前，参数类型在后

### 执行储存过程

```mysql
call pr1;     # 加不加括号都行，因此最好加括号
call pr2(d);  # 必须加括号，带参数
show create procedure pr1;  # 显示储存过程的内容
drop procedure pr1;   # 删除储存过程
```

### 储存函数

储存函数和储存过程唯一的不同就是储存函数会在执行后返回一个值。

```mysql
create function 函数名(参数 类型) returns 返回类型
begin
	sql语句
	return 返回值
end   # 注意第一句是returns
```

```mysql
drop function fn1;
```

### 触发器

在表进行某种操作时会被自动触发的机制。例如创建在表tb1中记录被删除时自动将被删除记录插入tb1_from的触发器tr1

```mysql
delimiter //
create trigger tr1 before delete on tb1 for each row 
begin
insert into tb1_from values(old.empid, old.name, old.age);
end
//
delimiter ;
```

```mysql
drop trigger tr1;   # 删除触发器
```



## 事务

将多个不可分割的操作，即原子型事件称为事务。事务成功则可以提交，否则必定回滚。

drop操作和`alter table`无法回滚。

开启事务`start transaction;`,提交开启事务之后的操作`commit;`,回滚开启事务之后的操作`rollback`

如果在未提交事务的情况下关闭连接，事务将自动回滚。



## 文件操作

从文件中读取数据

```mysql
load data infile '文件名' into table 表名 选项的描述;
# 选项的描述
fields terminated by 分隔符（默认是'\t',Tab）
lines terminated by 换行符（默认是'\n',换行）
ignore 最开始跳过的行 lines（默认是0）
```

```mysql
load data infile '文件路径' into table tb1k fields terminated by ',';   # csv
```

将数据写入文本文件

```mysql
select * into outfile '文件名' 选项的描述 from 表名;
#  例子
select * into outfile '文件名' fields terminated by ',' from tb1;
```

从文件中读取执行sql命令

```mysql
source  文本文件名    # 不带引号和分号
```

将输出重定向到文件

- 在shell中连接时`mysql -u root -p1234 > log.txt`
- 在mysql中使用`tee 输出文件名`之后接下来的输出会同时保存到文件，`notee`停止向文件输出

### 备份和恢复数据库

​    可以将数据库的创建过程的整个转存到文本文件，作为备份或者复制到其他机器上，即**转储（dump）**

以下情况都是在shell执行

```bash
# 转储数据库格式,在shell执行
mysqldump -u 用户名 -p密码 数据库名 > 输出文件的名称
# 具体到情况
mysqldump -u root -p1234 db1 > db1_out.txt
```

这样在本目录就会得到一个`db1_out.txt`文件，注意**尖角号的尖朝哪，数据就是往哪个方向传输。**

#### 将转储文件恢复到数据库db2

```bash
# 使用mysqladmin可以直接在shell创建删除数据库
mysqladmin -u root -p1234 create db2
# 注意 < 方向
mysql -u root -p1234 db2 < db1_out.txt
```

只转储恢复指定table

```bash
# 从db1中转储tb1
mysqldump -u root -p1234 db1 tb1 > test.txt 
# 相当于复制了tb1到db2
mysqldump -u root -p1234 db2 < test.txt
```



#### 字符编码问题

​	如果在转储和恢复过程中出现中文乱码情况的话，就要在两个执行命令最后面加上

```bash
--default-character-set=utf8
```

## PHP基本语法

​	php是动态语言，使用变量不用声明；变量命名规则：

- 以`$`开头，大小写敏感，第二个字符不能是数字

### 数据类型

| 整数   | integer       |
| ------ | ------------- |
| 浮点数 | float，double |
| 字符串 | string        |
| 布尔值 | boolean       |
| 对象   | object        |
| 数组   | array         |
| 资源   | resource      |
| 空值   | NULL          |

```php
"" 和''都可以用来括住字符串，""也可以括变量当作原意，但是''不行。字符串之间用.连接
```

比较运算符中的不等于`<>`,其他语法和C语言相似。

使用php脚本编写web页面需要用priint或echo将HTML标签作为文本输出.

使用get方法发送数据时数据作为参数加入到`URL`中（在？后面），post不会

HTTP报错500一般是输出动态页面时程序的错误。

