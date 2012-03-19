import sys, re, urllib, array, MySQLdb
import lib
from elementtree.ElementTree import *

#use /usr/lib/python2.6/site-packages easy_install elementtree

def main():
	# x = lib.dataPull()
	# x.callAPI('getCitiesInState','CA')
	 #x.mysqlQuery("""""")

	##works
	# x = lib.dbQuery()
	# x.execute("insert into xmlResponseTag (func, header, param) values ('getCityStats', 'listingStats','type');")
	# x.execute("insert into xmlResponseTag (func, header, param) values ('getCityStats', 'listingStats','numberOfProperties');")
	# x.execute("insert into xmlResponseTag (func, header, param) values ('getCityStats', 'listingStats','medianListingPrice');")
	# x.execute("insert into xmlResponseTag (func, header, param) values ('getCityStats', 'listingStats','averageListingPrice');")
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
	# print x.response_data['trafficStats']
	x.save_results()
	#x.execute("select param from xmlResponseTag where func = 'getCityStats' and header = 'listingStats';")


if __name__ == '__main__':
	main()