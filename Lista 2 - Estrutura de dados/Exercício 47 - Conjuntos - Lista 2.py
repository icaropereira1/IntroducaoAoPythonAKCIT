conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = { 6, 7, 8}

if conjunto1&conjunto2 == set():
    print("Os conjuntos não têm elementos em comum.")

else:
    print("Os conjuntos têm elementos em comum.")
    print("Elementos em comum:", conjunto1&conjunto2)