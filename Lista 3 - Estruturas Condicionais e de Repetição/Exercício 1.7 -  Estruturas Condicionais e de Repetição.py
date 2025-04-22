apples = float(input("Type how much apple in kilograms: "))
strawberry = float(input("Type how much strawberry in kilograms: "))

weight = apples + strawberry

if (strawberry > 5) and (apples > 5):
    price = 4 * strawberry + apples * 2
    
elif(strawberry <= 5) and (apples > 5):
    price = 5 * strawberry + apples * 2
    
elif(strawberry <= 5) and (apples <= 5):
    price = 5 * strawberry + apples * 3 

elif(strawberry > 5) and (apples <= 5):
    price = 4 * strawberry + apples * 3      
    

if(price > 35 or weight > 8):
    final_price = 0.8*price
    print('The total is: R$',final_price)

else:
    print('The total is: R$',price)



