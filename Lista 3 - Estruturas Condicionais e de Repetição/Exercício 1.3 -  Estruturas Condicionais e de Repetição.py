grade1 = float(input('Type the first grade of the student: '))
grade2 = float(input('Type the second grade of the student: '))

average = (grade1 + grade2)/2

if average >= 6.0:
    print('Student approved')

else:
    print('Student reproved')