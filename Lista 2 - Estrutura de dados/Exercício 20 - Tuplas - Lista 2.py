tuple = ('Hello', 'World', '!')
string = ''

# Poderia usar o .join string = ' - '.join(tupla)

for i in range (len(tuple)):
    string = string + tuple[i] 
print (string)

for i in range (len(tuple)):
    string = ' '.join(tuple)
print (string)
