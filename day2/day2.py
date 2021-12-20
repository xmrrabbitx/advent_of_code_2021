#part 1 && 2

forward = []
down = []
up = []
aim = int()
depth = []

with open("input.txt") as f:
    for line in f:
       a = line.split()
       if(a[0] == "forward"):
           forward.append(int(a[1]))
           if(aim != ""):
               depth.append(aim * int(a[1]))
       elif(a[0] == "down"):
           down.append(int(a[1]))
           if(aim != ""):
               aim = aim + int(a[1])
       elif(a[0] == "up"):
            up.append(int(a[1]))
            if(aim != ""):
               aim = aim - int(a[1])

horz = sum(forward)
dept = sum(down) - sum(up)



print(horz * sum(depth))
