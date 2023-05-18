# Definir se um número é negativo, positivo ou netro 
num = int(input("Digite um número inteiro qualquer: "))
if num > 0:
    print("O número {} é positivo".format(num))
elif num == 0:
    print("O número {} é neutro".format(num))
else :
    print("O número {} é negativo".format(num))
