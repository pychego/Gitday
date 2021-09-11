整了三四天才终于让我弄好了YouCompleMe的安装编译。

直接在github的YouCompleMe仓库里面按照教程进行[安装](https://github.com/ycm-core/YouCompleteMe)，在macOS模块按照作者的教程一步一步进行，最后进行到

```bash
cd ~/.vim/bundle/YouCompleteMe
./install.py
```

到这一步没有问题，但是这时候的补全只有id什么的，完全没有和库函数什么的联系起来，最终的效果就是下面的这种

<img src="/Users/chegopy/Library/Application Support/typora-user-images/image-20210905131235860.png" alt="image-20210905131235860" style="zoom:50%;" />

我又在github上面闲逛，又找到了一个作者的[仓库](https://github.com/yangyangwithgnu/use_vim_as_ide),在其中配置YouCompleMe的时候，提到了怎么安装和配置YouCompleMe。

我大致步骤按照这个来，但是一个人整也弄了很长时间。

安装好了YouCompleMe之后，去github下载[libclang预编译二进制文件](https://github.com/llvm/llvm-project/releases/tag/llvmorg-12.0.0),我下载的是

![image-20210905131910519](/Users/chegopy/Library/Application Support/typora-user-images/image-20210905131910519.png)

解压之后就按照以下步骤

```bash
cd ~/downloads/ 
mkdir ycm_build 
cd ycm_build 
cmake -G "Unix Makefiles" -DUSE_SYSTEM_BOOST=ON -DPATH_TO_LLVM_ROOT=~/downloads/clang+llvm/ .\
 ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp
cmake --build . --target ycm_core
```

这里面最后一步可能会报错，不用管他。弄好了之后就执行

```bash
cd ~/.vim/bundle/YouCompleteMe
./install.py --clangd-completer
```

到这里就可以达到上图的效果了。