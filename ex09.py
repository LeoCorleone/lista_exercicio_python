# Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o 
# resultado.
# Por exemplo, se o número é 2021 , então a saída deve ser 4.

num = input("Digite um número inteiro qualquer: ")
ix = 0
while ix < len(num):
    ix = ix + 1
print("O numéro {} tem {} caractéres.".format(num, ix))