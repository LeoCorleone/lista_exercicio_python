# Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos 
# os números de 1 até ao número digitado. Por exemplo, se o usuário digitar o número 4, a 
# saída deve ser 10 (1+2+3+4=10).
num = int(input("Digite um número qualquer: "))
num = num + 1
soma = 0
for ix in range(1, num):
    soma = soma+ ix
    print(soma)
