people = [
    {'name':'Ícaro','age':20},
    {'name':'Anna','age':20},
    {'name':'Sônia','age':49},
    {'name':'Brenda','age':25},
    {'name':'Malu','age':12}
]
ages = 0    

for i in people:
    ages += i['age']

print(f'A soma das idades é {ages}')

