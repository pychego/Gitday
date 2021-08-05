<<<<<<< HEAD
/*
初始化函数
	void SR04_Init()
	功能：超声测距模块初始化
	输入参数：无
	输出参数：无
功能函数
	float GetDistance()
	功能：测距
	输入参数：无
	输出参数：距离，单位：cm,浮点类型数据

*/

#define TrigPin  A4
#define EchoPin  A5

void SR04_Init()
{
  pinMode(TrigPin, OUTPUT);
  // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
  pinMode(EchoPin, INPUT);
}
// 单位CM
float GetDistance()
{
  // 产生一个10us的高脉冲去触发TrigPin
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
  float ret= pulseIn(EchoPin, HIGH,5000) / 58.00;
  if(ret==0)
    ret=1000;
  return ret;
}
=======
/*
初始化函数
	void SR04_Init()
	功能：超声测距模块初始化
	输入参数：无
	输出参数：无
功能函数
	float GetDistance()
	功能：测距
	输入参数：无
	输出参数：距离，单位：cm,浮点类型数据

*/

#define TrigPin  A4
#define EchoPin  A5

void SR04_Init()
{
  pinMode(TrigPin, OUTPUT);
  // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
  pinMode(EchoPin, INPUT);
  /*将引脚设置为不同模式，将决定其在程序中如何工作。
   * 当引脚设置为输出模式时，引脚为低阻抗状态。这意味着
   * 通过它可以向其它电路元器件提供电流，可以点亮LED或者驱动电机。
   * 当引脚设置为输入模式时，引脚为高阻抗状态。
   * 此时该引脚可用于读取传感器信号或开关信号。

*/
}
// 单位CM
float GetDistance()
{
  // 产生一个10us的高脉冲去触发TrigPin
  digitalWrite(TrigPin, LOW);
  //设置引脚输出电平高低，在此函数之前，需要指定引脚是输出模式
  delayMicroseconds(2);   //作用类似delay(),参数单位为微秒
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
  float ret= pulseIn(EchoPin, HIGH,5000) / 58.00;
  // pulseIn()求得的是时间，单位微秒，实际距离一厘米对应58微秒，因此除以58
  if(ret==0)
    ret=1000;
  return ret;
}
>>>>>>> test
