import sys, re, urllib, array

def callAPI(func, zip):
	url = 'http://api.trulia.com/webservices.php?library=LocationInfo&function='+func+'&state='+zip+'&apikey=gysqg4zr2z65ycpzxzm47jam'
	ufile = urllib.urlopen(url)
	utext = ufile.read()
	print utext
	

def main():
	callAPI('getCitiesInState','CA')

if __name__ == '__main__':
	main()