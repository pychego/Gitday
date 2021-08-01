//循迹传感器获取函数定义(这样定义可以使代码简洁)
#define TL2 GetL2()
#define TL1 GetL1()
#define TR1 GetR1()
#define TR2 GetR2()

int flag = 0;
void setup() {
  // put your setup code here, to run once:
  carInit();//电机初始化
  trackSensorInit();//循迹传感器初始化
  printfInit(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (1)
  {
    track();
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
      while(1);
    }
  
}
