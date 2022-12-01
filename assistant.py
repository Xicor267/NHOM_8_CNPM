import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic :
		robot_ear.adjust_for_ambient_noise(mic)	
		print("Robot : I'm listening")
		audio = robot_ear.listen(mic)
	print("Robot : ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("Me : " + you)

	if you == "":
		robot_brain = "I can't hear you, try again !!!"
	elif "hello" in you:
		robot_brain = "Hello Xicor !!! How are you today man ?"
	elif "fine" in you:
		robot_brain = "Haha ok ok"	
	elif "today" in you:
		today = date.today();
		robot_brain = today.strftime("%B %d, %Y and it's very cold !!!")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S sceonds")
	elif "infected" in you:
		robot_brain = "Yes, you have FO =((("
	elif "president" in you:
		robot_brain = "Pham Minh Chinh"
	elif "bye" in you:
		robot_brain = "Bye bye see you again, Xicor !!!"
		print("Robot : " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else: 
		robot_brain = "Ok i'm fine thank you !!!"

	print("Robot : " + robot_brain)
	voices = robot_mouth.getProperty('voices')
	# [0]: male/ [1]: female
	robot_mouth.setProperty('voice', voices[1].id)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()