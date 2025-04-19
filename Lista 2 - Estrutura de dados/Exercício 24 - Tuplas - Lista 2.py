numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 2, 3, 4, 5, 6)
times = 0 

number = int(input('Type a number: '))

for i in range(len(numbers)):
   if(number == numbers[i]):
        times = times + 1
    

print('The number {} appears {} times in the tuple'.format(number, times))
