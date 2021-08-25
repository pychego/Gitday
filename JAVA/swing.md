```java
JFrame frame = new JFrame(); // 创建新框架
JButton button = new Button(); // 创建weight组件
frame.getContentPane().add(button); // 把weight加到frame上面
frame.setSize(300, 300);   // 设置窗口大小
frame.setVisible(true);   // 设置窗口可见
```

设置事件，比如鼠标点击事件，必须右事件执行类去implements特定的接口。将这个类的实例当作参数传到事件源方法中。

​	在frame上面添加画板的方法：创建一个JPanel的子类并覆盖掉paintComponent() 这个方法。

```java
class MyDrawPanel extends JPanel {
  public void paintComponent(Graphcs g) {
    // 新的自己的实现
  }
}
```

这个方法很重要！，系统会自动调用这个方法，不能用户自己调用。

