arr为np.array对象

axis=0, 表示以行为单位添加或删除； axis=1，表示以列为单位添加或删除

```python
np.array(object, dtype=None)   #传入数组参数，创建数组对象
np.arange(start, stop, step, dtype=None)
#左闭右开，仅stop为必须参数
np.random.rand(obj)  #创建0～1随机数的数组
```

### **属性**

1. arr.shape    #查看数组的行列数
2. arr.size       #返回数组元素个数
3. arr.dtype    #返回元素类型
4. arr.ndim     #返回数组维数

## **数组的重塑与转置**a.reshape()    #数组的重塑

```python
arr.reshape()    #数组的重塑
```

```python
arr.flatten() 或者 arr.ravel()   #将多维数组转化为一维数组
```

```python
arr.transpose()   #arr的转置
```

属性

1. T  #转置

## **数组元素的添加删除**

```python
np.append(arr, values, axis=None)
#未指定axis则先展开arr为一维，axis=0，添加行；axis=1，添加列
```

```python
np.insert(arr, obj, values, axis=None)
#未指定axis则先展开arr为一维，obj表示元素插入位置， values插入的数组
```

```python
np.delete(arr, obj, axis=None)     #参数类似
```

## **数组元素的处理**

```python
np.nan   #代表缺失值
arr[np.isnan(arr)] = 0   #将arr中的缺失值填充为0
```

```python
np.unique(arr)   #用于处理重复值
```

```python
#拼接数组
np.concatenate((arr1, ...,  arr2), axis=0)   
#np.hstack()和np.vstack()可以由上面函数代替
```

```python
#拆分数组
np.split(arr, obj, axis=0)
#obj为数字表示平均份数，为数组表示拆分的索引
```

### **数组计算**

1. 形状相同的数组加减乘除，即他们对应元素的加减乘除

### **统计计算**

```python
#求和
arr.sum(axis=None)
#默认对整个数组求和，axis=0，对每一列求和；axis=1，对每一行求和
#求平均值
arr.mean()
#求极值
arr.max()  arr.min()
```







![img](https://img-blog.csdnimg.cn/20190828160900248.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3NDYxNDE2,size_16,color_FFFFFF,t_70)

