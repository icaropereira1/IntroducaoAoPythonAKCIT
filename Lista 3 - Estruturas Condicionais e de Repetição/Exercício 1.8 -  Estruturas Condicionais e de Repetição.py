weight = float(input('Weight: '))
height = float(input('Height: '))

# for those who is lower than 1.20m
if (height < 1.20):
    if(weight < 60):
        print('A')
    elif(weight >= 60) and (weight < 90):
        print('D')
    elif(weight > 90):
        print('G')
# for those who is between 1.20 and 1.70
if (height >= 1.20) and (height < 1.70):
    if(weight < 60):
        print('B')
    elif(weight >= 60) and (weight < 90):
        print('E')
    elif(weight > 90):
        print('H')

# for those who is higher than 1.70
if (height > 1.70):
    if(weight < 60):
        print('C')
    elif(weight >= 60) and (weight < 90):
        print('F')
    elif(weight > 90):
        print('I')