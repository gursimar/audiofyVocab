class TTSEngine(object):
	def __init__(self):
		print 'Constructing object'

	def _convertWord(self, word):
		wordmod = word.replace(" ","+")
		return wordmod


if __name__ == "__main__":
	word1 =  'In tts engine'
	print word1
	engine1 = TTSEngine()
	print engine1._convertWord(word1) 
	


