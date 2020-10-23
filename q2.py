def Month(m):
    months = [['January','February','March','April','May','June','July','August','September','October','November','December'],['Jan','Feb','Apr','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]
    if len(m) == 4:
        return (months[1].index(m) + 1)
    else:
        return (months[0].index(m) + 1)

def DateFormat(date1):
    year = 0
    month = 0
    date = 0
    if date1.find("/") == -1:
        if date1.find("-") == -1:
            if date1.find(".") == -1:
                d1 = date1.split()
                year = d1[2]
                temp = d1[1].split(",")
                m = temp[0]
                month = Month(m)
                temp = d1[0].strip()
                date = temp[:-2]
            elif date1.find(".") != -1:
                d1 = date1.split(".")
                temp = d1[2].split("\n")
                year = temp[0]
                month = d1[1]
                date = d1[0].strip()
        elif date1.find("-") != -1:
            d1 = date1.split("-")
            temp = d1[2].split("\n")
            year = temp[0]
            month = d1[1]
            date = d1[0].strip()

    elif date1.find("/") != -1:
        d1 = date1.split("/")
        temp = d1[2].split("\n")
        year = temp[0]
        month = d1[1]
        date = d1[0].strip()
    return [year,month,date]

from datetime import date

f = open("date_calculator.txt","r")
a = f.readline().split(":")
b = f.readline().split(":")

date1 = a[1]
date2 = b[1]

f1 = open("output.txt","w")
f1.write("Date Difference:")
f1.close()

dateF1 = DateFormat(date1)
dateF2 = DateFormat(date2)

