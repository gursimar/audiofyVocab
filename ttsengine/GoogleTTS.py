from TTSEngine import TTSEngine
import urllib2

class GoogleTTS(TTSEngine):
	def __init__(self):
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	def convertAudioMP3(self, sentence):
		response = self.opener.open('http://translate.google.com/translate_tts?tl=en&q=' + sentence)
		data = response.read()
		return data



if __name__ == "__main__":
	filename = 'simar.mp3'
	f = open(filename, 'w')
	
	gtts = GoogleTTS()
	data = gtts.convertAudioMP3('simar')
	f.write (data)
	f.close()