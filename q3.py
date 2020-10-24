import json

f1 = open("Employee1.txt","r")
x = f1.read()
data1 = json.loads(x.replace("\'","\""))

f2 = open("Employee2.txt","r")
x = f2.read()
data2 = json.loads(x.replace("\'","\""))

f = open("output.txt","w")
f.write("Available Slot\n")
f.close()

lis1 = []
start = '9:00AM'
slot_end = '5:00PM'
st = 0.0
for L in data1:
    f = open("output.txt","a")
    f.write(L)
    f.write(": ")
    f.close()
    for I in data1[L]:
        for J in data1[L][I]:
            j = J.split(" - ")
            temp1 = j[0].split(":")
            strt = float(temp1[0]) + float(float(temp1[1][:2])/60)
            temp2 = j[1].split(":")
            end_ = float(temp2[0]) + float(float(temp2[1][:2])/60)
            temp = start.split(":")
            start_ = float(temp[0]) + float(float(temp[1][:2])/60)
            startAPM = temp[1][-2:]
            strtAPM = temp1[1][-2:]
            endAPM = temp2[1][-2:]
            if startAPM == "PM" and int(temp[0]) != 12:
                start_ = start_ + 12
            if strtAPM == "PM" and int(temp1[0]) != 12:
                strt = strt + 12
            if endAPM == "PM"  and int(temp2[0]) != 12:
                end_ = end_ + 12                            
            if start_ < strt:
                s = start + " - " + j[0]
                lis1.append(s)
            start = j[1]
            st = end_

temp3 = slot_end.split(":")
slot_end_ = float(temp3[0]) + float(float(temp3[1][:2])/60) + 12.0

if st < slot_end_ :
    s = start + " - " + slot_end
    lis1.append(s)

str_lis1 = str(lis1)
print(str_lis1)

f = open("output.txt","a")
f.write(str_lis1)
f.write("\n")
f.close()

lis2 = []
start = '9:00AM'
slot_end = '5:00PM'

st = 0.0

for L in data2:
    f = open("output.txt","a")
    f.write(L)
    f.write(": ")
    f.close()
    for I in data2[L]:
        for J in data2[L][I]:
            j = J.split(" - ")
            temp1 = j[0].split(":")
            strt = float(temp1[0]) + float(float(temp1[1][:2])/60)
            temp2 = j[1].split(":")
            end_ = float(temp2[0]) + float(float(temp2[1][:2])/60)
            temp = start.split(":")
            start_ = float(temp[0]) + float(float(temp[1][:2])/60)
            startAPM = temp[1][-2:]
            strtAPM = temp1[1][-2:]
            endAPM = temp2[1][-2:]
            if startAPM == "PM" and int(temp[0]) != 12:
                start_ = start_ + 12
            if strtAPM == "PM" and int(temp1[0]) != 12:
                strt = strt + 12
            if endAPM == "PM" and int(temp2[0]) != 12:
                end_ = end_ + 12                            
            if start_ < strt:
                s = start + " - " + j[0]
                lis2.append(s)
            start = j[1]
            st = end_

temp3 = slot_end.split(":")
slot_end_ = float(temp3[0]) + float(float(temp3[1][:2])/60) + 12.0

if st < slot_end_ :
    s = start + " - " + slot_end
    lis2.append(s)


str_lis2 = str(lis2)
print(str_lis2)

f = open("output.txt","a")
f.write(str_lis2)
f.write("\n")
f.close()           

    

