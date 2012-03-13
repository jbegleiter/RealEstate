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
				print tuple[0]

class dbQuery:
	input_param = []
	target_data = []
	population = {}
	result_data = {}
	cursor = '' ##might have to update this
	
	def  __init__(self):
		print 'yoyoyoyo'

	def init_conn(self):
		conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "root", db = "test_realestate")
		cursor = conn.cursor()
		return cursor

	def close_conn(self,cursor):
		cursor.close

	def execute(self,cursor,query):
		request = cursor.execute(query)
		if (range(request) > 0):
			for r in range(request):
				print cursor.fetchone() ##have this added to a dictionary
		else:
			return false


class APIcall:
	func = ''
	apikey = 'gysqg4zr2z65ycpzxzm47jam' ##Make this a db table (eventually)
	root = 'http://api.trulia.com/webservices.php?library='
	request_url = ''

	def __init__(self):
		print 'ahoy'

	#def compose_request(self,func,population):
		##lookup structure of request in db
		#returns url

	#def make_apicall(self,url):
		#returns utext

	#def parse_results(self,utext,func):
		##lookup result fields in db
		## insert into dictionary with field names as lookup key
		## parse structure hardcoded for now, variables returned from db (above)
		#returns result_data

	#def save_results(self,result_data,func):
		##look up appropriate sql table to save from a sql table
		##Make sql call to insert into table
		#return true/false/error message

	#def display_results(self,results, func):
		##this can be used if I'm not sure if I'm sure if the data should be saved
		#print results

class pullData:
	request_input = {}
	vehicle = ''
	request_param = {}

	def __init__(self):
		print 'matey'

	#def retrieve_data(self,specs):
		##determine whether info exists in tables, if not make the necessary api call
		##can use APIcall.displayresults if first want to check quality
		##have to make db table here?
		#call APIcall or pullData.dbpull

	#def db_pull(self, specs)
		#execute dbQuery(specs)

