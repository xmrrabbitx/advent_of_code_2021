inp = open("input.txt")

r = inp.readlines()

arr = []


for x in r:

    l = x.rstrip("\n")
    arr.append(int(l))

i = 0
incr = []

while i <= (len(arr)-1):
        
    if(i+1 <= (len(arr)-1)):
        if(arr[i] < arr[i+1]):
            incr.append("increased")

    i += 1

print(len(incr))
