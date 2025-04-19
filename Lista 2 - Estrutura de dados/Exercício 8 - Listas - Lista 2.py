numbers = [1,2,3,4,5,6,7,8,9,10,5,6,7,8,9,10]
numbers_non_repeated = []

for number in numbers:
    if(number not in numbers_non_repeated):
        numbers_non_repeated.append(number)

print(numbers_non_repeated)