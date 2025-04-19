students = {
    'Brenda': 25,
    'Ícaro': 20,
    'Anna': 22,
    'Sônia': 28,
    'Malu': 18
}

# Ordenando por chave (nome)
for nome in sorted(students.keys()):
    print(f'{nome}: {students[nome]}')
