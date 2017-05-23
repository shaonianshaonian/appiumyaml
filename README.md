## 简介
这是一个用Python语言基于Appium写的自动化测试框架，使用方法较为简单。测试人员可以不用懂代码，只需要编写如下文例子中的YAML格式文件即可按照自己的想法实现测试用例。各个模块之间相对独立，易于后续扩展其他功能。

##框架用法
#### 目录结构
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_tree.jpg)

Logic文件夹存放Python源文件。
Result文件夹存放执行用例后的测试报告及失败截图。
TestCase文件夹存放用户编写的实际用例。

#### 用户流程
用户可以遵循以下流程，快速上手执行用例：
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_liucheng.jpg)

#### 环境要求
Python3 + Appium1.4

#### 编写用例
1.通过YAML格式的文件编写用例，用例请放置于TestCase文件目录下。这里强调一下，为何使用YAML去描述用例，而不是用JSON或者XML，主要是因为YAML的表现形式更加直观，方便编写用例，并且易学易懂，几乎没有什么学习成本。相信看了下面的例子，大家的印象会更加深刻。
没错，这又是一个关于登录的小例子，它执行该流程：点击登录入口->输入账号及密码->确认登录->判断是否登录成功。

```yaml
-
 test_action: click
 test_control_type: xpath
 test_control_id: //android.widget.LinearLayout[@index='0']//android.widget.LinearLayout[@index='3']//android.widget.TextView[@index='1']
-
 test_action: click
 test_control_type: xpath
 test_control_id: //android.widget.LinearLayout[@index='0']//android.widget.RelativeLayout[@index='0']//android.widget.LinearLayout[@index='0']//android.widget.LinearLayout[@index='0']//android.widget.TextView[@index='0']
-
#输入用户名
 test_action: write
 test_control_type: xpath
 test_control_id: //android.widget.RelativeLayout[@index='0']//android.widget.RelativeLayout[@index='2']//android.widget.EditText[@index='0']
 test_value: account
-
#输入密码
 test_action: write
 test_control_type: xpath
 test_control_id: //android.widget.RelativeLayout[@index='0']//android.widget.RelativeLayout[@index='3']//android.widget.EditText[@index='0']
 test_value: password
-
#点击登录按钮
 test_action: click
 test_control_type: xpath
 test_control_id: //android.widget.RelativeLayout[@index='0']//android.widget.RelativeLayout[@index='4']//android.widget.Button[@index='0']
-
#判断结果
 test_action: assert
 test_assert_type: control
 test_control_type: xpath
 test_control_id: //android.widget.LinearLayout[@index='0']//android.widget.RelativeLayout[@index='0']//android.widget.ImageView[@index='0']
```

2.看了上面的例子是不是有点蒙圈？别怕，下面的表格将详细地告诉你每一个动作的具体含义及它的用法。
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_excel.jpg)


#### 执行用例
打开cmd，进入Runner.py所在文件目录，使用`python Runner.py`执行即可，执行完的结果会打印至屏幕，当然以这种方式查看结果并非理想，后面会介绍以html的方式查看结果。
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_runner.png)
#### 结果展示
以html网页的形式展示结果，提升了结果的可读性。该结果中包含了被执行的测试用例条数、执行所花费的时间、执行结果以及失败原因。执行完成后，大家可以在Result文件目录中找到该html文件，并且还能在此目录下找到执行用例失败后的屏幕截图。
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_result.png)
## 实现原理
下图是该框架的在设计时的层次结构，通过对其分析，可以概括出框架的具体实现原理。
![](https://github.com/Gavin-Niubility/MyImage/raw/master/appium4_cengci.png)

用户层：该层是用户可操作的部分，即YAML格式的用例与Runner.py文件。用户编写符合规则的用例后，通过执行Runner.py脚本即可运行用例并生成html格式（网页版）的测试报告及失败截图。
执行层：该层起着组织及执行测试用例的作用，可读取上层的YAML格式用例，调用翻译层将YAML格式用例变成机器可懂的单元测试代码，可在用例开始/结束执行时，添加除用例以外的其他操作。
翻译层：该层顾名思义，提供了翻译上层用例的方法。这些方法能够读取指定文件夹下所有YAML格式的文件，并按文件生成对应的case，判断这些case的key值，去选择调用驱动层的具体方法。
驱动层：该层对Appium常用的操作进行了封装，也增加了一些自定义的常用操作。通过调用Appium提供的接口达到UI自动化的目的。

# Appiumpython
