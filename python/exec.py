import sys, re, urllib, array, MySQLdb
import lib
from elementtree.ElementTree import *

#use /usr/lib/python2.6/site-packages easy_install elementtree

def main():
	##works
	# x = lib.dbQuery()
	# x.execute("""create table r_listingStats (id int auto_increment not null, weekEndingDate varchar(16), type varchar(25), numberOfProperties varchar(25), medianListingPrice varchar(25), averageListingPrice varchar(25),  primary key (id)); """)
	# x.close_conn()
	# print x.result_data

	pop = {}
	pop["city"] = "cleveland"
	pop["state"] = "oh"
	pop["startDate"] = "2009-02-01"
	pop["endDate"] = "2009-02-12"
	pop["statType"] = "all"
	x = lib.APIcall()
	x.func = 'getCityStats'
	x.population = pop
	x.compose_request()
	x.make_apicall()
	x.parse_results()
	#print x.request_url
	#print x.response_data['listingStats']
	x.save_results()
	#print x.save_query
	# #x.execute("select param from xmlResponseTag where func = 'getCityStats' and header = 'listingStats';")
	# for a in x.response_data['listingStats']:
	# 	print a

if __name__ == '__main__':
	main()


# select distinct A.param, B.param 
# 		from xmlResponseTag as A
# 		left join xmlResponseTag as B 
# 			on A.tier <= B.tier and A.family = B.family and A.header = B.header and A.param <> B.param
# 		where A.func = 'getCityStats' and A.header = 'listingStats';