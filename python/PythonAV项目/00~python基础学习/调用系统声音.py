import pyttsx3 # 初始化引擎

engine = pyttsx3.init() # 将文本转换为语音
engine.say('欢迎使用pyttsx3库') # 运行引擎
engine.runAndWait()