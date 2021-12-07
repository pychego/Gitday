## Latex常用知识总结

​																												-----基于美赛模版

1. 支持使用中文但不改变原来的英文结构

   ```latex
   \usepackage[scheme=plain]{ctex}
   ```

2. 表格内部换行

   ```latex
   \newcommand{\tabincell}[2]{\begin{tabular}{@{}#1@{}}#2\end{tabular}}
   ```

3. 美赛 latex模板mcmthesis 单独修改目录的行间距----mcmthesis.cls第113行

   ```latex
   \setlength\parskip{.5\baselineskip}%正文的行间距
   \renewcommand\tableofcontents{%
       \setlength\parskip{2.5pt}% 控制目录内的行间距(新加的一句)
       \centerline{\normalfont\Large\bfseries\sffamily\contentsname
           \@mkboth{%
              \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}%
           \vskip 2ex%
       \@starttoc{toc}% 恢复正文的行间距
       \setlength\parskip{.5\baselineskip}%  (新加的一句)
       }
   % 一共新加两句话
   ```

4. 使用\cite命令插入参考文献

   ```latex
   % 将这段话插入到放 References 的地方
   \bibliographystyle{unsrt}   % 按照文献引用顺序排列
   \bibliographystyle{plain}
   \bibliography{file}         % latex目录中bib文件名，即.file.bib
   
   % bib文件模版参考csdn收藏
   ```

5. 图片和表格并列放

   ```latex
   \documentclass{article}  % 可以直接在一个新的tex里面测试
   \usepackage{graphicx}
   \usepackage{floatrow}
   
   \floatsetup{heightadjust=all, floatrowsep=columnsep}
   \newfloatcommand{figurebox}{figure}[\nocapbeside][\dimexpr(\textwidth-\columnsep)/2\relax]
   \newfloatcommand{tablebox}{table}[\nocapbeside][\dimexpr(\textwidth-\columnsep)/2\relax]
   
   \begin{document}
   % 结构开始
   \begin{figure}[htbp]
   \begin{floatrow}[2]
   \figurebox{\caption{Image}}{%
     \includegraphics[width=3cm]{example-image-1x1.pdf}}%
   \tablebox{\caption{Table}}{%
     \begin{tabular}{|c|c|}  % 控制列状态: c 居中，l 靠左， r 靠右;
       \hline
       aa & bb \\ \hline
       cc & dd \\ \hline
     \end{tabular}}
   \end{floatrow}
   \end{figure}
   % 结构结束
   \end{document}
   ```

   

