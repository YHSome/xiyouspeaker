** 此文章同步保存在以下网站 ** 
[森的神秘空间](https://yhsome.github.io/2023/08/23/xiyouspeaker)
[github](https://github.com/YHSome/xiyouspeaker/)

# 功能简介
该脚本可以帮助你完成 [西柚英语](https://student.xiyouyingyu.com) 中烦人的单词朗读。
# 使用方法
<video src="example.mp4" position= "absolute" width="100%" height="100%" controls="controls"></video>

## 第一步，安装python以及相应库
你需要安装的python库有
```
sounddevice
soundfile
pyautogui
```
## 第二步，完成相应设置
### 设置默认录制设备（十分重要！）
**使用前请将系统默认录制设备改成“立体声混音”，否则无法录音**
### 打开 ``` ./config.json ``` ，填写相应配置。
以下是配置文件的相关释义
**提示：**你可以使用 ``` ./显示鼠标坐标.py ``` 快速定位光标所处的像素的坐标
>"screensize": 屏幕分辨率【x,y】

>"nextpos": '下一个'按钮的坐标【x,y】

>"input_icon": 左下角'立即录音'按钮的坐标【x,y】

>"input_icon": 单词下方英式发言右边的小喇叭的坐标【x,y】

这个是这个是1600x900分辨率下，谷歌浏览器（左）半屏打开向右拉到底的设置示例
```
{
  "screensize": [1600,900],
  "nextpos": [1025,820],
  "input_icon": [340,800],
  "example_icon": [333,250]
}
```

## 第三步，启动程序
你可以用cmd运行，也可以用vscode等ide运行文件
```cmd
$ python 朗读练习v1.0.py
```

# 未来的展望
目前只做了几个功能，会考虑以后更多功能的开发