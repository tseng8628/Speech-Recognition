import speech_recognition as sr
import os
import string
from textblob import TextBlob
from gtts import gTTS


fromLanguage = "zh-TW"
toLanguage = "en"

r = sr.Recognizer()
# 去除雜音
r.energy_threshold = 4000

#從麥克風聽
with sr.Microphone() as source:
	print ("按下 Ctrl-C 可停止程式")
	try:
		while True:
			print("請唸出想翻譯的 句子或單詞")
			audio = r.listen(source)
			sttTXT_org = r.recognize_google(audio,language=fromLanguage)
			print ("Google Speech Recognition thinks you said : " + sttTXT_org)

			sttTXT_tblob = TextBlob(sttTXT_org)

			blobTranslated = sttTXT_tblob.translate(to=toLanguage)
			print("翻譯結果-->  " + str(blobTranslated))

			tts = gTTS(str(blobTranslated) + ". ", lang=toLanguage)
			tts.save("tts.mp3")
			os.system("omxplayer -p -o local tts.mp3")


	except KeyboardInterrupt:
		print('關閉程式')
