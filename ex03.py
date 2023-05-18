#tabuada de 1 a 10

valor = int(input("Digite um valor para a tabuada: "))
for ix in range(1, 11, 1):
    calc = valor * ix
    print("{} x {} = {}".format(valor, ix, calc))