conjunto = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 1,2,3,4,5}
conjunto = list(conjunto)

for i in range(len(conjunto)):
    if conjunto[i] > 10:
        print(conjunto[i])