import sys, re, urllib, array, MySQLdb
import lib

def main():
	# x = lib.dataPull()
	# x.callAPI('getCitiesInState','CA')
	# x.mysqlQuery("""insert into funcParam (func, param, param_class) values ('getZipCodeStats', 'endDate', 'date');""")

	##works
	# x = lib.dbQuery()
	# x.execute("select * from funcParam;")
	# x.close_conn()
	# print x.result_data[0][0]

	pop = {}
	pop["city"] = "cleveland"
	pop["state"] = "oh"
	x = lib.APIcall()
	x.compose_request('getCityStats',pop)
	
if __name__ == '__main__':
	main()