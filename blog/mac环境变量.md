## mac每次打开终端需要重新配置环境变量的解决办法

在 ~/.bash_profile 中配置环境变量, 每次重启终端后配置的环境变量不生效。需要重新执行 : $source ~/.bash_profile才可以。是因为zsh加载的是 ~/.zshrc文件，而 ‘.zshrc’ 文件中并没有定义环境变量。

在终端执行：

```bash
vim ~/.zshrc
```

进入文件之后，在最后一行加上  `source ~/.zshrc`

ok!

