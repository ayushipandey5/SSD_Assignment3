import json

f = open('org.json',)
data = json.load(f)

print("Enter two EmpIds\n")
a, b = map(int, input().split())

name_a = a
name_b = b

level_a = -1
level_b = -1
level_p = -1

for L in data:
    for dicts in data[L]:
        if dicts["name"] == name_a:
            level_a = int(L[1])
        if dicts["name"] == name_b:
            level_b = int(L[1])


org_lev_a = level_a
org_lev_b = level_b

if level_a > level_b:
    while(level_b != level_a):
        for L in data:
            for dicts in data[L]:
                if dicts["name"] == name_a:
                    if int(L[1]) > 0:
                        level_a = int(L[1]) - 1
                        name_a = dicts["parent"]

if level_a < level_b:
    while(level_b != level_a):
        for L in data:
            for dicts in data[L]:
                if dicts["name"] == name_b:
                    if int(L[1]) > 0:
                        level_b = int(L[1]) -1
                        name_b = dicts["parent"]

if level_a == level_b:
    parent = -1
    for L in data:
        for dicts in data[L]:
            if dicts["name"] == name_b:
                if int(L[1]) > 0:
                    level_p = int(L[1]) -1
                    parent = dicts["parent"]
                else:
                    print("No Leader")
                    break
    if level_p != -1:
        print(str(parent) + "\n" + str(parent) + " is " + str(org_lev_a - level_p) + " levels above " + str(a) + "\n" + str(parent) + " is " + str(org_lev_b - level_p) + " levels above " + str(b))

f.close()
