from gtts import gTTS as ts
"""
文本转化为声音
"""

# ts.GOOGLE_TTS_URL = 'https://translate.google.cn/translate_tts'
# ts.GOOGLE_TTS_HEADERS = {
#     'Referer': 'http://translate.google.cn/',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# }

txt2speech = ts(text="Hello Python", lang="en")
txt2speech.save("data/text.mp3")

with open("data/poetry.txt") as f:
    audio = ts(text=f.read(), lang="zh-cn")
    audio.save("poety.mp3")
