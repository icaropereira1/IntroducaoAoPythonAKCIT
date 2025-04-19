people = [
    {'name':'Ícaro','age':20},
    {'name':'Anna','age':20},
    {'name':'Sônia','age':49},
    {'name':'Brenda','age':25},
    {'name':'Malu','age':12}
]

name = input("Type the name of the person: ")
# Procura na lista
for person in people:
    if person['name'] == name:
        print(f"{name} tem {person['age']} anos")
        break
else:
    print(f"{name} não foi encontrada na lista.")

