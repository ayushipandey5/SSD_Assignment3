import json

print("Input slot duration\n")
slot = input()

f1 = open("Employee1.txt","r")
x = f1.read()
data1 = json.loads(x.replace("\'","\""))

f2 = open("Employee2.txt","r")
x = f2.read()
data2 = json.loads(x.replace("\'","\""))

f = open("output.txt","w")
f.write("Available Slot\n")
f.close()

date1 = " " 

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
        date1 = I
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

f = open("output.txt","a")
f.write(str_lis1)
f.write("\n")
f.close()

lis2 = []
start = '9:00AM'
slot_end = '5:00PM'

st = 0.0

date2 = " "

for L in data2:
    f = open("output.txt","a")
    f.write(L)
    f.write(": ")
    f.close()
    for I in data2[L]:
        date2 = I
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

f = open("output.txt","a")
f.write(str_lis2)
f.write("\n\nSlot Duration: ")
f.write(slot + " hour\n")
f.close()           

lis = []
lis_max = []

if len(lis1) <= len(lis2):
    lis = lis1
    lis_max = lis2
else:
    lis = lis2
    lis_max = lis1

ans = " "

for i in lis:
    temp = i.split(" - ")
    temp1 = temp[0].split(":")
    strt = float(temp1[0]) + float(float(temp1[1][:2])/60)
    temp2 = temp[1].split(":")
    end_ = float(temp2[0]) + float(float(temp2[1][:2])/60)
    strtAPM = temp1[1][-2:]
    endAPM = temp2[1][-2:]
    if strtAPM == "PM" and int(temp1[0]) != 12:
        strt = strt + 12
    if endAPM == "PM" and int(temp2[0]) != 12:
        end_ = end_ + 12                            
    st_end = strt + float(slot)
    if st_end <= end_ and date1 == date2:
        # search in lis_max if same slot available 
        for j in lis_max:
            tem = j.split(" - ")
            tem1 = tem[0].split(":")
            strt_max = float(tem1[0]) + float(float(tem1[1][:2])/60)
            tem2 = tem[1].split(":")
            end_max = float(tem2[0]) + float(float(tem2[1][:2])/60)
            strt_maxAPM = tem1[1][-2:]
            end_maxAPM = tem2[1][-2:]
            if strt_maxAPM == "PM" and int(tem1[0]) != 12:
                strt_max = strt_max + 12
            if end_maxAPM == "PM" and int(tem2[0]) != 12:
                end_max = end_max + 12                            
            st_end_max = strt_max + float(slot)
            if st_end_max <= end_max:
                if strt_max <= strt and end_max <= end_ and end_max > strt:
                    if end_max - strt >= float(slot):
                        e = strt + float(slot)
                        if(e>12.0):
                            e = e - 12.0
                        hr = int(e)
                        mn = int((e - float(hr)) * 60)
                        s = str(hr) + ":" + str(mn)
                        if hr == 12 or hr < 9:
                            s = s + "PM"
                        else:
                            s = s + "AM"                        
                        ans = temp[0] + " - " + s
                        break
                elif strt_max >= strt and end_max >= end_ and strt_max < end_:
                    if end_ - strt_max >= float(slot):
                        e = strt_max + float(slot)
                        if(e>12.0):
                            e = e - 12.0
                        hr = int(e)
                        mn = int((e - float(hr)) * 60)
                        s = str(hr) + ":" + str(mn)
                        if hr == 12 or hr < 9:
                            s = s + "PM"
                        else:
                            s = s + "AM"                        
                        ans = tem[0] + " - " + s
                        break
                elif strt_max >= strt and end_max <= end_:
                        e = strt_max + float(slot)
                        if(e>12.0):
                            e = e - 12.0
                        hr = int(e)
                        mn = int((e - float(hr)) * 60)
                        s = str(hr) + ":" + str(mn)
                        if hr == 12 or hr < 9:
                            s = s + "PM"
                        else:
                            s = s + "AM"
                        ans = tem[0] + " - " + s
                        break
                elif strt_max <= strt and end_max >= end_:
                        e = strt + float(slot)
                        if(e>12.0):
                            e = e - 12.0
                        hr = int(e)
                        mn = int((e - float(hr)) * 60)
                        s = str(hr) + ":" + str(mn)
                        if hr == 12 or hr < 9:
                            s = s + "PM"
                        else:
                            s = s + "AM"
                        ans = temp[0] + " - " + s
                        break
        if ans != " ":
            l = []
            l.append(ans)
            d = {}
            d[date1] = l
            f = open("output.txt","a")
            f.write(str(d))
            f.close()   
            break

if ans == " ":
    f = open("output.txt","a")
    f.write("No common slot available")
    f.close()   
