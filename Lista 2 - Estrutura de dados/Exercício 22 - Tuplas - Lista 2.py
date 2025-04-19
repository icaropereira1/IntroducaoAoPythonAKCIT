numbers = (1,2,3,4,5,6,7,8,9,10)
odds= []

for i in range(len(numbers)):
    if (numbers[i] % 2 != 0):
        odds.append(numbers[i])
        
    else:
        continue

print(odds)