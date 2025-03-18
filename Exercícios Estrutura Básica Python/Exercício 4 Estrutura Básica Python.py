product_value = float(input('How much this costs? '))
percentage_profit =  float(input('How much % will it profit? '))

sale_value = product_value*(1+percentage_profit/100)

print('The sale value to profit',percentage_profit,'% is', sale_value)