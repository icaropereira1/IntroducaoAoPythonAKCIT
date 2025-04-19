tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = (1,2,3,4,6,7,8,9,10)

for i in range(len(tuple1)):
    if tuple1[i] == 5:
        print('The number 5 is in the tuple1')
    else:
        continue


for i in range(len(tuple2)):
    if tuple2[i] == 5:
        print('The number 5 is in the tuple2')
    else:
        continue
