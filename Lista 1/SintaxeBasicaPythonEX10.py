product1 = float(input('Type the value of first product: '))
product2 = float(input('Type the value of second product: '))
product3 = float(input('Type the value of third product: '))

total = product1 + product2 + product3

print('Total:', total)

discount = total*0.9

apply_discount = int(input('Do you want do apply a discount of 10%? Type 1 for yes, 2 for no\n'))

while apply_discount != 1 and apply_discount != 2:
    print('Type 1 for yes, 2 for no\n')
    apply_discount = int(input())
    
if(apply_discount == 1):
    print(discount)
