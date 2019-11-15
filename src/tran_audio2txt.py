import speech_recognition as sr
"""
声音转化为文本

常用Python语音识别依赖库
Python的依赖库中有一些现成的语音识别软件包。其中包括：

apiai
google-cloud-speech
pocketsphinx
SpeechRcognition
watson-developer-cloud
wit
其中SpeechRecognition，是google出的，专注于语音向文本的转换。

wit 和 apiai 提供了一些超出基本语音识别的内置功能，如识别讲话者意图的自然语言处理功能。

*** 
地址来源: <https://blog.csdn.net/alice_tl/article/details/89684369>
"""
r = sr.Recognizer()
wirh sr.AudioFile('data/test1.wav') as source:
    audio = r.record(source)
    print(type (audio))

try:
    result = r.recognize_google(audio, language='zh-CN', show_all= True)
    print(result)
except sr.Unknow as e:
    print("Google 语音识别未能理解音频内容")
except sr.ResuqestError as e:
    print("未能从 Google 语音识别服务器请求到结果", e)
