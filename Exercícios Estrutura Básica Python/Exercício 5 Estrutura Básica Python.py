name = input('Whats the name of the seller? ')
base_salary= float(input('Whats his salary? '))
how_much_sell= float(input('How much '+name+' sell?' ))

comission = 0.15 * how_much_sell

salary = comission + base_salary

percentage_received = salary * 100 / base_salary



print('Name: '+name+'\nSalary:',salary,'\nPercentage received in excess by comission:',percentage_received)