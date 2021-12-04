#!/usr/bin/python3.8

################
# Day 1
################

# Read in the file
with open("day1_p1_input.txt", "r") as f:
    file = f.readlines()

values = [int(x) for x in file]

# Create array for window values
def slidingWindow(valuesArray, window):
    windowedArray = []
    for i in range(window-1, len(values)):
        total = 0
        for j in range(window):
            total += values[i-j]    
        windowedArray.append(total)     
    return windowedArray
        
# Sum window values
def sumWindow(valuesArray):
    numValues = 0
    # Parse the file
    for i in range(len(valuesArray)):
        if i > 0:
            if valuesArray[i] > valuesArray[i-1]:       
                numValues += 1
    return numValues

# Generate Answers
print(slidingWindow(values, 3))
result = slidingWindow(values, 3)
print(sumWindow(result))
