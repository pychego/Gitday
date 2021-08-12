理解fig, ax = plt.subplots(2，3)作用：

创建一个画布，子图有2*3个，函数返回fig图像和子图ax（轴域）的array列表

常见的画图操作fig, ax = plt.subplots()**建议使用这种写法**等价于

```
fig = plt.figure()
ax = fig.add_subplot(1,1,1)  #最后一个参数1代表第一个子图
```

在此上边绘图只需将plt.plot()换成ax0.plot()即可；ax0=ax[0, 0], plt.plot()没有ax参数

## 常见函数

1. plt.plot()

   

   ```
   plt.plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
   ```

   可以传入多对x和y，不传x时。默认从0开始，steo=1

   fmt：格式控制字符串最多可以包括颜色，点型，线性

   label：可选参数，图例

2. *plt.legend( )*中有*handles*、*labels*和*loc*三个参数，其中：

   **handles**需要传入你所画线条的**实例对象**，这个我也解释不清楚......

   **labels**是图例的名称（能够覆盖在plt.plot( )中label参数值）

   **loc**代表了图例在整个坐标轴平面中的位置（一般选取'best'这个参数值）

   loc是其中最常用的参数，使用help(plt.legend)即可查看可选字符串，一般使用loc=‘

3. 直方图 plot.hist()

```
plt.hist(x, bins=None, density=False, cumulative=False, color=, )
```

x: 可以直接传Series对象

bins：int或list，直方图横坐标区间分组，若传入数字10，则区间等分10份；传入序列，[1,3,5,6]则直方图区间分为[1,3),[3,5),[5,6]

dentisty: 如果是True，绘制并返回一个概率密度

cumulative：若为True，绘制分布函数图像（累加）

## seaborn

2. 通过seaborn.distplot()拟合直方图的曲线分布（参考官方文档）灵活绘制**单变量**观测值分布图。

   ```
   seaborn.displot(a, bins=None, hist=True, kde=True, norm_hist=False, ax=None)
   ```

   a：序列，一维数组或列表

   bins：和plot.hist()中用法相同

   hist：为True则绘制的图形中显示直方图

   kde：为True则绘制的图形中显示拟合曲线

   norm_hist: 和plot.hist()中dendity用法相同

   ax:表示一张画布上的某个轴域（axes）

## ax对标plt

- plt.title() == ax.set_title()
- plt.legend() == ax0.legend()   ax1.legend()















