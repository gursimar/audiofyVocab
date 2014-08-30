import urllib2
response = urllib2.urlopen('http://translate.google.com/translate_tts?tl=en&q=Hello')
response.addheaders = [('User-agent', '')]
html = response.read()


