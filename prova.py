def numerazione_lista(lista):
    counter = 0
    for item in lista:
        counter = counter + 1
        print("la lunghezza della", counter, "parola e':", len(item))
    

lista_input = ["ciao", "prova", "antonio"]

numerazione_lista(lista_input)

