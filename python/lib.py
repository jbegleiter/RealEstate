import sys, re, urllib, array, MySQLdb, html5lib
from elementtree.ElementTree import ElementTree, fromstring

class dbQuery:
	input_param = []
	target_data = []
	population = {}
	result_data = []
	cursor = '' ##might have to update this
	
	def  __init__(self):
		self.init_conn()

	def init_conn(self):
		conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "root", db = "test_realestate")
		self.cursor = conn.cursor()

	def close_conn(self):
		self.cursor.close

	def execute(self,query):
		request = self.cursor.execute(query)
		if (range(request) > 0):
			for r in range(request):
				self.result_data.append(self.cursor.fetchone())
		else:
			return false
	
	def clear(self):
		self.result_data = []


class APIcall:
	func = ''
	apikey = 'gysqg4zr2z65ycpzxzm47jam' ##Make this a db table (eventually)
	root = 'http://api.trulia.com/webservices.php?library='
	request_url = ''
	population = {}
	ma_ufile = ''
	response_tags = []
	response_data = {}
	res_dat = []

	def __init__(self):
		print 'ahoy'

	def compose_request(self):
		##For all fields in funcParam, pull relevant field from population{}
		#print "{0} ...\n {1}!".format("hey", "there")
		#returns url

		if (re.search("Stats",self.func)):
			self.request_url = self.root + "TruliaStats&function="+self.func
		else:
			self.request_url = self.root + "LocationInfo&function="+self.func
		
		cr_db = dbQuery()
		cr_db.execute("select param, param_class from funcParam where func = '"+self.func+"';")

		for r in cr_db.result_data:
			cr_param = r[0]; cr_param_class = r[1]
			if (self.population[cr_param]): #create a function (pop_validate) that checks for correct formatting of inputs
				self.request_url += "&" + cr_param +"="+ self.population[cr_param]
			else: break

		self.request_url += "&apikey="+self.apikey
		cr_db.close_conn()
			 

	#def pop_validate(self):
		##validate each input -->this.population, used in compose_request
		##create db table for input formats
		#returns true/false

	def make_apicall(self):
		##composes raw data file to be parsed
		self.ma_ufile = urllib.urlopen(self.request_url)
		self.utext = self.ma_ufile.read()
		

	def parse_results(self):
		##lookup result fields in db
		## insert into dictionary with field names as lookup key
		## parse structure hardcoded for now, variables returned from db (above)
		#returns result_data

		##get response heading tags --> can make this db call in future
		if (re.search("Stats",self.func)):
			self.response_headers = ['trafficStats','listingStats']
		else:
			##update this!
			print 'np'

		treetop = fromstring(self.utext)
		for header in self.response_headers:
			tree = treetop.findall('.//'+header)
			self.res_dat = []
			self.traverse(tree)
			self.response_data[header] = self.res_dat
			

	def traverse(self,tree):
		t_d={}
		for target in tree:
			if (type(target.text) is str and len(target.text) > 0):
				t_d[target.tag] = target.text
			else:
				self.traverse(target)
		if (len(t_d) > 0):
			self.res_dat.append(t_d)
	

	def save_results(self):
		##look up appropriate sql table to save from a sql table
		##Make sql call to insert into table
		#return true/false/error message
		sr_m = dbQuery();
		sr_m.clear()
		for header in self.response_headers:
			sr_b = "select distinct param from xmlResponseTag where func = '"+self.func+"' and header = '"+header+"';"
			sr_m.execute(sr_b)
			sr_xmlParam = sr_m.result_data
			sr_m.clear()
			#print self.response_data[header][0]['date']
			sr_tableString = 'insert into r_'+header+' ('## insert into res_ 
			
			for sr_xParam in sr_xmlParam:
				#print sr_xParam
				sr_tableString =sr_tableString + str(sr_xParam[0])+', '
			sr_tableString = sr_tableString[:-2]+ ') values '
			print sr_tableString
			#print self.response_data[header]
			for sr_byte in self.response_data[header]:
				print sr_byte
				for sr_xParam2 in sr_xmlParam:
					print sr_xParam2[0]##week ending date is a higher tier. add tier and family to xmlResponseTag
					#have to apply lower tiers (higher priority) to higher tiers in the same family


			# print 'stop'
			# for sr_val in self.response_data[header]:
			# 	print sr_val
			# 	sr_str1 = '( '
			# 	for sr_xParam2 in sr_xmlParam:
			# 		print sr_val[sr_xParam2[0]]
			# 		#sr_str1 += str(sr_val[sr_xParam2[0]])+', '
			# 	#print sr_str1

			# print sr_tableString
			# print self.response_data[header]
			##compose mysql query --> dbtable (header, weekEndingDate, type/key numberOfProperties, medianListingPrice, averageListingPrice)
			
		sr_m.close_conn()


	#def display_results(self,results, func):
		##this can be used if I'm not sure if I'm sure if the data should be saved
		#print results@

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

