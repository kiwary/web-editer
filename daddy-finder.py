#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def DaddyFinder():
	ak = open("List.txt","r");
	link = raw_input("Mode: http \nใส่ URL ที่ต้องการค้นหา \n(ตัวอย่างเช่น : mict.go.th หรือ www.mict.go.th ): ")
	print "\nกําลังดําเนินการ.................\nURL ที่สามารถเป็นไปได้ : \n"
	while True:
		sub_link = ak.readline()
		status = sub_link
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:			
			print "พ่ออยู่ที่นี่ --> ",req_link

def Credit():
	Space(5); print "                   _         _   _            _           "
	Space(5); print " __ _ _ _  __ _ __| |_  __ _| |_| |_  __ _ __| |_____ _ _ "
	Space(5); print "/ _` | ' \/ _` / _| ' \/ _` | / / ' \/ _` / _| / / -_) '_|"
	Space(5); print "\__,_|_||_\__,_\__|_||_\__,_|_\_\_||_\__,_\__|_\_\___|_|  "
	Space(1); print ""
	Space(10); print "#####################################"
	Space(10); print "#   <        Daddy-Finder       >   #"
	Space(10); print "#  This Script specific to ThaiWeb  #"
	Space(10); print "#             Edit by AK            #"
	Space(10); print "#         anachakhacker.com         #"
	Space(10); print "#####################################"


Credit()
DaddyFinder()
