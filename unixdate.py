#!/usr/bin/env python
"""
Simple Solution to Convert Dates to Unix
Dates in Yr,Mt,Dt format
3 Dates Converted
Today's Date
Your Start Date
Your End Date

@kelvin mwathi 2017
"""


import time
import datetime

class UnixDate(object):
    def __init__(self):
        self.nowDate = time.mktime(todayTime.timetuple())
        self.startDate = time.mktime(startTime.timetuple())
        self.endDate = time.mktime(endTime.timetuple())
        
    def dateToday():
        d = datetime.datetime.now()
        dEdit = d.replace(hour=0,minute=0,second=0,microsecond=0)
       # print "unix of todays date is: ",(self.nowDate)
    def otherDays():
        startTime = datetime.date(input('Enter Year: '),input('Enter Month: '),input('Enter Day: '))
        endTime = datetime.date(input('Enter Year: '),input('Enter Month: '),input('Enter Day: '))

       # print "unix of first date is: ",(self.startDate)
       # print "unix of last date is: ",(self.endDate)
    def allDates(self):
        print "unix of todays date is: "
        return self.nowDate
        print "unix of first date is: "
        return self.startDate
        print "unix of last date is: "
        return self.endDate
   #break


