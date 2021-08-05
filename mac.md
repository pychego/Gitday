1. conda安装的库路径

   ```
   .conda/envs/python3/lib/python3.8/
   ```

   如果这个目录不能直接找到，可以继续打开site-packages

2. 自己安装的python3.9下载的库位置

   ```
   HD/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
   ```

conda安装的是python3.8，自己安装的是3.9，which python 可以查看安装位置

最最简单的方法查看库安装的位置

```
import pandas
print(pandas)
```



3. shift + command + . 显示隐藏文件夹