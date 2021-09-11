**Mac OS X + MAMP 配置mysql的my.cnf配置文件**

MAMP自身没有my.cnf文件，需自己创建，/Applications/MAMP/conf/my.cnf ，在这个路径创建my.cnf文件。我是需要和外部文件进行交互，文件内容如下：

![img](https://img-blog.csdnimg.cn/20210909230111639.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcHljaGVnbw==,size_20,color_FFFFFF,t_70,g_se,x_16) 

在mysql中进行测试：

<img src="https://img-blog.csdnimg.cn/20210909230133168.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAcHljaGVnbw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom: 50%;" /> 

显示为空则表示成功！