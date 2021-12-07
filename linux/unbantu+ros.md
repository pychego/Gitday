## ubuntu操作系统从新机配置 + 虚拟机安装ubuntu（M1）+ ros



1. ### 安装更新

   ```shell
   rm -rf ~/.ssh/known_hosts     # 更换操作系统之后操作之后才能ssh
   
   
   apt update
   apt install git
   
   cat /etc/shells        # 查看本机shell
   sudo apt install zsh
   chsh -s /usr/bin/zsh   # zsh路径
   ```

2. 安装Oh-my-zsh

   github 找 zsh-autosuggestions， ohmyzsh，zsh-syntax-highlighting

   ```shell
   # 安装ohmyzsh
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```

3. 安装宝塔面板



### 虚拟机安装ubuntu（M1）+ ros

1. 安装[vwmare for mac m1](https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-2021H1),下载安装之后可能会出现‘未找到文件’的情况，很容易[解决](https://zhidao.baidu.com/question/477768113.html).
2. 下载**arm64**的[ubuntu](https://cdimage.ubuntu.com/releases/20.04/release/)，一定不要看成amd64！！！

![image-20211207195811824](../../Library/Application Support/typora-user-images/image-20211207195811824.png)

3. 拖入iso文件到虚拟机进行安装，安装好了之后是命令行窗口，需要安装可视化桌面：

   ```bash
   sudo apt install tasksel
   sudo tasksel install ubuntu-desltop
   ```

   **注意**：大概半小时完成安装，安装完成之后还是命令行，需要执行`reboot`之后变为可视界面，到此，ubuntu安装完成. 这个可视化方法不适用于本机terminal登陆服务器

4. 进入可视界面后，首先解决本机和虚拟机之间不能复制粘贴的问题

   ```bash
   sudo apt-get autoremove open-vm-tools
    
   sudo apt-get install open-vm-tools-desktop
   ```

   

   ### 安装ros

   进入[ros官网](http://wiki.ros.org/noetic/Installation/Ubuntu)安装步骤

1. 如果这个source.list不行的话，就用清华源的，官网有给出

   ```bash
   sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
   ```

2. ```bash
   sudo apt install curl # if you haven't already installed curl
   curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
   ```

   第二句话执行很可能报错，因为识别不了管道符。可以先执行前一步再执行后一步，但是我不是这样来的。虚拟机curl很慢，就直接在本机上操作

   ```bash
   curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc >> a.txt
   ```

   之后将`a.txt`文件内容剪切到虚拟机中的同名文件，在虚拟机中执行

   ```bash
   sudo apt-key add a.txt
   ```

   到这里添加成功！剩下的跟着官网步骤走，直到初始化这一步，可以[reference](https://mp.weixin.qq.com/s/VGs8oWdhHH6XsHcx21lN4Q).

   ```bash
   sudo pip install rosdepc  或者 sudo pip3 install rosdepc
   # 如果没有pip
   sudo apt-get install python3-pip 
   sudo pip install rosdepc
   # 初始化
   sudo rosdepc init
   rosdepc update
   ```

   到此，整个安装过程完成！

