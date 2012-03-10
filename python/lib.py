import sys, re, urllib, array, MySQLdb

class dataPull():

	def __init__(self):
		print 'heya'

	def mysqlQuery(self,query):
		conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "root", db = "test_realestate")
		cursor = conn.cursor()
		request = cursor.execute(query)
		for r in range(request):
			print cursor.fetchone()

		cursor.close()


	def callAPI(self,func, zip):
		url = 'http://api.trulia.com/webservices.php?library=LocationInfo&function='+func+'&state='+zip+'&apikey=gysqg4zr2z65ycpzxzm47jam'
		ufile = urllib.urlopen(url)
		utext = ufile.read()
		self.sqlFields(utext)
		##print utext

	##temporary	--> Find all API fields returned
	def sqlFields(self,utext):
		fields = []
		tuples = re.findall(r'<([\w\d\+\.\s/-]+)>([\w\d\+\.\s/-]+)</([\w\d\+\.\s/-]+)>',utext)
		for tuple in tuples:
			if not (tuple[0] in fields):
				fields.append(tuple[0])
				#print tuple[0]

class dbQuery:
	input_param = []
	target_data = []
	population = {}
	result_data = {}
	
	def  __init__(self):
		print 'yoyoyoyo'		