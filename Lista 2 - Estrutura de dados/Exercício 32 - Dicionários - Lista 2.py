student = {'name':'Ícaro', 'age':20, 'course': 'Engenharia de computação','grade':10}

print(student)


student_keys = list(student.keys())

if 'age' in student_keys:
    print('A chave age existe.')
else:
    print('A chave age não existe.')