students = dict()
grades_sum = 0 
i = 0

print("Adicionando alunos e notas\nPara sair digite 'sair'")

while True:
    
    name = input('Digite o nome do aluno: ')
    
    if(name == 'sair'):
        break

    grade = float(input(f'Digite o nota d@ {name} : '))
    grades_sum += grade
    i = i+1
    students[f'{name}'] = grade

average = grades_sum / i

print('Media geral:',average)