```bash
mysql -u root -proot   # 连接数据库
```

```bash
SET PASSWORD FOR root@localhost=PASSWORD('1234');  # 修改密码
```

mysql不区分大小写。

### 基本语法

```bash
create database db1;   # 创建数据库
use db1;  # 使用指定数据库
create table tb1 (empid varvhar(10), name varchar(10) ,age(int));   # 创建表格
insert into tb1 values(value1, value2, value3);    # 插入数据

```

```bash
use db1;   # 指定数据库
select database();   # 显示当前使用的数据库
desc tb1;            # 显示表格数据类型
select * from tb1; 
```

```mysql
# 显示数据库和表格
show databases;
show tables;
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

## 复制、删除和记录

### 复制

```mysql
# 复制整个表格
create table tb1 select * from tb;
# 复制表格结构,不包括数据
create table tb2 like tb;
# 复制相同结构的其他表格数据
insert into tb3 select * from tb;
# 如果只复制指定列，其他列用NULL补全
```

###  删除表、数据库和记录

​	删除整个内容都是用`drop`，删除哪种类型，后面就加什么类型的名字

```mysql
drop table tb;
drop table if exists tb; # 如果不存在不报错
```

删除表中记录

```mysql
delete from tb;        # 删除表格中的所有记录  
```


## 使用条件对表格数据进行提取


 `*`是通配符，可以代替任意字符

 ```mysql
# 指定别名，表格和列都可以指定别名
select 列名 as 别名 from 表名;
 ```

  在select后面可以使用运算符号，基本和以前一样。
函数后面的括号中一般放的都是列名。
```mysql
select database();   # 显示当前数据库
select version();    # 显示版本
select user();       # 显示当前数据
```



```mysql
# 常用函数
concat(s1, s2,...);     # 连接多个字符串
substring(empid, 2, 3); #从第二个字符开始截取3个字符
reverse();
repeat('.',age);        # 重复指定字符指定次数 
```


使用where进行条件选择

新的逻辑运算符



|       比较运算符      | 含义         |
|:---------------------:|--------------|
|           <>          | 不等于       |
|         a IN b        | a在列表b中   |
|       a NOT IN b      | a不在列表b中 |
|   a BETWEEN b AND c   |              |
| a NOT BETWEEN b AND c |              |
|           =           | 等于         |


```mysql
# 使用字符串作为条件
select * from tb where empid = 'A101';
# 模糊搜索
select * form tb where empid like 'A101';
# 这个搜索和上面完全等价
''中可以包含通配符，%代表任意字符串，_代表任意一个字符串。
```


多个条件进行选择，使用`and`或`or`连接；**当and和or混合使用时，会优先处理and**，可以使用()更改优先级。

根据成绩不同判定不同等级的做法：
```mysql
select 
case 
    when sales >= 100 then 'good'
    when sales >= 50 then 'bad'
    else 'badly'
end as alias
from tb;
```


#### 排序

```mysql
select col from tb order by col_name;
select * from tb order by sales;    # 默认升序排序ASC
select * from tb order by sales desc limit 5;  # 选出前5名
select * from tb order by sales desc limit 2 offset 3;
# offset 3,从第四条开始显示
```


#### 分组显示

```mysql
# 默认的这种分组显示没意义，只会每组显示一条数据
select * from tb group by empid;
select count(*) from tb group by empid; # 计算各组的记录数
```


两种分组和条件结合的筛选方法
```mysql
# 先分组，根据结果筛选满足条件的组
 select 统计列 from 表名 group by 分组列 having 条件;

# 先提取满足条件的记录，在根据这个分组
select empid, avg(sales)
from tb 
    where sales>=50
group by empid;
```


分组后排序

```mysql
select  empid,avg(sales)
from tb
    group by empid
order by avg(sales)
    desc;
```


   当同时出现`where 条件`,`group by `, `order by `时，三个出现的顺序
按照w, g, o

### 编辑数据

更新列中的所有数据
```mysql
update tb set col = 设置的值;   # 该列所有值换成指定值
alter table tb add remark int;  #  添加新列
update tb set col = val where condition; # 只更新指定列的值

```


复制 删除符合条件的记录

```mysql
create table tb1 
    select * from tb
where condition;

delete from tb where condition;
# 排序后删除
delete from tb 
    order by sales
desc 
    limit 4;
```


## 联历多个表格

`union`进行纵向连接
```mysql
# 可同时联历多个表格，中间用union连接
select * from tb1 union select * from tb2;
# 按条件进行纵向连接
select * from tb1 where condition1
    union
select * from tb2 where condition2;
```


`join` 进行横连接

```mysql
# 基本语法
select col1 from tb1 
    join tb2
on tb1_col1 = tb2_col2;

join即inner join，只会提取两个表中都有的记录
在选择列的时候要指明tb1的列和tb2的列
```


如果连接条件的两个列名字相同，可用`using()`代替`on tb1.col1=tb1.col1`

`left join`左外连接， `right joii`右外连接

#### 自连接

  自身和自身连接，自连接必须给表格指定别名，**自连接一个很大的不同是
不用指定连接条件**

```mysql
select * from tb1 as a 
    jion tbe2 as b;     # 自连接数目为平方的
```

```mysql
# 自连接进行排序
select a.name, a.age, count(*)
    from tb1 as a
join tb1 as b
    where a.age <= b.age
group by a.empid;
```


#### 子查询

这个第一阶段查询出来的结果是指定的列 
```mysql
# 非常有用，比如筛选出数据表中销售额最高的一条记录
select * from tb where sales in 
    (select max(sales) from tb);
# 筛选出sales大于平均值的记录
select * from tb where sales >=
    (select avg(sales) from tb);
```

使用`exists`,第一阶段查询得到的是符合条件的记录
```mysql
# 仅显示tb和tb1中都存在的empid记录
select * from tb1 where exists
   (select * from tb where tb.empid = tb1.empid); 
```

```mysql
#  使用子查询进行排序
1、创建和tb结构相同的tb_rank
create table tb_rnak like tb;
2、向表中添加自动记录序号的列
alter table tb_rank add c_rank into auto_insertment primary key;
3、子查询插入新表格
insert into tb_rank
    (empid, sales, month)
(select empid, sales, month from tb order by sales desc);
```


### 使用视图

视图相当于表格的另一种展现形式;**更新视图，基表的数据也会更新。**

向视图中插入不满足视图筛选条件的数据，视图中不会显示，基表会显示。

```mysql
# 创建视图
 create view v1 as select * from tb where condition; # as易错
# update view, it will change base table 
update v1 set name = 'new' where name = 'old'
```


更新基表时，根据基表和条件创建的视图会动态变化。
通过`show tables` 查看table时，table和view交织在一起。

#### 替换、修改和删除视图

```mysql
# 创建或替换原有视图
create or replace view v1
    as 
select ...
```

```mysql
# 替代视图的结构和内容
alter view v1 as select col from tb;
# 删除视图
drop view v1;
```


### 储存过程和函数

为了避免在shell中写一行执行一行，可以重定义分隔符`delimiter //`

```mysql
# create procedure, the parameter in font
create procedure pr1 (parameter data_type)
begin 
    sql statement1;
    sql statement2;
end
# call procedure
call pr1();
# drop procedure 
drop procedure pr1;
```

**About stored function**
```mysql
 # create stored function
create function fn1 (parameter data_type) returns data_type
begin
    sql statement;
    return value;
end
#  define variables though declare
declare variable_name data_type;
```


#### trigger 

触发器是一种对表执行某操作后会触发执行其他命令的机制。



| trigger timing |                    | col_value |
|----------------|--------------------|-----------|
| before         | 在对表处理之前触发 | old.col   |
| after          |                    | new.col   |

```mysql
# create trigger 
create trigger  tr1 before delete on tb1 for each row
begin
insert into tb1_from values(old.empid, old.name, old.age);
end
# 将tb1中删除的数据插入到tb1_from
```

### 事务

  将多个操作作为单个工作但愿处理的功能称为**事务**，事务**提交**
即代表执行成功，不成功则**回滚**，即回到原状。
drop命令不能回滚。

```mysql
start transaction;      # 开启事务
commit;                 # 提交
rollback;               # 回滚
```



### 使用文件进行交互

​	导入文件
```mysql
load data infile 'file_name' into table tb1 选项的描述；
# 描述
fields terminated by 分隔符（默认Tab）
lines terminated by 换行符（默认 '\n')
ignore 最开始跳过的行 Lines (默认是0)
```

将数据写入到文本文件
```mysql
 select * into outfile 'file_name' 选项的描述 from tb1;
# instance 
select * into outfiel 'C:/data/out.csv' fields terminated 
    by ',' from tb1; 
```


从文件中读取并执行sql语句

```bash
# it isn`t a sql statement ,so not need ;
source file_name
# execute the sql in the file from the command line
mysql db1 -u root -p1234 -e"source file_name"
```


将sql的执行结果重定向到文件

- 通过命令提示符进行重定向
```bash
# 注意>的方向
mysql db1 -u root -p1234 -e"source file_name" > abc.txt
# 使用重定向同时输入输出
mysql -u root -p1234 < in.txt > out.txt
# 将in的内容作为输入，输出到out 
```

- 通过mysql命令使用重定向
between `tee file_name;` and `notee`, the sql statement will be
out to file.

**备份和恢复数据库**

对数据库的所有内容执行到处的操作称为**转储**
```bash
# use mysqldump to export
mysqldump -u root -p1234 db1 > out.file
# recover dump file
mysqladmin -u root -p1234 create db2
mysql -u root -p1234 db2 < out.file
# 将db1整个复制到db2
```

如果编码乱码，在命令行操作时加上参数`--default-character-set=utf8`

