from TTSEngine import TTSEngine
import pyttsx

# To fix saving the file to disk seek
# https://github.com/humbled/pyttsx/commit/ab65d84e21c570c7c645a047fbf62c40adc4441a
# http://stackoverflow.com/questions/15516572/how-can-i-convert-text-to-speech-mp3-file-in-python

class pyttsxTTS(object TTSEngine):
	def __init__(self):
		self.engine = pyttsx.init()
	
	def setRate(self, rate):
		self.engine.setProperty('rate', rate)
	
	def setVolume(self, vol):
		self.engine.setProperty('volume', vol)
	
	def setVoice(self, voice):
		engine.setProperty('voice', voice.id)
		
	def convertAudioMP3(self, sentence):
		self.engine.say(sentence)
		self.engine.runAndWait()
	
	def getVoices():
		voices = self.engine.getProperty('voices')
		return voices

		

if __name__ == "__main__":
	#filename = 'simar.mp3'
	#f = open(filename, 'w')

	ptts = pyttsxTTS()
	voices = ptts.getVoices()
	for voice in voices:
		print "Using voice:", repr(voice)
		engine.setProperty('voice', voice.id)
		engine.say("Hi there, how's you ?")
		engine.runAndWait()
		
	pytts = pyttsxTTS()
	data = pytts.convertAudioMP3('simar')
	#f.write (data)
	#f.close()

