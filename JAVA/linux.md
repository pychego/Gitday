## 

1、基本操作

文件系统通过索引节点号而不是文件全名及路径来表示文件。

`ls` 即list   

- `-a` 即all，查看全部文件，包括隐藏文件  

- `-l` 具体的文件属性

`cd` change directory  可直接加相对路径，加绝对路径时以`/`开头

`pwd` （英文全拼：print work directory） 命令用于显示工作目录。

`mkdir` 创建目录

`rmdir` 删除目录

`cp`  复制文件，详细信息看`cp --help`

`rm -rf 文件名`  强制删除文件

检查版本 

```bash
[root@pychego bin]# cat /etc/redhat-release 
CentOS Linux release 7.9.2009 (Core)
```

```shell
systemctl restart firewalld 	# 重启防火墙，重启服务器之后要弄一下
```

###  1.1软链接和硬链接

软链接即为符号链接（symbolic links)

```shell
ln -s 原始文件 符号链接文件
# 创建完成之后，使用ls -l命令可以看到符号链接通过->指向原始文件，符号链接相当于指向了原始文件，来两个文件并不相同
```

硬链接

```shell
ln 原始文件 新文件
# 相当于一个inode指针指向了两个不同的地址，这两个文件本质上是同一个文件，修改是同步的
```

### 1.2重命名文件

```shell
mv 源文件 目标文件     # 两个都是文件名相当于重命名
mv 源文件夹 目标位置	 # 移动文件夹
```

###  1.3删除文件

```shell
rm 文件名
rm -r 文件夹			# recursive 递归删除
-f 强制删除
rm -rf /				# 删库跑路
```

### 1.4查看文件

```shell
cat 文件名				
more
less   # 两个可以分页显示
tail
head   # 分别显示文件开头和结尾
```

### 1.5 文件占用的磁盘空间

```shell
df 查看所有已挂载磁盘的使用情况，不太懂。。。
-h --humam-readable
```

```shell
du        # 显示当前目录下所有文件、目录和子目录的磁盘使用情况，单独使用用处不大
-s				# 显示输出参数的总和
-h				# 格式化输出
du -sh * | sort -nr     # n 按数字排序，r反序
｜将du的输出重定向到sort命令
```

### 1.6 文件的权限管理

`umask`显示了要创建文件对象时哟啊减去的权限值。

例如，对文件来说，全权限值是666，umask为022，则创建的新文件默认权限是644

```shell
➜  shell lla       
总用量 12
drwxr-xr-x   2 www  www  4096 10月  1 16:48 .
dr-xr-x---. 23 root root 4096 10月  1 20:28 ..
-rwxr-xr-x   1 www  www   193 10月  1 20:26 test
# 需要修改文件的读写权限使用chmod
chmod u+w file_name  # u 代表用户，+代表增加权限，w代表写入权限
```

### 1.7 重定向

STDERR不会随着STDOUT的重定向而发生改变。

文件描述符0代表标准输入，1代表标准输出，2代表标准错误。

```shell
lla badfile 2> test             # 将报错重定向到test文件
&>     # 将标准输出和标准错误重定向到同一文件
```



## 2、进程管理

### 2.1 查看进程

```shell
ps					 # Process ID, 即PID
ps -ef    
# e 显示所有进程， f 显示完整格式的输出
htop				 # 显示进程动态信息
```

### 2.2 结束进程

```shell
kill -9 PID 	# 无条件终止进程
```

### 2.3 处理数据文件

```shell
sort file			# 将每行按照字符顺序排序
-r 						# 反序输出
-n						# 将数字识别成数字而不是字符，按数字排序
```

搜索数据grep

```shell
grep [option] pattern [file]      # 打印包含匹配模式的行。pattern可用正则表达式
```

### 使用历史命令

```shell
history							# 显示历史命令
!数字 							 # 召回指定命令
```



## 3、环境变量

​	所有的环境变量名均使用大写，自己创建的局部变量使用小写字母。

​	变量名、等号和值之间没有空格。

直接通过变量名创建的变量都是局部变量。闯将全局变量需要首先创建局部变量再导出为全局变量。比如

```shell
my_variable="hello world"
export my_variable     # 成为全局变量
```

修改子shell中的全局环境变量不会影响到父shell中该变量的值。

### 3.1 删除环境变量

```shell
# 接上面例子
unset my_variable.   # 不能使用$
```

 一般地，如果用到变量，使用$, ;如果操作变量，不使用$

### 3.2 设置PATH环境变量

```shell
echo $PATH 				   # 查看
PATH=$PATH:/home/christine/scripts     # 追加
PATH=$PATH:.												# 将当前目录加入到PATH环境变量
```

这个修改只能持续到shell退出。

持久化：

- 在`/etc/profile.d`目录中创建一个`.sh`结尾的文件，该目录下的文件全部会执行
- zsh中把在`.zshrc`设置变量



## 4、 shell脚本

 脚本文件的执行，比如文件名为test，进入文件所在的目录，执行`./test`

### 4.1 变量

部分变量通过`${variable}`形式引用，花括号仅仅是用来识别变量名。

给变量赋值时`=`两边不能出现空格，很重要

引用一个变量值时需要使用美元符，而给变量赋值时不要使用美元符。

```shell
echo This is a test    # 不用加引号，仅需要输出单引号时可加双引号
```

### 4.2 命令替换

即从命令输出中提取信息，并赋值给变量。

使用命令替换的两种方式

- 反引号`
- `$()`

```shell
testing=`date`    
testing=$(date)
# 两者效果相同，都会先执行里面的命令，在将输出赋值给testing
```

命令替换会创建一个子shell执行相应的命令，无法使用脚本中创建的变量。（子shell无法使用父shell定义的局部变量）

### 4.3 管道符

```shell
command1 | command2.  # 将命令1的输出作为命令2的输入
# 常见用法是将命令产生的大量输出通过管道传送给more进行分页显示
```

查看脚本退出状态码在执行完命令之后执行`echo $?`; 0代表命令成功结束，1代表一般性未知错误。

### 4.4 bash结构化命令

if-then

```shell
if command
then 
		conmands
fi
```

​	if后面的command会被执行，如果该命令的退出状态码为0则then语句会被执行；fi表示if语句结束。if-then语句的另一种表达形式

```shell
if command ; then 
	commands
fi	
```

if-then-else

```shell
if command
then
	commands
else
	commands
fi	
```

`if`只能根据后面命令的状态码来判断是否执行then语句，可以通过`test`语句增强if语句。

```shell
test condition
# 如果test命令中列出的条件成立，test语句会返回状态码0.否则返回非零状态码
```

`test`可以判断三类条件：数值比价、字符串比较、文本比较

数值比较（即，条件判断）可以很好的配合test语句使用，注意这个是数值比较不是字符串比较，字符串使用常规符号进行比较大小。

`n1 -eq  n2			判断相等 

`n1 -ge n2`		 大于等于

`n1 -gt n2`			大于

`n1 -le n2`			小于等于

`n1 -lt n2`			小于

`n1 -ne n2`           不等于

```shell
if [ contidion ]    # 这种也可以达到test语句的效果，中括号两边必须留空格
then 
	commands
fi
=========
if (( expression ))   # 双括号里面的测试语句可以写成c语言那种
```





















