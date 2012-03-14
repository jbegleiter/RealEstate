import sys, re, urllib, array, MySQLdb
import lib

def main():
	# x = lib.dataPull()
	# x.callAPI('getCitiesInState','CA')
	# x.mysqlQuery("""insert into funcParam (func, param, param_class) values ('getZipCodeStats', 'endDate', 'date');""")

	x = lib.dbQuery()
	x.execute("select * from funcParam;")
	x.close_conn()

if __name__ == '__main__':
	main()