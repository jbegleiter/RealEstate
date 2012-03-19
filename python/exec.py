import sys, re, urllib, array, MySQLdb
import lib
from elementtree.ElementTree import *

#use /usr/lib/python2.6/site-packages easy_install elementtree

def main():
	# x = lib.dataPull()
	# x.callAPI('getCitiesInState','CA')
	# x.mysqlQuery("""insert into funcParam (func, param, param_class) values ('getZipCodeStats', 'endDate', 'date');""")

	##works
	# x = lib.dbQuery()
	# #x.execute("create table xmlResponseTag (id int not null auto_increment, );")
	# x.close_conn()
	# print x.result_data[0][0]

	pop = {}
	pop["city"] = "cleveland"
	pop["state"] = "oh"
	pop["startDate"] = "2009-02-06"
	pop["endDate"] = "2009-02-07"
	pop["statType"] = "all"
	x = lib.APIcall()
	x.func = 'getCityStats'
	x.population = pop
	x.compose_request()
	x.make_apicall()
	x.parse_results()
	print x.response_data
	#print x.res_dat


if __name__ == '__main__':
	main()