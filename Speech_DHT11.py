import speech_recognition as sr
import os
from gtts import gTTS
import time
import Adafruit_DHT

# initial speech recognition
r = sr.Recognizer()
r.energy_threshold = 4000


# initial GPIO (DHT11
GPIO_PIN = 4


# listen from microphone
with sr.Microphone() as source:
	print("按下 Ctrl-C 可停止程式")
	try:
		while True:
			print("對麥克風說一些話～")
			audio = r.listen(source)
			stt = r.recognize_google(audio, language='zh-TW')
			print("Google覺得你說的話是: " + stt)


			if "溫度" in r.recognize_google(audio, language='zh-TW'):
 
				h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
				#print('溫度={0:0.1f}度C 濕度={1:0.1f}%'.format(t, h))
				t1 = str(int(t))
			
				ch_t = ""
				dic = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
				for c in t1:
					ch_t += str(dic[c])
					ch_t += ' '
				#print(ch_t)
											
				tts = gTTS('溫度' + ch_t + '度')
				tts.save('tem1.mp3')
				print('溫度' + t1 + '度')
				os.system('omxplayer -p -o local tem1.mp3')
	except KeyboardInterrupt:
		print("關閉程式")




