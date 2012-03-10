import sys, re, urllib, array, MySQLdb
import lib

def main():
	x = lib.dataPull()
	x.callAPI('getCitiesInState','CA')
	x.mysqlQuery("""insert into funcParam (func, param, param_class) values ('getZipCodeStats', 'endDate', 'date');""")

if __name__ == '__main__':
	main()