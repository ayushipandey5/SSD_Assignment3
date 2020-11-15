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
par_at_min_level = [i for i in levels]
parents = [i for i in elements]


def levelMatch(plevel,i):
    while plevel != min_level:
        for L in data:
            for dicts in data[L]:
                if dicts["name"] == parents[i]:
                    if int(L[1]) > 0:
                        plevel = int(L[1]) -1
                        parents[i] = dicts["parent"]
    return

def First():
    res = False
    for i in range(size):
        if par_at_min_level[i] != min_level:
            plevel = par_at_min_level[i]
            levelMatch(plevel,i)
            par_at_min_level[i] = plevel

        res = all(ele == parents[0] for ele in parents)
    return res

def ifParentDiff(res):
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
    return res

def Second(res):
    if (res == False):
        res = ifParentDiff(res)
        print("Common leader : " + parents[0])
        for i in range(size):
            print("Leader " + parents[0] + " is " + str(levels[i] - par_at_min_level[i]) +" levels above employee " + elements[i])
        exit()
    return res

def ifParentSame(i):
    if par_at_min_level[i] > 0:
        for L in data:
            for dicts in data[L]:
                    if dicts["name"] == parents[i]:
                        if int(L[1]) > 0:
                            plevel = int(L[1]) -1
                            parents[i] = dicts["parent"]
        par_at_min_level[i] = plevel 
    return


def Third(res):
    if (res):
        for i in range(size):
            ifParentSame(i)
        print("Common leader : " + parents[0])
        for i in range(size):
            print("Leader " + parents[0] + " is " + str(levels[i] - par_at_min_level[i]) +" levels above employee " + elements[i])    
        exit()
    return



def Solution():
    if min_level == 0:
        print("No leader")
    else:
        res = First()
        res = Second(res)        
        Third(res)

    return


Solution()
