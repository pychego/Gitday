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



