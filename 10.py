# Faça um programa em linguagem Python, que lê um número n e imprime os n primeiros 
# números da sequência de Fibonacci.

num = int(input("Digite um número inteiro qualquer: "))
res = 0
f1 = 1
f2 = 0
num = num + 1
for ix in range(1, num):
    res = f1 + f2
    print(res)
    f1 = f2
    f2 = res
