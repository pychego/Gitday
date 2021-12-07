## **数据结构**

- Series对象：类似一维数组对象

  ```python
  s = pd.Series(['猫', '狗', '兔', '鼠'])     #创建Series对象
  ```

- DataFrame对象： 类似表格

  ```python
  df= pd.DataFrame(object, columns=None, index=None)
  #object是二维数组，columns设置列标签， index设置行标签
  df.dtypes       #查看不同列的dtypes
  DataFrame.to_numpy()给出底层数据的 NumPy 表示,不包括index和columns
  ```
  
  **NumPy 数组对整个数组有一个 dtype，而 pandas DataFrames 每列有一个 dtype**。

## **读取、保存数据**

```python
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
```



- 读取Excel、csv工作簿数据

  ```python
  df = pd.read_excel('xxx.xlsx', sheet_name=None, header=0, index_col=None, usecols=)
  #usecols 默认解析所有列，可以传入由列索引组成的数组，解析指定列
  #header=0表示使用数据表的第0行内容作为列标签
  #index_col=0表示使用数据表的第0列内容作为行标签，默认为None
  #当有多个sheet时，指定None读入所有
  df = pd.read_csv('xxx.csv')  # 默认不加参数即可
  ```

- 显示索引、列

  ```python
  df.index
  df.columns
  df.count()   
  ```

- 读取指定列

  ```python
  pd.read_excel('xxx', usecols=[])   #usecols的值为一个列表，读取指定列
  ```

- 数据预览

  ```python
  df.head(n=5)       #head()不含参数表示读取前5行，带参数100表示读取100行
  df.tail()       #读取最后5行
  df.shape        #返回数据行列数元组,是属性，而不是方法
  df.dtypes       # 获取每列的类型
  df.info()       #查看数据类型，每一列有多少NaN，较全面
  df["省份"].value_counts()    # 查看有多少省份，以及每个省份多少人,返回Series对象
  df["省份"].unique()
  df.describe()   # 获取基本统计量
  # 注意，这里面好几个函数需要print才有输出
  ```

- 转换特定列的数据类型

  ```
  df['学号'] = df['学号'].astype('string')
  ```

  把学号转换为string可以避免保存文件时学号被用认为是数字用科学计数法表示

- 保存文件

  ```
  df.to_excel(self, excel_writer, sheet_name='Sheet1', na_rep='', columns=None,  index=True,inf_rep='inf')
  ```

  - excel_writer :指定文件导出路径与文件名；
  - sheet_name : 指定Sheet名称；
  - inindex ：设置是否使用自然数索引，默认使用；一般都是不使用
  - columns : 指定要导出的列；
  - na_rep : 设置缺失值的填充；
  - inf_rep : 设置无穷值inf的填充值

## **选择数据**

iloc和loc后面只有一个数时，都是选择的某一行的数据

- 选择单行数据

  ```python
  df.loc['行标签']
  df.iloc[3]        # 根据行号选择单行数据，从0开始
  ```

- 选择多行数据

  ```python
  df.loc[['行标签1', '行标签2']]
  df[2:5]         #切片，选择3条数据
  df.iloc[[3, 4]]      #选择第4行和第5行
  df.iloc[1:5]         #选择第2～5行
  ```

- 按条件选择行

  ```
  a = df['毕业中学'] == '原阳县第一高级中学'
  df[a]
  ```

- 选择列数据

  ```python 
  df['毕业中学']               #通过列标签选择单列数据
  df[['生源地', '毕业中学']]		 #选择多列数据
  df.iloc[:, [1, 3]]          #选择第2、4列
  df.iloc[:, 1:3]             #选择第2、3列，切片
  ```

- 同时选择行列

  ```
  df.iloc[1:5, 1:5]           #切片也可以由行列号数组替换
  ```
  
- 查看不同专业人数


- ```
  df['专业'].count_values()
  ```




### 修改行标签和列标签

```
df.set_index('学号')         #将'学号'作为行标签
df = df.rename(column={'原行标签': '新标签'...}, inplace=True)
#inplace=True 代表直接修改原对象
```

---

## **高级用法**
### 数据的查找替换

1. len(df)可以查看一共多少条数据

- isin()函数可以查看DataFrame是否包含某个值，返回True，False组成的数组

  也可以用来直观查找数据

  ```
  df[data['毕业中学'].isin('原阳县第一高级中学'])
  ```

#### 替换修改

dataframe.apply(function,axis)对一行或一列做出一些操作（axis=1遍历行，axis=0遍历列），可以用匿名函数

```python
Series.where(condition, other=nan, inplace=False)
# 如果 condition 为真，保持原来的值，否则替换为other， inplace为真标识在原数据上操作，为False标识在原数据的copy上操作。other的形状必须与self相同。
# 注意是条件为真保持原来不变
```



- 一对一替换

  ```python
  	df.replace('原内容', '新内容')
  	#该操作不改变df，而是生成新的对象；将replace()参数inplace=True则改变df
  ```

- 多对一替换

  ```python
  df.replace(['原1'，'原2'], '新1')   #将原1、原2都替换成新1
  ```

- 多对多替换

  ```python
  df.replace({'原1': '新1', '原2': '新2'})
  ```

### **数据的处理修改**

- 按条件修改

  可以按这个方法把脱敏的学号再变回原来的

  ```
  df[df > 0] = -df  #把所有的正数变成相反数
  ```

  

- 插入数据

  ```
  #插入列数据(也可以直接赋值)
  df.insert(2, '列名'， ['元素1'，..])
  df['列名'] = ['元素1'，..]
  ```

  

  ### 数据清洗

  ```python
  df.dropna(subset=['毕业中学'])		# 放弃这列空白所对应的记录
  df.drop('毕业中学', axis=1)			  # 放弃有空白值的整个列
  df['毕业中学'].fillna(value)			# 将空白用特定值填充
  ```

  

  **删除空白数据**（使用drop()方法删除，必须指定要删除的行/列索引）

  `pandas`模块的drop()函数既可以删除指定的行，也可以删除指定的行，注意不改变原对象，而是返回新对象

  ```python
  df.drop(['列名1','列名2'], axis=1, inplace=True)   # axis=1处理列，axis=0处理行
  df.drop(df.columns[[2,5]], axis=1)
  df.drop(columns=['列名1', '列名2'])
  # 三者功能相同，axis用于指定第一个参数给出的是行标签还是列标签
  # 删除行时，axis参数可以省略
  df.drop(index=['行号1', '行号2'])
  # 更实用的方法，删除满足条件元素所在的行
  df = df.drop(df[<some boolean condition>].index)
  df = df.drop(df[df['专业'] == '航空航天类'].index)
  # 注意drop的参数是索引
  ```

  df.drop(self, *labels=None*, *axis=0|1*, *index=None, columns=None*, *level=None,* *inplace=False|True, errors='raise| ignore'*)

  labels : 列名称 或者 行|列索引号

  labels, axis=0 等价于 index=labels ;

  labels, axis=1 等价于 columns=labels

  *inplace=False|True* : 是否替代原来的df, 默认False(不替代)

  *errors='raise| ignore' :* 是否忽略错误, 默认raise(报错), ignore为跳过错误继续运行

  *level* 用于多重index,第几层

  在python/pandas中，缺失值一般用NaN表示

  1. 删除缺失值，dropna()函数可以删除表中含有缺失值的行，默认只要有缺失值，就删除整行；

     参数设置为how='any'只删除整行都为缺失值的行

  2. 填充缺失值

     ```python
     df.fillna(value=0)     #将缺失值填充为0
     df.fillna({'列名1':0, '列名2':1})    #不同列填充不同的值
     ```

- 处理重复值

  1. 删除重复行

     ```python
     df.drop_duplicates()       #删除完全重复的行
     df.drop_duplicates(subset='列名1')    #删除某一列的重复值
     #参数keep指定为'first',保留第一个重复值；为'last',保存最后一个重复值
     #为False，删除所有重复值
     
     ```
     
  2. 获取唯一值

     ```python
     df['列名1'].unique()              #获取指定列数据的唯一值
     ```
  
- 排序函数

  ```python
  #按axis排序
  df.sort_index(axis=1, ascending=False)  
  #按值排序
  df.sort_values(by='列名1', ascending=True)   #升序或者降序
  ```

- 数据表的拼接

  1. 根据公共列拼接**两个**DataFrame对象,不能一次拼接三个对象

     ```python
     a = pd.merge(df1, df2, how=, on='列名')   
     #how='outer'可以指定两表取并集
     #on参数指定合并依据的列，两对象只有一个相同列是不用指出
     ```

  2. 直接在一个表的后面追加表格

     ```python
     e = pd.concat([data1, df2], ignore_index=True)
     #参数为True表示将两个表的行标签合在一起
     f = df.append(df2, ignore_index=)
     ```

- 统计计算(参数为1时，进行另一个轴的统计计算)

  ```
  df['列名'].sum()
  df['列名'].mean()
  df['列名'].max()
  df['列名'].min()
  df.describe()   #获取数据的个数，均值，最值，方差等
  df.corr()       #计算各列之间的相关系数
  ```

  

### 数据透视表

1. 堆叠

   表格在行列方向上均有索引（类似于DataFrame），花括号结构只有“列方向”上的索引（类似于层次化的Series），结构更加偏向于堆叠（Series-stack，方便记忆）。stack函数会将数据从”表格结构“变成”花括号结构“，即将其行索引变成列索引，反之，unstack函数将数据从”花括号结构“变成”表格结构“，即要将其中一层的列索引变成行索引。

2. pd.pivot_table()  （功能和groupby可以相互取代）参考csdn收藏

   ```
   pd.pivot_table(df, index=, aggfunc='mean', values=, columns)
   ```

   df: DataFrame对象


   index：可以接受一个列表作为多级索引，如果要显示所有的文本列，就要把他们的列索引全部写进去

   aggfunc：默认是mean(), 可以接受列表传入多个函数

   values：整理之后的列索引

   columns：接受参数：原来的列索引，将该列的值去重之后作为第二级列索引



## 易错知识点

1. data是只有一列数据（加权成绩）的DataFrame对象，data和data['加权成绩']是不一样的，后者是Series
