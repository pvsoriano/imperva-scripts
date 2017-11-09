#!/usr/bin/python

# Modified script from Violent Python
# that tests a user agent response.

import mechanize
def UserAgent(url, userAgent):
	browser = mechanize.Browser()
	browser.addheaders = userAgent
	webpage = browser.open(url)
	source_code = webpage.read()
	print source_code

url = 'http://www.useragentstring.com'
userAgent = [('User-agent','Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6')]
UserAgent(url, userAgent)
