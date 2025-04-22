weight = float(input('Weight:'))
height = float(input('Height:'))

if (70  <= weight <= 80) and (1.75 <= height) and (height <= 1.90):
    print('Accepted')

elif(70  <= weight) and (weight <= 80) and (1.75 > height) or (height > 1.95):
    print('Recused by height')

elif(70  > weight) or (weight > 80) and (1.75 <= height <= 1.90):
    print('Recused by weight')

elif(70  > weight) or (weight > 80) and (1.75 > height) or (height > 1.95):
    print('Recused by height and weight')