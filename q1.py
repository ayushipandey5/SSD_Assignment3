import json

f = open('org.json',)
data = json.load(f)
f.close()


print("Enter the EmpIds\n")
ele = []

ele = input().split()
elements = [i for i in ele[1:]]
size = len(elements)
levels = [-1 for i in range(size)]

for L in data:
    for dicts in data[L]:
        if dicts["name"] in elements: 
            levels[elements.index(dicts["name"])] = int(L[1])

min_level = min(levels)
if min_level == 0:
    print("No leader")
else:
    par_at_min_level = [i for i in levels]
    parents = [i for i in elements]
    for i in range(size):
        if par_at_min_level[i] != min_level:
            plevel = par_at_min_level[i]
            while plevel != min_level:
                for L in data:
                    for dicts in data[L]:
                        if dicts["name"] == parents[i]:
                            if int(L[1]) > 0:
                                plevel = int(L[1]) -1
                                parents[i] = dicts["parent"]
            par_at_min_level[i] = plevel

    res = all(ele == parents[0] for ele in parents)
    if (res == False):
        while(res == False):
            for i in range(size):
                if par_at_min_level[i] > 0:
                    for L in data:
                        for dicts in data[L]:
                            if dicts["name"] == parents[i]:
                                if int(L[1]) > 0:
                                    plevel = int(L[1]) -1
                                    parents[i] = dicts["parent"]
                par_at_min_level[i] = plevel                
            res = all(ele == parents[0] for ele in parents)
        print("Common leader : " + parents[0])
        for i in range(size):
            print("Leader " + parents[0] + " is " + str(levels[i] - par_at_min_level[i]) +" levels above employee " + elements[i])
        
    elif (res):
        for i in range(size):
            if par_at_min_level[i] > 0:
                for L in data:
                    for dicts in data[L]:
                            if dicts["name"] == parents[i]:
                                if int(L[1]) > 0:
                                    plevel = int(L[1]) -1
                                    parents[i] = dicts["parent"]
                par_at_min_level[i] = plevel 
        print("Common leader : " + parents[0])
        for i in range(size):
            print("Leader " + parents[0] + " is " + str(levels[i] - par_at_min_level[i]) +" levels above employee " + elements[i])
