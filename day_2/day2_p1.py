#!/usr/bin/python3.8

################
# Day 2
################

# Read in the file
with open("day2_p1_input.txt", "r") as f:
    filename = f.readlines()

values = [x.split() for x in filename]

# Return value of depth, horizontal in easy way 
def total_movement(valueList):
    depth, horizontal = 0, 0
    for i in values:
        if i[0] == "forward":
            horizontal += int(i[1]) 
            continue
        if i[0] == "down":
            depth += int(i[1])
            continue
        if i[0] == "up":
            depth -= int(i[1])
            continue
    return depth, horizontal

# Return value of depth, horizontal in complex way
def total_movement_aim(valueList):
    depth, horizontal, aim = 0, 0, 0        
    for i in values:    
        if i[0] == "forward":
            horizontal += int(i[1]) 
            depth += aim*int(i[1])
            continue
        if i[0] == "down":
            aim += int(i[1]) 
            continue
        if i[0] == "up":
            aim -= int(i[1]) 
            continue
    return depth, horizontal

# Generate Answers
print(total_movement_aim(values))
total_move = total_movement_aim(values)
print(total_move[0]* total_move[1])
