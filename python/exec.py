import sys, re, urllib, array, MySQLdb
import lib

def main():
	x = lib.dataPull()
	x.callAPI('getCitiesInState','CA')
	x.mysqlQuery('select * from funcTables;')

if __name__ == '__main__':
	main()