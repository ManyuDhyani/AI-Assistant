import sys
import speech_recognition as sr

def voice_typing():
	#r = sr.Recognizer()
	#with sr.Microphone() as source:
	print("Please tell File name:")
		#audio = r.listen(source)
		#Filename = r.recognize_google(audio)
	Filename = input()
	print(Filename)
	print("Please start your message....")
	while 1:
		try:
			"""
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.listen(source)
				text = r.recognize_google(audio)
			"""
			f = open("/Users/pankajdhyani/Desktop/"+Filename+".txt","a")
			while 1:
				text = input()
				if text == "close message":
					break
				f.write(text)
			#f = open("/Users/pankajdhyani/Desktop/"+Filename+".txt","a")
			#f.write(text)
			f.close()
		except:
			print("Didn't get you..")
		else:
			f = open("/Users/pankajdhyani/Desktop/"+Filename+".txt","r")
			print(f.read())
			return 
			
