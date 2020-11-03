monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def Month(m):
    months = [['January','February','March','April','May','June','July','August','September','October','November','December'],['Jan','Feb','Apr','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]
    if len(m) == 3:
        return (months[1].index(m) + 1)
    else:
        return (months[0].index(m) + 1)

def countLeapYears(dateF1): 
    years = int(dateF1[0])
    if (int(dateF1[1]) <= 2) : 
        years-= 1
    return int(years // 4 - years // 100 + years // 400 ) 

def getDifference(dateF1, dateF2) : 
    n1 = int(dateF1[0]) * 365 + int(dateF1[2])  
    for i in range(0, int(dateF1[1]) - 1) : 
        n1 += monthDays[i]  
    n1 += countLeapYears(dateF1)  
    n2 = int(dateF2[0]) * 365 + int(dateF2[2])
    for i in range(0, int(dateF2[1]) - 1) : 
        n2 += monthDays[i]  
    n2 += countLeapYears(dateF2)  
    return (n2 - n1)  
   

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
    return [str(year),str(month),str(date)]

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

if len(dateF1[2]) == 2:
    temp = dateF1[2]
    if(temp[0] == '0'):
        dateF1[2] = temp[1]
if len(dateF2[2]) == 2:
    temp = dateF2[2]
    if(temp[0] == '0'):
        dateF2[2] = temp[1]

if len(dateF1[1]) == 2:
    temp = dateF1[1]
    if(temp[0] == '0'):
        dateF1[1] = temp[1]
if len(dateF2[1]) == 2:
    temp = dateF2[1]
    if(temp[0] == '0'):
        dateF2[1] = temp[1]

delta = abs(getDifference(dateF1,dateF2))

f1 = open("output.txt","a")
f1.write(str(delta))
f1.write(" Days")
f1.close()
