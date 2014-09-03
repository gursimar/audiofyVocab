from dictionary.WordnixDictionary import WordnixDictionary
from ttsengine.GoogleTTS import GoogleTTS

word = 'dejected'


filename = 'output/' + word + '.mp3'
f = open(filename, 'w')
		
gtts = GoogleTTS()
wndic = WordnixDictionary()

sentence = ''
sentence = sentence + word + '.'

definitions = wndic.getDefinitions(word)
for i,v in enumerate(definitions):
	sentence = sentence + v.text

print word + ' ' + sentence + '\n'
data = gtts.convertAudioMP3(sentence)
f.write (data)
f.close()
