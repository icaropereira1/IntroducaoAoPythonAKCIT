days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
day = input('Enter a day of the week: ')

for i in range(len(days)):
    if (day == days[i]):
        print (f'{days[i]} is in the tuple')


       