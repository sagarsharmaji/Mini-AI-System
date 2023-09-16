# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3
import ctrl
import sys
import datetime
from datetime import date

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

# Loop infinitely for user to
# speak
def Play():
	SpeakText("Hi!Sagar!How can I help You?")
	while(1):
		
		# Exception handling to handle
		# exceptions at the runtime
		try:
			
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level
				r.adjust_for_ambient_noise(source2, duration=0.2)
				
				#listens for the user's input
				audio2 = r.listen(source2)
				
				# Using google to recognize audio
				MyText = r.recognize_google(audio2)
				MyText = MyText.lower()

				print("Did you say "+MyText)
				#SpeakText(MyText)

				if "hi" in MyText:
					SpeakText("hi how are you")
				elif "play" in MyText:
					SpeakText("Playing your Recording....")
					from playsound import playsound 
					playsound('rec.wav')
				elif "volume" in MyText:
					SpeakText("Get Ready to Control Volume using Gesture")
					ctrl.Ctrl()
				elif "weather" in MyText:
					import weather
					weather.get_current_weather()
				elif "date" in MyText:
					today = date.today()
					t = datetime.datetime.now()
					SpeakText("The Current Date is")
					SpeakText(today)
					SpeakText("And Current Time is")
					SpeakText(t.hour)
					SpeakText(t.minute)
				elif "close gui" in MyText:
					SpeakText("Thank You Sagar Have a Great Day Ahead..Closing GUI..")
					sys.exit()
				else:
					SpeakText("Kindly Comeup again.")

		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			
		except sr.UnknownValueError:
			print("unknown error occured")