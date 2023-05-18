# Todos os números entre 5 e 100 que são divisíveis por 7 e não são múltimos de 5

for ix in range(5, 101, 1):
    if ix % 7 == 0 and ix % 5 != 0:
        print(ix)