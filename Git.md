#### **名词解释**

Working Directory  工作区，即目录

Repository  版本库，仓库





#### **基础操作**

modified  改动过的

unstage    撤销

```
git log                        ; 查看提交日志
git reflog                     ; 查看你的每一次命令
git status                     ; 查看分支状态,没事多用这个
git diff HEAD -- <file name>   ; 查看工作区和版本库中版本差异
```

stage是暂存区

![git-repo](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

=============================

#### **版本操作/管理修改**

HEAD指针指向当前版本, HEAD^表示上个版本, HEAD^^以此类推

```
git reset --hard HEAD^           ; 回退到上个版本
git reset --hard <commit id>     ; 回到指定版本
```

```
git checkout -- file             ; 丢弃工作区的修改
```

该命令让文件回到最近一次commit或add的状态

```
git reset HEAD <file>            ; 撤销放到暂存区的修改
```



========================

#### **分支**

```
git cheakout -b <branch name>      ;创建并切换到分支
```

```
git branch <branch name>           ;创建分支
git checkout  <branch name>        ;切换到当前分支
git switch  <branch name>          ;功能同上
```

```
git branch                         ;查看当前所有分支
```

```
git branch -d  <branch name>       ;删除指定分支
```

```
git branch -D <branch name>        ;强行删除一个没有个合并过的分支
```



1. git cheakout -b <branch name>  创建分支并切换到这个分支
    相当于 git branch <branch name>   创建分支
           git checkout <branch name>  切换分支
2. git branch  查看当前所有分支
3. git checkout <branch name> 或   git switch <branch name>
 切换到指定分支
4. git merge <branch name> 用于合并指定分支到当前分支
5. git branch -d <branch name> 删除指定分支

   6.git branch -D <branch name> 强行删除一个没有合并过的分支

========================

#### **保存现场**--stash

1. 在当前分支的更改commit或者stash之前,是不能切换分支的
2. dev分支更改或者添加的内容stash或者commit之后再切换到其他分支,
在其他分支看不到dev的更改,只有两个分支合并之后才能在main看到之前dev上面的更改
3. 合并冲突, 当两个分支的更改是冲突的,执行合并本身就是一次
    commit, (执行合并之后就默认了你已经更改冲突)可以忽视冲突,
    再add,然后再进行一次commit



```
git stash                           ;可以在任何工作状态保存现场
```

```
git stash list                      ;查看保存的现场列表
```

$ git stash   可以在任何工作状态保存现场

$ git stash list   查看保存的现场列表

**两种恢复现场并删除stash的方法**

```
git stash apply stash@{数字}         ;恢复现场, 但是stash并没有删除
git stash drop                      ; 接着上一条命令,就会只删除已经恢复现场的stash
```

```
git stash pop                        ; 弹出现场的同时删除stash    .....是不是弹出最近的stash???
```







1. 
$  git stash apply stash@{ 数字 }   恢复现场, 但是stash并没删除
$  git stash drop 删除(接着上一条命令,就会只删除已经恢复现场的stash)

2. 
$ git stash pop  弹出现场的同时删除stash



============================

#### **推送/抓取分支**

@@@把本地文件不断补充上传的时候会经常用这个功能

```
git remote -v                       ;查看远程库信息
```

```
git push origin <branch name>       ; 把该分支上的本地提交推送到远程库
```





1. git remote -v  查看远程库信息

2. git push origin <branch name>  把该分支上的所有本地提交推送到远程库

========================

#### **分支合并**

fast-forward

如果待合并的分支在当前分支的下游，也就是说没有分叉时，会发生快速合并，从test分支切换到master分支，然后合并test分支

```
git chaeckout master
git merge test
```

![img](http://yanhaijing.com/blog/498.gif)



no-ff

如果不想要快速合并，那么我们可以强制指定为非快速合并，只需加上`--no-ff`参数

```
git checkout master
git merge -no-ff test
```

注意在master分支新建了一个comit

![img](http://yanhaijing.com/blog/499.gif)

squash

squash和no-ff非常类似，区别只有一点不会保留对合入分支的引用

```
git checkout master
git merge -squash test
```

![img](http://yanhaijing.com/blog/500.gif)



rebase

当要合并两个分叉的分支时，merge的方式是将待合入分支和当前分支不同的部分，在当前分支新建节点，如下图所示

![img](http://yanhaijing.com/blog/501.png)



rebase与merge不同，rebase会将合入分支上超前的节点在待合入分支上重新提交一遍，如下图，B1 B2会变为B1’ B2’，看起来会变成线性历史

![img](http://yanhaijing.com/blog/502.png)



cherry-pick

想把那个节点merge过来就把那个节点merge过来，其合入的不是分支而是提交节点

```
git cherry-pick <commit id>         ;单独合并一个提交
```

```
git cherry-pick <start commit id>..<end commit id>
git cherry-pick <start commit id>^..<end commit id>
```

前者表示把左开右闭的几次提交pick到当前分支

后者表示把包含开始的commit pick到当前分支





git merge <branch name> 将指定分支的修改归并到当前分支
这个操作会在该分支产生一个新的commit
 例子,   
 $ git checkout master
 $ git merge test 
 test 分支没有变化, test内容合并到master,master向前进一个提交

1. git rebase <branch name> 将当前节点的工作直接移到指定节点
    @@@图解4种git合并分支方法（转载）看csdn收藏讲的很详细
2. 
   ​        



========================
**创建标签**

1. git tag <tagname>  用于新建一个标签,默认为HEAD,(当前分支的最近一次提交)
也可以在后面追加commit id进行指定
2. git tag -a <tag name> -m'blablabla...' 可以指定标签信息
3. git tag 可以查看所有标签
4. git push origin <tagname> 推送一个本地标签到远程
5. git push origin --tags  可以推送全部未推送过的本地标签
6. git tag -d <tagname>可以删除一个本地标签；
7. git push origin :refs/tags/<tagname>可以删除一个远程标签。





其他小技巧

cat <file>  查看文件内容

git diff   查看文件更改的地方