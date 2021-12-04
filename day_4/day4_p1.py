#!/usr/bin/python3.8

################
# Day 4
################

# Read in the file
with open("day3_p1_input.txt", "r") as f:
    filename = f.readlines()

values = [x.strip() for x in filename]

# Determine the gamma and epislon
def calc_gamma_epsilon(valueList):
    numValues = len(valueList[0])
    gamma = [0] * numValues 
    epsilon = [0] * numValues 
    for j in valueList:
        print(j)
        for i,x in enumerate(j):
            #print(x,j)
            if x == '1':
                gamma[i] += 1 
                epsilon[i] += 0
                #jprint('1')
            elif x == '0':
                gamma[i] += 0 
                epsilon[i] += 1
                #print('0')

    fin_gamma = ''
    fin_epsilon = ''
    for x,j in enumerate(gamma):
        if epsilon[x] < j:
            fin_gamma += '1' 
            fin_epsilon += '0' 
        else:
            fin_gamma += '0' 
            fin_epsilon += '1' 

    print(int(''.join(map(str,fin_gamma)), 2) * int(''.join(map(str,fin_epsilon)),2))

# Determine the c02 and o2 
def calc_co2_o2(valueList):
    numValues = len(valueList[0])
    end_gamma = list(valueList)
    end_epsilon = list(valueList)

    for i in range(numValues):
        if len(end_gamma) > 1:
            a0 = len([x for x in end_gamma if x[i] =='0'])
            a1 = len([x for x in end_gamma if x[i] =='1'])
            if a1 >= a0:
                end_gamma = [x for x in end_gamma if x[i]=='1']
            else:
                end_gamma = [x for x in end_gamma if x[i]=='0']

        if len(end_epsilon) > 1:
            a0 = len([x for x in end_epsilon if x[i] =='0'])
            a1 = len([x for x in end_epsilon if x[i] =='1'])
            if a1 >= a0:
                end_epsilon = [x for x in end_epsilon if x[i]=='0']
            else:
                end_epsilon = [x for x in end_epsilon if x[i]=='1']

    print(int(''.join(map(str,end_gamma)), 2) * int(''.join(map(str,end_epsilon)),2))

# Generate Answers
#calc_co2_o2(values)
