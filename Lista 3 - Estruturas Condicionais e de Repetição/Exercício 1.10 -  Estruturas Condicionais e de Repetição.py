a= float(input("Type the value of 'a' "))
b= float(input("Type the value of 'b' "))
c= float(input("Type the value of 'c' "))

lista = [a,b,c]

while True:
    i = int(input('Choose if i will receive 1 or 2 or 3: '))

    if( i in [1,2,3]):
        break
    else:
        print('Choose between 1 or 2 or 3!')

if i == 1:
    lista.sort()
    print(lista)

elif i == 2:
    lista.sort(reverse = True)
    print(lista)

else:
    if(a >= b) and (a >= c):
        print(b,a,c)
    if(b >= a) and (b >= c):
        print(a,b,c)
    if(c >= b) and (c >= a):
        print(b,c,a)