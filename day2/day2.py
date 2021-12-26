#!/usr/bin/python3

file = open("input_day2.txt", "r")

data = file.readlines()
cleanData = []
splitData = []

for item in data:
    cleanItem = item.strip()
    cleanData.append(item.split())

def part1():
    forward_amount = []
    up_amount = []
    down_amount = []
    
    for direction,amount in cleanData:
        if direction == 'forward':
            forward_amount.append(int(amount))
        elif direction == 'up':
            up_amount.append(int(amount))
        elif direction == 'down':
            down_amount.append(int(amount))

    distance = sum(forward_amount)
    depth = sum(down_amount) - sum(up_amount)

    return(distance,depth)

def part2():
    forward_aim_list = []
    aim_amount_list = []

    for direction,amount in cleanData:
        if direction == 'down':
            aim_amount_list.append(int(amount))
        elif direction == 'up':
            aim_amount_list.append(-(int(amount)))
        elif direction == 'forward':
            forward_aim_list.append((int(amount),sum(aim_amount_list)))

    print(forward_aim_list)
    distance = sum(i[0] for i in forward_aim_list)
    depth = sum(i*j for i,j in forward_aim_list)

    return(distance,depth)

print('The submarine will end up at the following distance,depth: ',part1())
print('According to the new instructions, our distance,depth pair is: ',part2())
