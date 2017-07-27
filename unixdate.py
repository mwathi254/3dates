
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

startTime = datetime.date(input('Enter Year: '),input('Enter Month: '),input('Enter Day: '))
endTime = datetime.date(input('Enter Year: '),input('Enter Month: '),input('Enter Day: '))
d = datetime.datetime.now()
dEdit = d.replace(hour=0,minute=0,second=0,microsecond=0)
nowDate = time.mktime(dEdit.timetuple())
startDate = time.mktime(startTime.timetuple())
endDate = time.mktime(endTime.timetuple())            
print "Today's date in UNIX is: ",(nowDate)
print "First date in UNIX is: ",(startDate)
print "Last date in UNIX is: ",(endDate)
#eNd
