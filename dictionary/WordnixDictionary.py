from Dictionary import Dictionary
from wordnik import *

class WordnixDictionary(Dictionary):
	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = '960542d38a1d63153361539342c38085a378dcecf6fc3578f'

	def __init__(self):
		client = swagger.ApiClient(self.apiKey, self.apiUrl)
		self.wordApi = WordApi.WordApi(client)

	def getExample(self, word):
		exam = self.wordApi.getTopExample(word)
		return exam
		
	def getDefinitions(self, word):
		definitions = self.wordApi.getDefinitions(word)
		return definitions

if __name__ == "__main__":
	wndict = WordnixDictionary()
	word = 'apathy'
	
	example = wndict.getExample(word)
	print example.text
	
	definitions = wndict.getDefinitions(word)
	for i,v in enumerate(definitions):
		print i,v.text

