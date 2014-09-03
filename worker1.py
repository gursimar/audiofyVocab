#from dictionary.wordnix.Wordnix import wordnix
from ttsengine.GoogleTTS import GoogleTTS

filename = 'simar.mp3'
f = open(filename, 'w')
		
gtts = GoogleTTS()
data = gtts.convertAudioMP3('simar')
f.write (data)
f.close()
