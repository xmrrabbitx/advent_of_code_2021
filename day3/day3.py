#part 1

import numpy as np
from collections import Counter


inp = open("input.txt")

r = inp.readlines()

arr = [[],[],[],[],[],[],[],[],[],[],[],[]]

my_list = []

for x in r:
    l = x.rstrip("\n")
    my_list.append(list(l))
    for n in range(len(arr)):
        arr[n].append(int(l[n]))


gamma = []
ep = []
for g in range(len(arr)):

    (unique, counts) = np.unique(arr[g], return_counts=True)

    freq = np.asarray((counts)).T
    
    if(int(freq[0:1]) > int(freq[1:2])):
        gamma.append(int((np.asarray(( unique)).T)[0:1]))
    else:
        gamma.append(int((np.asarray(( unique)).T)[1:2]))
    if(int(freq[0:1]) < int(freq[1:2])):
        ep.append(int((np.asarray(( unique)).T)[0:1]))
    else:
        ep.append(int((np.asarray(( unique)).T)[1:2]))


gammadc = int(''.join(map(lambda gamma: str(int(gamma)),gamma)),2)
epdc = int(''.join(map(lambda ep: str(int(ep)), ep)), 2)

print(gammadc * epdc)



#part 2


ar = np.array(my_list)

oxgen = []

for i in range(12):
    col = ar[:, i]

    if(Counter(col)['1'] > Counter(col)['0']):
        y = "1"
    elif(Counter(col)['1'] == Counter(col)['0']):
        y = "1"
    else:
        y = "0"
    
    f = [row for row in ar if y in row[i]]
    
    if(len(f) < 1):
        break
    
    ar = np.array(f)

    oxgen = f


arco2 = np.array(my_list)

co2 = []

for g in range(len(arco2)):
    colco2 = arco2[:, g]

    if(Counter(colco2)['1'] < Counter(colco2)['0']):
        m = "1"
    elif(Counter(colco2)['1'] == Counter(colco2)['0']):
        m = "0"
    else:
        m = "0"
    
    fco2 = [row2 for row2 in arco2 if m in row2[g]]

    arco2 = np.array(fco2)

    if(len(fco2) < 1):
        break
    

    co2 = fco2


def converter(list):
    s = [str(i) for i in list]
    res = int(''.join(s))
    return (res)

oxgen = int(str(converter(oxgen[0])),2)
co2scrub = int(str(converter(co2[0])),2)


print(oxgen * co2scrub)