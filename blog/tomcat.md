

**CentOS安装配置tomcat**

## 1、安装jdk

我是先把原来的jdk卸载了，原来jdk的路径可以用`which java`查看。

去官网下载[jdk](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html#license-lightbox)，我用了宝塔面板把文件上传到linux，放到了`/usr/local`目录下面并解压

## 2、安装tomcat

[官网](https://tomcat.apache.org/download-90.cgi)，下载tar.gz文件，和上面一样放到`/usr/local`目录下面并解压

![image-20210910091611321](/Users/chegopy/Library/Application Support/typora-user-images/image-20210910091611321.png)

### 3、配置环境变量

在这个上面折腾了一晚上才成功，具体就是启动了之后访问不了8080端口。

两个都安装好了之后执行`vim /etc/profile`

我是在后面追加了

```bash
JAVA_HOME=/usr/local/jdk1.8.0_301
JRE_HOME=/usr/local/jdk1.8.0_301
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
CLASSPATH=:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
export JAVA_HOME JRE_HOME PATH CLASSPATH

CLASSPATH=$JAVA_HOME/lib/
CATALINA_HOME=/usr/local/tomcat
PATH=$PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin
export PATH JAVA_HOME CLASSPATH CATALINA_HOME
```

保存之后执行`source /etc/profile`

到这里还是不行，进入`/usr/local/tomcat/bin`目录，打开`setclasspath.bat`

在文件最上面添加`set JAVA_HOME=/usr/local/jdk1.8.0_301`

我的端口提前都已经开放好了，重启了服务器，进入tomcat的bin目录`cd /usr/local/tomcat/bin`

执行`./startup.sh`

![image-20210910092609279](/Users/chegopy/Library/Application Support/typora-user-images/image-20210910092609279.png)

以前环境变量没设置好时，显示的结果也是这个，但是访问不了8080端口，这次就好了。

