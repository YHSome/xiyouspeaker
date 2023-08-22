print('引入资源中...')
import sounddevice as sd
import soundfile as sf
import json
import pyautogui
import time
import os

def clear_terminal():
    # 判断操作系统类型
    if os.name == 'nt':  # Windows系统
        os.system('cls')
    else:  # Linux、macOS等系统
        os.system('clear')
    # 清空终端
    #clear_terminal()

duration = 2  # 录制时长（秒）
filename = "./saved/output.wav"  # 保存的文件名
samplerate = 44100  # 采样率（可以根据需要进行调整）


# 读取JSON文件
filename = "config.json"  # JSON文件名
with open(filename, "r") as file:
    data = json.load(file)
# 读取JSON中的数据
screensize = data["screensize"]
nextpos = data["nextpos"]
input_icon = data["input_icon"]
example_icon = data["example_icon"]
# 打印读取的数据
print("屏幕分辨率:", screensize)
print("下一个按钮的位置:", nextpos)
print("录音按钮位置:", input_icon)
print("系统发发音按钮位置:", example_icon)
print('提示：执行过程中不要移动鼠标！')
print('将系统音量调至60%以保证最佳录音效果')

while True:
    input('按回车开始,按ctrl+c结束程序运行')
    for _ in range(5):
        print('使用前请将系统默认录制设备改成“立体声混音”，否则无法录音')
    t = int(input('请输入你还有多少个单词未完成'))
    print('两秒后开始')
    for i in range(1,t+1,1):
        time.sleep(2)
        clear_terminal()
        print(f'正在执行第{i}个')
        # 设置录音参数
        duration = 2  # 录制时长（秒）
        filename = "./saved/output.wav"  # 保存的文件名
        samplerate = 44100  # 采样率（可以根据需要进行调整）
        # 录制电脑发出的声音
        print("开始录音...")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
        time.sleep(0.1)
        pyautogui.click(example_icon)
        sd.wait()
        print("录音完成.")
        # 保存录音文件
        sf.write(filename, recording, samplerate)
        
        # 读取录音文件
        filename = "./saved/output.wav"  # 录音文件名
        data, samplerate = sf.read(filename)
        # 增加音量（乘以增益因子）
        gain = 1  # 增益因子，可以根据需要进行调整
        data *= gain# 保存增益后的录音文件
        output_filename = "./saved/output.wav"  # 保存的文件名
        sf.write(output_filename, data, samplerate)


        # 读取录音文件
        filename = "./saved/output.wav"  # 录音文件名
        data, samplerate = sf.read(filename)
        #这里点击启动录音按钮
        pyautogui.click(input_icon)
        time.sleep(0.1)
        # 播放录音文件
        print("开始播放录音...")
        sd.play(data, samplerate)
        sd.wait()
        print("播放完成.")
        #再次点击启动录音按钮，停止录音
        pyautogui.click(input_icon)
        time.sleep(2)
        print('点击下一个按钮')
        pyautogui.click(nextpos)