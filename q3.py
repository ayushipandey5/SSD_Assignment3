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
    date = ""
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
            date = I
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

present = "true"

for i in range(len(Employees)):
    if(len(availSlotDur[i]) == 0):
        present = "false"

if present == "true":
    flag = ""
    ans = []
    t = ""

    final_time1 = 0.0
    final_time2 = 0.0

    for i in availSlotDur[0]:
        flag = ""
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
        # print(final_time1,final_time2)

        for j in range(len(Employees)):
            if (j != 0):
                print("i",i,"j",j)
                for k in availSlotDur[j]:
                    tempk = k.split(" - ")
                    timek1 = tempk[0]
                    timek2 = tempk[1]
                    temk1 = timek1.split(":")
                    hk1 = int(temk1[0])
                    mk1 = temk1[1][:2]
                    apmk1 = temk1[1][-2:]
                    if apmk1 == "PM" and hk1 != 12:
                        hk1 += 12
                    final_timek1 = float(hk1) + float(float(mk1)/60)
                    temk2 = timek2.split(":")
                    hk2 = int(temk2[0])
                    mk2 = temk2[1][:2]
                    apmk2 = temk2[1][-2:]
                    if apmk2 == "PM" and hk2 != 12:
                        hk2 += 12        
                    final_timek2 = float(hk2) + float(float(mk2)/60)                

                    print(final_timek1,final_timek2)
                    if(final_time1 >= final_timek1) and (final_time2 >= final_timek2) and (final_timek2 >= final_time1) and (abs(final_time1 - final_timek2) >= float(slot)):
                    
                        final_time2 = final_timek2
                        print(final_time1,final_time2)
                        print("1")

                        break

                    elif(final_time1 <= final_timek1) and (final_timek1 <= final_time2) and (final_time2 <= final_timek2) and (abs(final_timek1 - final_time2) >= float(slot)):
                        # print("2")
                        final_time1 = final_timek1
                        print(final_time1,final_time2)
                        print("2")
                        break
                    elif(final_time1 <= final_timek1) and (final_time2 >= final_timek2) and (abs(final_timek2 - final_timek1) >= float(slot)):
                        # print("3")
                        final_time1 = final_timek1
                        final_time2 = final_timek2
                        print(final_time1,final_time2)
                        print("3")
                        break
                    elif(final_time1 >= final_timek1) and (final_time2 <= final_timek2) and (abs(final_time1 - final_time2) >= float(slot)):
                        break
                    elif(final_time1 >= final_timek2):
                        pass
                    else:
                        # print("4")
                        flag = "false"
                        print(final_time1,final_time2)
                        print("4")
                        break
                if flag == "false":
                    break
        if flag == "":
            if final_time1 > 12.0:
                final_time1 -= 12.0
            hr = int(final_time1)
            mn = int((final_time1 - float(hr)) * 60)
            if len(str(mn)) == 2:
                s1 = str(hr) + ":" + str(mn)
            else:
                s1 = str(hr) + ":" + str(mn) + "0"
            if hr == 12 or hr < 9:
                s1 = s1 + "PM"
            else:
                s1 = s1 + "AM"  

            final_time2 = final_time1 + float(slot)

            if final_time2 > 12.0:
                final_time2 -= 12.0
            hr = int(final_time2)
            mn = int((final_time2 - float(hr)) * 60)
            if len(str(mn)) == 2:
                s2 = str(hr) + ":" + str(mn)
            else:
                s2 = str(hr) + ":" + str(mn) + "0"
            if hr == 12 or hr < 9:
                s2 = s2 + "PM"
            else:
                s2 = s2 + "AM"  

            fin = s1 + " - " + s2
            ans.append(fin)
            t = "true"
            break


    if(t == ""):
        f = open("output.txt","a")
        f.write("No common slot available")
        f.close()   
    elif(t == "true"):
        f = open("output.txt","a")
        d = {}
        date = ""
        for L in data[0]:
            for I in data[0][L]:
                date = I
        d[date] = ans
        f = open("output.txt","a")
        f.write(str(d))
        f.close()   

elif present == "false":
    f = open("output.txt","a")
    f.write("No common slot available")
    f.close()      
