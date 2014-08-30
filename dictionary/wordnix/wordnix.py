from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '960542d38a1d63153361539342c38085a378dcecf6fc3578f'
client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)
example = wordApi.getTopExample('irony')
print example.text
definitions = wordApi.getDefinitions('irony')
for i,v in enumerate(definitions):
	print i,v.text


