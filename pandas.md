## **数据结构**

- Series对象：类似一维数组对象

  ```python
  s = pd.Series(['猫', '狗', '兔', '鼠'])     #创建Series对象
  ```

- DataFrame对象： 类似表格

  ```python
  df= pd.DataFrame(object, columns=None, index=None)
  #object是二维数组，columns设置列标签， index设置行标签
  ```

## **读取、保存数据**

- 读取Excel工作簿数据

  ```python
  data = pd.read_excel('xxx.xlsx', sheet_name=None, header=0, index_col=None)
  #header=0表示使用数据表的第0行内容作为列标签
  #index_col=0表示使用数据表的第0列内容作为行标签，默认为None
  ```

- 读取csv文件

  ```python
  data = pd.read_csv('xxx.csv')
  ```

- 读取指定列

  ```python
  pd.read_excel('xxx', usecols=[])   #usecols的值为一个列表，读取指定列
  ```

- 查看特定行列

  ```python
  data.head()       #head()不含参数表示读取前5行，带参数100表示读取100行
  data.shape        #返回数据行列数元组
  data.indo()       #查看数据类型，每一列有多少NaN，较全面
  ```

- 转换特定列的数据类型

  ```
  data['学号'] = data['学号'].astype('string')
  ```

  把学号转换为string可以避免保存文件时学号被用认为是数字用科学技术法表示

- 保存文件

  ```
  df.to_excel(self, excel_writer, sheet_name='Sheet1', na_rep='', columns=None,  index=True,inf_rep='inf')
  ```

  - excel_writer :指定文件导出路径与文件名；
  - sheet_name : 指定Sheet名称；
  - index ：设置是否使用自然数索引，默认使用；一般都是不使用
  - columns : 指定要导出的列；
  - na_rep : 设置缺失值的填充；
  - inf_rep : 设置无穷值inf的填充值

## **选择数据**

- 选择单行数据

  ```python
  data.loc['行标签']
  data.iloc[3]        #根据行号选择单行数据，从0开始
  ```

- 选择多行数据

  ```python
  data.loc[['行标签1', '行标签2']]
  data.iloc[[3, 4]]      #选择第4行和第5行
  data.iloc[1:5]         #选择第2～5行
  ```

- 按条件选择行

  ```
  a = data['毕业中学'] == '原阳县第一高级中学'
  data[a]
  ```

- 选择列数据

  ```python 
  data['毕业中学']               #通过列标签选择单列数据
  data[['生源地', '毕业中学']]		 #选择多列数据
  data.iloc[:, [1, 3]]          #选择第2、4行
  data.iloc[:, 1:3]             #选择第2、3行，切片
  ```

- 同时选择行列

  ```
  data.iloc[1:5, 1:5]           #切片也可以由行列号数组替换
  ```

### 修改行标签和列标签

(比较鸡肋)

```
data.set_index('学号')         #将'学号'作为行标签
data = data.rename(column={'原行标签': '新标签'...})
```

---

## **高级用法**









