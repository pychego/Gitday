//循迹传感器获取函数定义(这样定义可以使代码简洁)
#define TL2 GetL2()
#define TL1 GetL1()
#define TR1 GetR1()
#define TR2 GetR2()
#include <Servo.h>

#define LDR_Rev A6//光敏接收IO
Servo myservo;//实例化舵机
#define SERVO 9//设置舵机控制IO
#define MIDDLE_ANGLE 80//设置舵机中位（平衡）角度
#define WINDOW 7//设置平均数窗口大小

int flag = 1;

#define IR_Rev A1//红外接收IO

#include <Adafruit_NeoPixel.h>

#define PIN            A0//定义彩色LED使用的引脚
#define NUMPIXELS      4//使用LED的数量
Adafruit_NeoPixel pixels =
  Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int flag = 0;
void setup() {
  // put your setup code here, to run once:
  carInit();//电机初始化
  trackSensorInit();//循迹传感器初始化
  printfInit(9600);
  Serial.begin(115200);//初始化串口
  OLED_Init();//初始化OLED
  SR04_Init();//超声测距模块初始化
  myservo.attach(SERVO);       // 选择控制的舵机的IO
  myservo.write(MIDDLE_ANGLE); // 指定舵机转向的角度

  pinMode(IR_Rev, INPUT); //设置红外光敏二极管所在IO输入

  pixels.begin();//初始化WS2812 LED


}

void loop() {
  // put your main code here, to run repeatedly:

  int irRev;
  irRev = analogRead(IR_Rev);
  if (flag == 0 && irRev > 50) {
    flag = 1;
    led();
    delay(1000);
  }
  else if (flag == 1)
  {
    track();
  }
  else if (flag == 2)

  {
    light_seeking();
  }
}

void track() {

  printf("%d %d %d %d\r\n", TL2, TL1, TR1, TR2);
  if (TL1 == 0 && TR1 == 1) //左内侧传感器发现黑线
  {
    carMove(-180, 180);//左转
    //      delay(30);
  }
  else if (TL1 == 1 && TR1 == 0)
  {
    carMove(180, -180);//右转
    //      delay(30);
  }
  else if (TL2 == 1 && TR2 == 0) //右外侧传感器发现黑线
  {
    carMove(170, -170); //右大转
    delay(10);
  }
  else if (TL2 == 0 && TR2 == 1) //左外侧传感器发现黑线
  {
    carMove(-170, 170); //左大转
    delay(10);
  }
  else
    carMove(160, 160); //前进

  if (TL1 == 0 && TL2 == 0 && TR1 == 0 && TR2 == 0 )
  {
    flag = 2;
    carMove(0, 0);
    delay(20);
  }

}

void led() {
  int c1, c2, c3;
  for (int i = 0; i < 32; i++)
  {
    c1 = i; //颜色1
    c2 = 32 - i; //颜色2
    if (i > 16)
      c3 = (i * 2) - 32; //颜色3
    else
      c3 = 32 - (i * 2); //颜色3
    /*
      设置LED颜色
      参数0 选择控制哪一颗LED，从0开始
      参数1 LED的R、G、B颜色
    */
    pixels.setPixelColor(0, pixels.Color(c1, c2, c3));
    pixels.setPixelColor(1, pixels.Color(c2, c3, c1));
    pixels.setPixelColor(2, pixels.Color(c3, c1, c2));
    pixels.setPixelColor(3, pixels.Color(c1, c3, c2));
    pixels.show(); //显示设定的颜色


  }
}
  void light_seeking() {
    static unsigned char addFlag = 1;//角度加减标志，用这个标志控制舵机角度是增加还是减少
    static int servoAngle = MIDDLE_ANGLE;//舵机角度
    delay(1000);
    int angleList[90];
    int ap = 0;
    int halfWindow = (WINDOW - 1) / 2;
    //把要转的角度放入数组
    for (int i = -44; i <= 45; i++)
      angleList[ap++] = i;
    int lightList[90 + WINDOW - 1]; //存放原始亮度信息，长度增加窗口
    //测量原始亮度信息
    for (int i = 0; i < 90; i++) {
      servoAngle = MIDDLE_ANGLE + angleList[i];
      myservo.write(servoAngle); // 指定舵机转向的角度
      delay(20);//延时给舵机运行的时间
      int ldrRev;
      ldrRev = analogRead(LDR_Rev);
      lightList[i + halfWindow] = ldrRev;
    }
    //为亮度信息数组前后各补充半个窗口的数据
    for (int i = 0; i < halfWindow; i++)
    {
      lightList[i] = lightList[halfWindow];
      lightList[90 + WINDOW - 1 - 1 - i] = lightList[90 + WINDOW - 1 - 1 - halfWindow];
    }
    //计算滑动窗口内亮度均值
    int avgLightList[90];
    for (int i = halfWindow; i < 90 + halfWindow; i++)
    {
      int sum;
      sum = 0;
      for (int j = i - halfWindow; j <= i + halfWindow; j++)
        sum += lightList[j];
      avgLightList[i - halfWindow] = sum /= WINDOW;
    }

    //寻找最高亮度以及对应的角度
    int maxLight, maxi;
    maxLight = 0;
    maxi = 999;
    for (int i = 0; i < 90; i++)
      if (avgLightList[i] > maxLight) {
        maxLight = avgLightList[i];
        maxi = i;
      }
    int lightAngle = angleList[maxi];
    Serial.println(angleList[maxi]);
    char disChar[20];
    sprintf(disChar, "LA:%d,   ", lightAngle);
    OLED12864_ShowStr(0, 0, disChar);
    //判断距离，如果太小就停下
    myservo.write(MIDDLE_ANGLE);
    delay(600);
    float distance = GetDistance(); //调用测距函数
    static int err_sum = 0;
    if (distance < 20)
    {
      carMove(0, 0);
      while (1);
    }
    else if (abs(lightAngle) > 10)
    {
      int leftSpeed, rightSpeed;
      float P = 1.5, I = 1;
      int _speed = (int)lightAngle * P + (err_sum * I);
      err_sum += lightAngle;
      leftSpeed = -_speed;
      rightSpeed = _speed;
      carMove(leftSpeed, rightSpeed);


      sprintf(disChar, "SumErr:%d,   ", err_sum);
      OLED12864_ShowStr(0, 1, disChar);
      sprintf(disChar, "L:%3d,R:%3d   ", leftSpeed, rightSpeed);
      OLED12864_ShowStr(0, 2, disChar);

      delay(600);
      carMove(0, 0);
    }
    else
    {
      err_sum = 0;
      forwardScan();
      carMove(0, 0);
    }
  }

  void forwardScan()
  {
    char disChar[20];
    myservo.write(MIDDLE_ANGLE);
    for (int i = 0; i < 60; i++) {
      carMove(63, 60);
      float distance = GetDistance(); //用于存放距离的变量
      sprintf(disChar, "SR:%d   ", int(distance));
      OLED12864_ShowStr(0, 4, disChar);
      for (int j = 0; j < 50 && abs(distance - 1000) < 0.05; j++)
        distance = GetDistance();
      if (distance < 20)
        break;
      delay(20);
    }
  }
