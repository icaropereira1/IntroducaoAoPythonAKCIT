height = float(input('Type the height of the person:'))

while True:
    number = int(input('Type 1 if male, 2 if female: '))

    if number != 1 and number != 2:
        print('Type a valid number!')
    else:
        break

if number == 1:
    print('Your ideal weight its: ',(72.7*height)-58)   
if number == 2:
    print('Your ideal weight its: ',(62.1*height)-44.7)   