import os, os.path, json, datetime

data = []

def open_files(Employees):
    f = []
    for i in range(0,len(Employees)):
        f.append(open("./Employee/"+Employees[i],"r"))
    x = []
    for i in range(0,len(Employees)):
        x.append((f[i].read()).replace("\'","\""))
        d = json.loads(x[i])
        data.append(d)
    
    return data

def availableSlot(data1):
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

    return lis1

def slotAvail(lis,slot):
    ans = []
    for i in lis:
        temp = i.split(" - ")
        time1 = temp[0]
        time2 = temp[1]
        tem1 = time1.split(":")
        h1 = int(tem1[0])
        m1 = tem1[1][:2]
        apm1 = tem1[1][-2:]
        if apm1 == "PM" and h1 != 12:
            h1 += 12
        final_time1 = float(h1) + float(float(m1)/60)
        tem2 = time2.split(":")
        h2 = int(tem2[0])
        m2 = tem2[1][:2]
        apm2 = tem2[1][-2:]
        if apm2 == "PM" and h2 != 12:
            h2 += 12        
        final_time2 = float(h2) + float(float(m2)/60)

        if (final_time2 - final_time1) >= float(slot):
            ans.append(i)
    return ans

print("Input slot duration\n")
slot = input()

DIR = './Employee'
Employees = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
Employees.sort()

data = open_files(Employees)

f = open("output.txt","w")
f.write("Available Slot\n")
f.close()

lis = []

for i in range(len(Employees)):
    lis.append(availableSlot(data[i]))


f = open("output.txt","a")
f.write("\n\nSlot Duration: ")
f.write(slot + " hour\n")
f.close()           

availSlotDur = []

for i in range(len(Employees)):
    availSlotDur.append(slotAvail(lis[i],slot))


