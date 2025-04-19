numbers = []
print("Type numbers to be add to a list, if you want to stop, type 0")
while True:
    number = int(input("Number: "))
    if(number == 0):
        break
    else:
        numbers.append(number)

print(numbers)