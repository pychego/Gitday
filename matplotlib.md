理解fig, ax = plt.subplots(2，3)作用：

创建一个画布，子图有2*3个，函数返回fig图像和子图ax（轴域）的array列表

在此上边绘图只需将plt.plot()换成ax0.plot()即可；ax0=ax[0, 0], plt.plot()没有ax参数

常用函数

1. 直方图 plot.hist()

   ```
   plot.hist(x, bins=None, density=False, cumulative=False, color=, )
   ```

   x: 可以直接传Series对象

   bins：int或list，直方图横坐标区间分组，若传入数字10，则区间等分10份；传入序列，[1,3,5,6]则直方图区间分为[1,3),[3,5),[5,6]

   dentisty: 如果是True，绘制并返回一个概率密度

   cumulative：若为True，绘制分布函数图像（累加）

2. 通过seaborn.distplot()拟合直方图的曲线分布（参考官方文档）

   ```
   seaborn.displot(a, bins=None, hist=True, kde=True, norm_hist=False, ax=None)
   ```

   a：序列，一维数组或列表

   bins：和plot.hist()中用法相同

   hist：为True则绘制的图形中显示直方图

   kde：为True则绘制的图形中显示拟合曲线

   norm_hist: 和plot.hist()中dendity用法相同

   ax:表示一张画布上的某个轴域（axes）



