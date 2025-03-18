name = input('Whats the name of the student? ')

grade1 = float(input('Whats the grade of the first bimonthly?'))
grade2 = float(input('Whats the grade of the second bimonthly?'))
grade3 = float(input('Whats the grade of the third bimonthly?'))
grade4 = float(input('Whats the grade of the fourth bimonthly?'))

average_grade_year = (grade1+grade2+grade3+grade4)/4
average_grade_first_semester = (grade1+grade2)/2
average_grade_second_semester = (grade3+grade4)/2

print('Student: ', name,'\nAverage grade year: ', average_grade_year,'\nAverage grade first semester:',average_grade_first_semester,'\nAverage grade second semester: ', average_grade_second_semester)