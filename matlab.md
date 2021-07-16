2

```matlab
clc
clear
x = [1 2 3 4 5];
y = [129747 140618.30 150986.70 161456.30 180385.30];
z = polyfit(x, y, 2);
plot_x = linspace(1, 5, 100);
predict_y = polyval(z, plot_x);
scatter(x, y, 'r')
xticks([1 2 3 4 5])
xticklabels({'2008年第1季度', '2010年第1季度', '2012年第1季度', '2014年第1季度', '2016年第1季度'})
str = "2015年第1季"+newline+"预测国民生产总值:171245";
text(4.5, polyval(z, 4.5),str)
xtickangle(20)
hold on
plot(plot_x, predict_y, 'b--')
xlabel("季度")
ylabel("国民生产总值")
title("我国国民生产总值")
```

3

```

```

4

```
clc
clear
A=[-4 1 2;1 -5 3; 2 0 -6]
B=[1;0.5;2]
C=[2 1 2]
D=[0]
[m,n]=size(A);  
[x,y]=size(B);
a=zeros(1,m);  
 R=eye(m);
 K=eye(m);
 P=R*A;
 a(1)=-trace(P)/1; 
for i=2:m
    R=R*A+a(i-1)*K;
    P=R*A;
    a(i)=-trace(P)/i;
end   %求取出n个特征多项式
cab=zeros(m-1,y);
cab(1,:)=C*A*B;
for i=2:m-1
    T=A^i;
    cab(i,:)=C*T*B;
end 
b=zeros(m,y);
b(1,:)=C*B; 
for i=2:m
    pk=0;
    for j=1:i-2
        pk=a(j)*cab(i-1-j,:)+pk;
    end
    b(i,:)=cab(i-1,:)+pk+a(i-1)*C*B;
end
a
b
```

5

```
clear all;
close all;
a0 = [9]       %开环分子
b0 = [1 3 9]   %开环分母
aa = a0        %闭环分子
bb = b0 + a0   %闭环分母
disp('System Closed Loop Tranfer Function is:')
aa
bb
sys=tf(aa,bb)
nyquist(a0, b0)  %判断稳定性
figure(2)
step(sys)
```

