number = []

while len(number) < 3:
    num = int(input(f'Number {len(number) + 1}:'))

    if num in number:
        print('Type diferent numbers!')
    else:
        number.append(num)

a,b,c = number[0],number[1],number[2]

if a > b and b > c:
    print(a, b, c)
elif a > c and c > b:
    print(a, c, b)
elif b > a and a > c:
    print(b, a, c)
elif b > c and c > a:
    print(b, c, a)
elif c > a and a > b:
    print(c, a, b)
else:
    print(c, b, a)