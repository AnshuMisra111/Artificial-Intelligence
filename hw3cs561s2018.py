import time

file = (open("/Users/anshuman786/Downloads/Sample_test_cases 2/input2.txt", "r")).readlines()
#file = (open("input.txt")).readlines()
start_time = time.time()
row, column = file[0].split("\n")[0].split(",")
row = int(row)
column = int(column)

wnumber = file[1].split("\n")[0]
wall = []
for i in range(0, row):
    walls = []
    for j in range(0, column):
        walls.append(False)
    wall.append(walls)

for i in range(0, int(wnumber)):
    temp = file[1 + (i + 1)].split("\n")[0].split(",")
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    wall[temp[0] - 1][temp[1] - 1] = True

tnumber = file[2 + int(wnumber)]
tstates = []

for i in range(0, row):
    walls = []
    for j in range(0, column):
        walls.append([False, 0])
    tstates.append(walls)

for i in range(0, int(tnumber)):
    temp = file[2 + int(wnumber) + (i + 1)].split("\n")[0].split(",")
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    temp[2] = float(temp[2])

    tstates[temp[0] - 1][temp[1] - 1] = [True, temp[2]]

wnumber = int(wnumber)
pwalk, prun = file[3 + int(wnumber) + int(tnumber)].split("\n")[0].split(",")
pwalk = float(pwalk)
prun = float(prun)

rwalk, rrun = file[4 + int(wnumber) + int(tnumber)].split("\n")[0].split(",")
rwalk = float(rwalk)
rrun = float(rrun)

factor = file[5 + int(wnumber) + int(tnumber)].split("\n")[0]
factor = float(factor)
# factor=1
# factor=((1/factor)-1)
value2 = []
value = []
policy = []
checker = []
max = 0.0
start = []
flag = []
for i in range(0, row):
    values = []
    policies = []
    checks = []
    flags = []
    for j in range(0, column):
        flags.append(False)
        if tstates[i][j][0] == True:
            checks.append(True)
            values.append(tstates[i][j][1])
            policies.append("Exit")
            if tstates[i][j][1] > max:
                # print("came here", i ,j)
                if len(start) > 0:
                    start[:] = []
                max = tstates[i][j][1]
                start.append(i)
                start.append(j)
        else:
            checks.append(False)
            values.append(0)
            if wall[i][j] == True:
                policies.append("None")
            else:
                policies.append("")
    flag.append(flags)
    value.append(values)
    value2.append(values)
    checker.append(checks)
    policy.append(policies)

change = 1


def max(temp1, dir1, temp2, dir2, temp3, dir3, temp4, dir4):
    if temp1 >= temp2:
        if temp1 >= temp3:
            if temp1 >= temp4:
                return temp1, dir1
            else:
                return temp4, dir4
        else:
            if temp3 >= temp4:
                return temp3, dir3
            else:
                return temp4, dir4
    else:
        if temp2 >= temp3:
            if temp2 >= temp4:
                return temp2, dir2
            else:
                return temp4, dir4
        else:
            if temp3 >= temp4:
                return temp3, dir3
            else:
                return temp4, dir4


def run(rownumber, colnumber):
    # ans = 0
    # direction = ""
    if tstates[rownumber][colnumber][0] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]

    if wall[rownumber][colnumber] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]
    dir1 = "Up"
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    # print("1st",rownumber,colnumber)
    if dir1 == "Up":
        # temp1 = 0
        # print("Came here up= ",rownumber,colnumber)
        # temp1 = temp1 + rrun
        if rownumber < row - 2:
            if wall[rownumber + 2][colnumber] == False and wall[rownumber + 1][colnumber] == False:
                # temp1 = temp1 + (factor*(prun * value[rownumber + 2][colnumber]))
                temp1 = temp1 + (prun) * (rrun + (factor * value[rownumber + 2][colnumber]))
            else:
                # temp1=temp1+(factor * (prun * value[rownumber][colnumber]))
                temp1 = temp1 + (prun) * (rrun + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + (factor * (prun * value[rownumber][colnumber]))
            temp1 = temp1 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber > 1:
            if wall[rownumber][colnumber - 2] == False and wall[rownumber][colnumber - 1] == False:
                # temp1 = temp1 + factor*((0.5)*(1 - prun) * value[rownumber][colnumber - 2])
                temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber - 2]))
            else:
                # temp1 = temp1 + (factor * ((0.5) * (1 - prun) * value[rownumber][colnumber]))
                temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + (factor * ((0.5) * (1 - prun) * value[rownumber][colnumber]))
            temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber < column - 2:
            if wall[rownumber][colnumber + 2] == False and wall[rownumber][colnumber + 1] == False:
                # temp1 = temp1 + factor*((0.5)*(1 - prun) * value[rownumber][colnumber + 2])
                temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber + 2]))
            else:
                # temp1 = temp1 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp1 = temp1 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp
        # direction = dir

    dir2 = "Down"
    if dir2 == "Down":
        # temp2 = 0
        # temp2 = temp2 + rrun
        if rownumber > 1:
            if wall[rownumber - 2][colnumber] == False and wall[rownumber - 1][colnumber] == False:
                # temp2 = temp2 + factor*(prun * value[rownumber - 2][colnumber])
                temp2 = temp2 + (prun) * (rrun + (factor * value[rownumber - 2][colnumber]))
            else:
                # temp2 = temp2 + factor * (prun * value[rownumber][colnumber])
                temp2 = temp2 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp2 = temp2 + factor * (prun * value[rownumber][colnumber])
            temp2 = temp2 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber > 1:
            if wall[rownumber][colnumber - 2] == False and wall[rownumber][colnumber - 1] == False:
                # temp2 = temp2 + factor*((0.5)*(1 - prun) * value[rownumber][colnumber - 2])
                temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber - 2]))
            else:
                # temp2 = temp2 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp2 = temp2 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber < column - 2:
            if wall[rownumber][colnumber + 2] == False and wall[rownumber][colnumber + 1] == False:
                # temp2 = temp2 + factor*((0.5)*(1 - prun) * value[rownumber][colnumber + 2])
                temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber + 2]))
            else:
                # temp2 = temp2 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp2 = temp2 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp2 = temp2 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp
        # direction = dir

    dir3 = "Left"
    if dir3 == "Left":
        # temp4 = 0
        # temp4 = temp4 + rrun
        if rownumber < row - 2:
            if wall[rownumber + 2][colnumber] == False and wall[rownumber + 1][colnumber] == False:
                # temp4 = temp4 + factor*((0.5)*(1 - prun) * value[rownumber + 2][colnumber])
                temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber + 2][colnumber]))
            else:
                # temp4 = temp4 + factor*((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp4 = temp4 + factor*((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if rownumber > 1:
            if wall[rownumber - 2][colnumber] == False and wall[rownumber - 1][colnumber] == False:
                # temp4 = temp4 + ((0.5)*(1 - prun) * value[rownumber - 2][colnumber])
                temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber - 2][colnumber]))
            else:
                # temp4 = temp4 + ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp4 = temp4 + ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp4 = temp4 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber > 1:
            if wall[rownumber][colnumber - 2] == False and wall[rownumber][colnumber - 1] == False:
                # temp4 = temp4 + factor*((prun) * value[rownumber][colnumber - 2])
                temp4 = temp4 + (prun) * (rrun + (factor * value[rownumber][colnumber - 2]))
            else:
                # temp4 = temp4 + factor * ((prun) * value[rownumber][colnumber])
                temp4 = temp4 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp4 = temp4 + factor * ((prun) * value[rownumber][colnumber])
            temp4 = temp4 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

    dir4 = "Right"
    if dir4 == "Right":
        # temp3 = 0
        # temp3 = temp3 + rrun
        if rownumber < row - 2:
            if wall[rownumber + 2][colnumber] == False and wall[rownumber + 1][colnumber] == False:
                # temp3 = temp3 + factor*((0.5)*(1 - prun) * value[rownumber + 2][colnumber])
                temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber + 2][colnumber]))
            else:
                # temp3 = temp3 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp3 = temp3 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if rownumber > 1:
            if wall[rownumber - 2][colnumber] == False and wall[rownumber - 1][colnumber] == False:
                # temp3 = temp3 + ((0.5)*(1 - prun) * value[rownumber - 2][colnumber])
                temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber - 2][colnumber]))
            else:
                # temp3 = temp3 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
                temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp3 = temp3 + factor * ((0.5) * (1 - prun) * value[rownumber][colnumber])
            temp3 = temp3 + (0.5) * (1 - prun) * (rrun + (factor * value[rownumber][colnumber]))

        if colnumber < column - 2:
            if wall[rownumber][colnumber + 2] == False and wall[rownumber][colnumber + 1] == False:
                # temp3 = temp3 + factor*((prun) * value[rownumber][colnumber + 2])
                temp3 = temp3 + (prun) * (rrun + (factor * value[rownumber][colnumber + 2]))
            else:
                # temp3 = temp3 + factor * ((prun) * value[rownumber][colnumber])
                temp3 = temp3 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        else:
            # temp3 = temp3 + factor * ((prun) * value[rownumber][colnumber])
            temp3 = temp3 + (prun) * (rrun + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp3
        # direction = dir

        # if temp > ans:
        # ans = temp
        # direction = dir

    # print("2nd",rownumber,colnumber)

    ans, direction = max(temp1, dir1, temp2, dir2, temp4, dir3, temp3, dir4)

    # ans=round(ans,1)
    # ans=ans+rrun
    return ans, direction


def walk(rownumber, colnumber):
    # ans=0
    # direction=""
    if tstates[rownumber][colnumber][0] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]

    if wall[rownumber][colnumber] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]

    dir1 = "Up"
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    if dir1 == "Up":
        # temp1=0
        # temp1=temp1+rwalk
        if rownumber < row - 1:
            if wall[rownumber + 1][colnumber] == False:
                # temp1 = temp1 + factor * (pwalk * value[rownumber+1][colnumber])
                # if rownumber==1 and colnumber==1:
                # print("1st=",value[rownumber+1][colnumber],temp1)
                temp1 = temp1 + pwalk * (rwalk + (factor * value[rownumber + 1][colnumber]))
            else:
                # temp1 = temp1 + factor * (pwalk * value[rownumber][colnumber])
                temp1 = temp1 + pwalk * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + factor * (pwalk * value[rownumber][colnumber])
            temp1 = temp1 + pwalk * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber > 0:
            if wall[rownumber][colnumber - 1] == False:
                # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber-1])
                # if rownumber == 1 and colnumber == 1:
                # print("2nd=",value[rownumber][colnumber-1], temp1)
                temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber - 1]))
            else:
                # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber < column - 1:
            if wall[rownumber][colnumber + 1] == False:
                # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber+1])
                # if rownumber == 1 and colnumber == 1:
                # print("3rd",value[rownumber][colnumber+1], temp1)
                temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber + 1]))
            else:
                # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp1 = temp1 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp1 = temp1 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        # if temp>ans:
        # ans=temp
        # direction=dir

    dir2 = "Down"
    if dir2 == "Down":
        # temp2 = 0
        # temp2 = temp2 + rwalk
        if rownumber > 0:
            if wall[rownumber - 1][colnumber] == False:
                # temp2 = temp2 + factor*(pwalk * value[rownumber - 1][colnumber])
                temp2 = temp2 + pwalk * (rwalk + (factor * value[rownumber - 1][colnumber]))
            else:
                # temp2=temp2+factor*(pwalk*value[rownumber][colnumber])
                temp2 = temp2 + pwalk * (rwalk + (factor * value[rownumber][colnumber]))

        else:
            # temp2 = temp2 + factor * (pwalk * value[rownumber][colnumber])
            temp2 = temp2 + pwalk * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber > 0:
            if wall[rownumber][colnumber - 1] == False:
                # temp2 = temp2 +factor*((0.5) * (1 - pwalk) * (value[rownumber][colnumber - 1]))
                temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber - 1]))
            else:
                # temp2 = temp2 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp2 = temp2 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber < column - 1:
            if wall[rownumber][colnumber + 1] == False:
                # temp2 = temp2 + factor*((0.5)*(1 - pwalk) * value[rownumber][colnumber + 1])
                temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber + 1]))
            else:
                # temp2 = temp2 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp2 = temp2 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp2 = temp2 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp
        # direction=dir

    dir3 = "Left"
    if dir3 == "Left":
        # temp3 = 0
        # temp3 = temp3 + rwalk
        if rownumber < row - 1:
            if wall[rownumber + 1][colnumber] == False:
                # temp3 = temp3 + factor*((0.5)*(1-pwalk) * value[rownumber + 1][colnumber])
                temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber + 1][colnumber]))
            else:
                # temp3 = temp3 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp3 = temp3 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if rownumber > 0:
            if wall[rownumber - 1][colnumber] == False:
                # temp3 = temp3 + factor*((0.5)*(1 - pwalk) * value[rownumber-1][colnumber])
                temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber - 1][colnumber]))
            else:
                # temp3 = temp3 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp3 = temp3 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp3 = temp3 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber > 0:
            if wall[rownumber][colnumber - 1] == False:
                # temp3 = temp3 + factor*((pwalk) * value[rownumber][colnumber - 1])
                temp3 = temp3 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber - 1]))
            else:
                # temp3 = temp3 + factor * ((pwalk) * value[rownumber][colnumber])
                temp3 = temp3 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp3 = temp3 + factor * ((pwalk) * value[rownumber][colnumber])
            temp3 = temp3 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp
        # direction = dir

    dir4 = "Right"
    if dir4 == "Right":
        # temp4 = 0
        # temp4 = temp4 + rwalk
        if rownumber < row - 1:
            if wall[rownumber + 1][colnumber] == False:
                # temp4 = temp4 + factor*((0.5)*(1-pwalk) * value[rownumber + 1][colnumber])
                temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber + 1][colnumber]))
            else:
                # temp4 = temp4 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp4 = temp4 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if rownumber > 0:
            if wall[rownumber - 1][colnumber] == False:
                # temp4 = temp4 + factor*((0.5)*(1 - pwalk) * value[rownumber-1][colnumber])
                temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber - 1][colnumber]))
            else:
                # temp4 = temp4 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
                temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp4 = temp4 + factor * ((0.5) * (1 - pwalk) * value[rownumber][colnumber])
            temp4 = temp4 + (0.5) * (1 - pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        if colnumber < column - 1:
            if wall[rownumber][colnumber + 1] == False:
                # temp4 = temp4 + factor*((pwalk) * value[rownumber][colnumber + 1])
                temp4 = temp4 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber + 1]))
            else:
                # temp4 = temp4 + factor * ((pwalk) * value[rownumber][colnumber])
                temp4 = temp4 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber]))
        else:
            # temp4 = temp4 + factor * ((pwalk) * value[rownumber][colnumber])
            temp4 = temp4 + (pwalk) * (rwalk + (factor * value[rownumber][colnumber]))

        # if temp > ans:
        # ans = temp
        # direction = dir
        # if rownumber==1 and colnumber==1:
        # print(temp1,temp4)
    # if rownumber==0 and colnumber==0:
    # print(temp1,temp2,temp3,temp4)
    ans, direction = max(temp1, dir1, temp2, dir2, temp3, dir3, temp4, dir4)
    # if rownumber==0 and colnumber==0:
    # print(ans, direction)

    # ans=round(ans,1)
    # ans=ans+rwalk
    return ans, direction


def utility(rownumber, colnumber):
    if tstates[rownumber][colnumber][0] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]

    if wall[rownumber][colnumber] == True:
        return value[rownumber][colnumber], policy[rownumber][colnumber]

    walk_utility, walk_direction = walk(rownumber, colnumber)
    run_utility, run_direction = run(rownumber, colnumber)
    # if rownumber==1 and colnumber==1:
    # print(walk_utility,walk_direction,run_utility,run_direction,value[1][0],value[2][1],value[1][2],value[0][1])
    # print(walk_utility,run_utility)
    if walk_utility >= run_utility:
        return walk_utility, "Walk " + walk_direction
    else:
        return run_utility, "Run " + run_direction


def diff(a, b):
    if (a == "Exit") or (a == "None") or (b == "Exit") or (b == "None"):
        return 0
    dict = {"Walk Up": 8, "Walk Down": 7, "Walk Left": 5, "Walk Right": 4, "Run Up": 3, "Run Down": 2, "Run Left": 1,
            "Run Right": 0}
    return dict[a] - dict[b]




# for i in range(row-1,-1,-1):
# print(value[i])


traverse = []
# traverse.append(start)
m = 0

gamma = 1
m = 0
rate = 0.5

while ((gamma > 0.0) and ((time.time() - start_time) < 176)):
    m += 1

    for i in range(0, row):
        for j in range(0, column):
            flag[i][j] = False

    gamma = 0.0
    traverse.append(start)
    while (len(traverse) != 0):

        points = traverse.pop(0)
        x = points[0]
        y = points[1]

        if ((x >= 0) and (x < row)) and ((y >= 0) and (y < column)):

            if wall[x][y] == True:
                policy[x][y] = "None"
                list1 = []
                if (x + 1 >= 0) and (x + 1 < row) and (y >= 0) and (y < column) and (flag[x + 1][y] == False):

                    flag[x + 1][y] = True
                    newvalue, direction = utility(x + 1, y)
                    if value[x + 1][y] != newvalue:
                        gamma = gamma + abs(value[x + 1][y] - newvalue)
                        value[x + 1][y] = newvalue

                        policy[x + 1][y] = direction
                    else:
                        #a = diff(policy[x + 1][y], direction)

                        policy[x + 1][y] = direction
                    list1.append(x + 1)
                    list1.append(y)
                    traverse.append(list1)

                list1 = []
                if (x - 1 >= 0) and (x - 1 < row) and (y >= 0) and (y < column) and (
                        flag[x - 1][y] == False):  # and (wall[x - 1][y] == False) and (
                    # tstates[x - 1][y][0] == False) and (flag[x-1][y]==False):
                    # print("Entered")
                    flag[x - 1][y] = True

                    newvalue, direction = utility(x - 1, y)
                    if value[x - 1][y] != newvalue:
                        gamma = gamma + abs(value[x - 1][y] - newvalue)
                        value[x - 1][y] = newvalue
                        # value[x-1][y]+=rate*(newvalue-value[x-1][y])
                        policy[x - 1][y] = direction
                    else:
                        #a = diff(policy[x - 1][y], direction)
                        # if (a < 0):
                        policy[x - 1][y] = direction

                    list1.append(x - 1)
                    list1.append(y)
                    traverse.append(list1)

                list1 = []
                if (x >= 0) and (x < row) and (y - 1 >= 0) and (y - 1 < column) and (
                        flag[x][y - 1] == False):  # and (wall[x][y - 1] == False) and (
                    # tstates[x][y - 1][0] == False) and (flag[x][y-1]==False):
                    newvalue, direction = utility(x, y - 1)
                    flag[x][y - 1] = True
                    if value[x][y - 1] != newvalue:
                        gamma = gamma + abs(value[x][y - 1] - newvalue)
                        value[x][y - 1] = newvalue
                        # value[x][y-1]+=rate*(newvalue-value[x][y-1])
                        policy[x][y - 1] = direction
                    else:
                        #a = diff(policy[x][y - 1], direction)
                        # if (a < 0):
                        policy[x][y - 1] = direction
                    list1.append(x)
                    list1.append(y - 1)
                    # if list1 not in traverse:
                    traverse.append(list1)
                    # print("came to this")
                list1 = []
                if (x >= 0) and (x < row) and (y + 1 >= 0) and (y + 1 < column) and (
                        flag[x][y + 1] == False):  # and (wall[x][y + 1] == False) and (
                    # tstates[x][y + 1][0] == False) and (flag[x][y+1]==False):

                    flag[x][y + 1] = True
                    newvalue, direction = utility(x, y + 1)
                    if value[x][y + 1] != newvalue:
                        gamma = gamma + abs(value[x][y + 1] - newvalue)
                        value[x][y + 1] = newvalue
                        # value[x][y+1]+=rate*(newvalue-value[x][y+1])
                        policy[x][y + 1] = direction
                    else:
                       #a = diff(policy[x][y + 1], direction)
                        # if (a < 0):
                        policy[x][y + 1] = direction
                    list1.append(x)
                    list1.append(y + 1)
                    # if list1 not in traverse:
                    traverse.append(list1)

            else:
                if tstates[x][y][0] == True:
                    # print("what is here",x,y)
                    list1 = []
                    if (x + 1 >= 0) and (x + 1 < row) and (y >= 0) and (y < column) and (
                            flag[x + 1][y] == False):  # and (wall[x + 1][y] == False) and (
                        # tstates[x + 1][y][0] == False) and (flag[x+1][y]==False):
                        # print("Enters1")
                        flag[x + 1][y] = True
                        newvalue, direction = utility(x + 1, y)
                        if value[x + 1][y] != newvalue:
                            gamma = gamma + abs(value[x + 1][y] - newvalue)
                            value[x + 1][y] = newvalue
                            # value[x+1][y]+=rate*(newvalue-value[x+1][y])
                            policy[x + 1][y] = direction
                        else:
                            #a = diff(policy[x + 1][y], direction)
                            # if (a < 0):
                            policy[x + 1][y] = direction
                        list1.append(x + 1)
                        list1.append(y)
                        # if list1 not in traverse:
                        traverse.append(list1)

                    list1 = []
                    if (x - 1 >= 0) and (x - 1 < row) and (y >= 0) and (y < column) and (
                            flag[x - 1][y] == False):  # and (wall[x - 1][y] == False) and (
                        # tstates[x - 1][y][0] == False) and (flag[x-1][y]==False):
                        # print("Entered")
                        # print("Enters2")
                        flag[x - 1][y] = True
                        newvalue, direction = utility(x - 1, y)
                        if value[x - 1][y] != newvalue:
                            gamma = gamma + abs(value[x - 1][y] - newvalue)
                            value[x - 1][y] = newvalue
                            # value[x-1][y]+=rate*(newvalue-value[x-1][y])
                            policy[x - 1][y] = direction
                        else:
                            #a = diff(policy[x - 1][y], direction)
                            # if (a < 0):
                            policy[x - 1][y] = direction
                        list1.append(x - 1)
                        list1.append(y)
                        # if list1 not in traverse:
                        traverse.append(list1)
                    # print("this is=", x - 1,row, y, wall[x - 1][y], tstates[x - 1][y][0], len(traverse))

                    list1 = []
                    if (x >= 0) and (x < row) and (y - 1 >= 0) and (y - 1 < column) and (
                            flag[x][y - 1] == False):  # and (wall[x][y - 1] == False) and (
                        # tstates[x][y - 1][0] == False) and (flag[x][y-1]==False):
                        # print("Enters3")
                        newvalue, direction = utility(x, y - 1)
                        flag[x][y - 1] = True
                        if value[x][y - 1] != newvalue:
                            gamma = gamma + abs(value[x][y - 1] - newvalue)
                            value[x][y - 1] = newvalue
                            # value[x][y-1]+=rate*(newvalue-value[x][y-1])
                            policy[x][y - 1] = direction
                        else:
                            #a = diff(policy[x][y - 1], direction)
                            # if (a < 0):
                            policy[x][y - 1] = direction
                        list1.append(x)
                        list1.append(y - 1)
                        # if list1 not in traverse:
                        traverse.append(list1)
                        # print("came to this")
                    list1 = []
                    if (x >= 0) and (x < row) and (y + 1 >= 0) and (y + 1 < column) and (
                            flag[x][y + 1] == False):  # and (wall[x][y + 1] == False) and (
                        # tstates[x][y + 1][0] == False) and (flag[x][y+1]==False):
                        # print("Enters4")
                        flag[x][y + 1] = True
                        newvalue, direction = utility(x, y + 1)
                        if value[x][y + 1] != newvalue:
                            gamma = gamma + abs(value[x][y + 1] - newvalue)
                            value[x][y + 1] = newvalue
                            # value[x][y+1]+=rate*(newvalue-value[x][y+1])
                            policy[x][y + 1] = direction
                        else:
                            #a = diff(policy[x][y + 1], direction)
                            # if (a < 0):
                            policy[x][y + 1] = direction
                        list1.append(x)
                        list1.append(y + 1)
                        # if list1 not in traverse:
                        traverse.append(list1)

                else:
                    list1 = []
                    if (x + 1 >= 0) and (x + 1 < row) and (y >= 0) and (y < column) and (
                            flag[x + 1][y] == False):
                        flag[x + 1][y] = True
                        newvalue, direction = utility(x + 1, y)
                        if value[x + 1][y] != newvalue:
                            gamma = gamma + abs(value[x + 1][y] - newvalue)
                            value[x + 1][y] = newvalue
                            # value[x + 1][y] += rate * (newvalue - value[x + 1][y])
                            policy[x + 1][y] = direction
                        else:
                            #a = diff(policy[x + 1][y], direction)
                            # if (a < 0):
                            policy[x + 1][y] = direction
                        list1.append(x + 1)
                        list1.append(y)
                        # if list1 not in traverse:
                        traverse.append(list1)

                    list1 = []
                    if (x - 1 >= 0) and (x - 1 < row) and (y >= 0) and (y < column) and (
                            flag[x - 1][y] == False):  # and (wall[x - 1][y] == False) and (
                        # tstates[x - 1][y][0] == False) and (flag[x-1][y]==False):
                        # print("Entered")
                        # print("Enters2")
                        flag[x - 1][y] = True
                        newvalue, direction = utility(x - 1, y)
                        if value[x - 1][y] != newvalue:
                            gamma = gamma + abs(value[x - 1][y] - newvalue)
                            value[x - 1][y] = newvalue
                            # value[x - 1][y] += rate * (newvalue - value[x - 1][y])
                            policy[x - 1][y] = direction
                        else:
                            #a = diff(policy[x - 1][y], direction)
                            # if (a < 0):
                            policy[x - 1][y] = direction
                        list1.append(x - 1)
                        list1.append(y)
                        # if list1 not in traverse:
                        traverse.append(list1)
                    # print("this is=", x - 1,row, y, wall[x - 1][y], tstates[x - 1][y][0], len(traverse))

                    list1 = []
                    if (x >= 0) and (x < row) and (y - 1 >= 0) and (y - 1 < column) and (
                            flag[x][y - 1] == False):  # and (wall[x][y - 1] == False) and (
                        # tstates[x][y - 1][0] == False) and (flag[x][y-1]==False):
                        # print("Enters3")
                        newvalue, direction = utility(x, y - 1)
                        flag[x][y - 1] = True
                        if value[x][y - 1] != newvalue:
                            gamma = gamma + abs(value[x][y - 1] - newvalue)
                            value[x][y - 1] = newvalue
                            # value[x][y - 1] += rate * (newvalue - value[x][y - 1])
                            policy[x][y - 1] = direction
                        else:
                            #a = diff(policy[x][y - 1], direction)
                            # if (a < 0):
                            policy[x][y - 1] = direction
                        list1.append(x)
                        list1.append(y - 1)
                        # if list1 not in traverse:
                        traverse.append(list1)
                        # print("came to this")
                    list1 = []
                    if (x >= 0) and (x < row) and (y + 1 >= 0) and (y + 1 < column) and (
                            flag[x][y + 1] == False):  # and (wall[x][y + 1] == False) and (
                        # tstates[x][y + 1][0] == False) and (flag[x][y+1]==False):
                        # print("Enters4")
                        flag[x][y + 1] = True
                        newvalue, direction = utility(x, y + 1)
                        if value[x][y + 1] != newvalue:
                            gamma = gamma + abs(value[x][y + 1] - newvalue)
                            value[x][y + 1] = newvalue
                            # value[x][y + 1] += rate * (newvalue - value[x][y + 1])
                            policy[x][y + 1] = direction
                        else:
                            a = diff(policy[x][y + 1], direction)
                            # if (a < 0):
                            policy[x][y + 1] = direction
                        list1.append(x)
                        list1.append(y + 1)
                        # if list1 not in traverse:
                        traverse.append(list1)

outputfile = open("output.txt", "w")
for i in range(row - 1, -1, -1):
    for j in range(0, len(policy[i])):
        if j == len(policy[i]) - 1:
            if i != 0:
                outputfile.write(policy[i][j] + "\n")
            else:
                outputfile.write(policy[i][j] + "\n")
        else:
            outputfile.write(policy[i][j] + ",")
    # print(value[i])
