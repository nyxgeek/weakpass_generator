#!/usr/bin/env python3
# 2020.02.18 - @nyxgeek - TrustedSec

# generate weak passwords based on current date

import datetime
from datetime import datetime, timedelta

#Define our Months and Keywords for Prefixes
monthDictionary = {}
monthDictionary["January"] = ["January", "Winter"]
monthDictionary["February"] = ["February", "Winter"]
monthDictionary["March"] = ["March", "Winter", "Spring"]
monthDictionary["April"] = ["April", "Spring"]
monthDictionary["May"] = ["May", "Spring", "Summer"]
monthDictionary["June"] = ["June", "Spring","Summer"]
monthDictionary["July"] = ["July", "Summer"]
monthDictionary["August"] = ["August", "Summer", "Fall", "Autumn"]
monthDictionary["September"] = ["September", "Fall", "Autumn"]
monthDictionary["October"] = ["October", "Fall", "Autumn", "Winter"]
monthDictionary["November"] = ["November", "Fall", "Autumn", "Winter", "Thanksgiving"]
monthDictionary["December"] = ["December", "Winter", "Christmas"]

OUTPUT_LIST = []


def create_passwords(tempdate):
    year_short=tempdate.strftime("%y")
    year_long=tempdate.strftime("%Y")
    current_month=tempdate.strftime("%B")

    SUFFIX_ARRAY = [ year_short ,  year_long, "@"+year_short, "@"+year_long, year_short+"!", year_long+"!", "1", "123"]

    for month_prefix in monthDictionary[current_month]:
        for password_suffix in SUFFIX_ARRAY:
            #print("%s%s" % (month_prefix, password_suffix) )
            global OUTPUT_LIST
            OUTPUT_LIST.append("%s%s" % (month_prefix, password_suffix))


for numberofdays in range(1,90):
    tempdate = datetime.now() - timedelta(days=numberofdays)
    create_passwords(tempdate)


#print the unique ones
print("Here are the results:")

OUTPUT_LIST.sort()
output_set = sorted(set(OUTPUT_LIST))

#open file to write to
outfile = open("latest_passwords.txt", "w")


#iterate through our sorted and uniqued list
for candidate_password in output_set:
    print(candidate_password)
    outfile.write(candidate_password+"\n")


#close our file now
outfile.close()
