import time,os
import pyautogui as pag
import json

#x, y = pag.position()
#获取鼠标的坐标
import json
 
#保存json文件
def save_json(save_path,data):
    assert save_path.split('.')[-1] == 'json'
    with open(save_path,'w') as file:
        json.dump(data,file)

#"screensize": 屏幕分辨率【x,y】
#"nextpos": '下一个'按钮的坐标【x,y】
#"input_icon": 左下角'立即录音'按钮的坐标【x,y】
#"input_icon": 单词下方英式发言右边的小喇叭的坐标【x,y】


# 获取屏幕的尺寸
screenWidth, screenHeight = pag.size()
print(f'屏幕尺寸为：{screenWidth}*{screenHeight}')

print('现在全屏打开西柚的‘朗读练习’作业,完成如下配置')

#获取下一个按钮位置
input('现在,右下角将会出现“下一个按钮”,将鼠标放置此按钮上,按下回车键确认位置')
nextx, nexty = pag.position()
print(f'好,‘下一个按钮’的位置是({nextx},{nexty})')

#获取录音按钮位置
input('现在,将鼠标移动至在左下角橙色“立即录音”按钮上,按下回车键确认位置')
inx, iny = pag.position()
print(f'好,‘录音按钮’的位置是({inx},{iny})')

#获取单词下方英式发音右边的小喇叭位置
input('现在,将鼠标移动至单词下方英式发音右边的小喇叭按钮上,按下回车键确认位置')
exax, exay = pag.position()
print(f'好,‘演示按钮’的位置是({exax},{exay})')

print('坐标录入完毕，正在处理中')

config = {
  "screensize": [screenWidth,screenHeight],
  "nextpos": [nextx,nexty],
  "input_icon": [inx,iny],
  "example_icon": [exax,exay]
}

save_json('config.json',config)

print(config)
input('你的配置文件已保存！现在你可以启动‘朗读练习’程序了')