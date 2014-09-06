from dictionary.WordnixDictionary import WordnixDictionary
from ttsengine.GoogleTTS import GoogleTTS
output_dir = 'output/'
input_file = 'words.txt'

f = open(output_dir + input_file, 'r')
wordstext = f.read()
f.close
#print wordstext
words = wordstext.split('\r\n')
#print words
for word in words:
	#print word
	#word = 'dejected'

	filename = output_dir + word + '.mp3'
	f = open(filename, 'w')
			
	gtts = GoogleTTS()
	wndic = WordnixDictionary()

	sentence = ''
	sentence = sentence + word + '.'

	definitions = wndic.getDefinitions(word)
	for i,v in enumerate(definitions):
		sentence = sentence + v.text
		break

	print sentence + '\n'
	data = gtts.convertAudioMP3(sentence)
	f.write (data)
	f.close()
