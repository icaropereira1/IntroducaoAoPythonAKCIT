tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

media = 0

for i in range(len(tuple)):
    media = media + tuple[i]

media = media / len(tuple)
print(media)

