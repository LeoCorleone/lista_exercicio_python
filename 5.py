#Descobrir o reajuste salarial.
# < 500 = 15%
# < 1000 = 10%
# >= 1000 = 5%

sal = float(input("Digite o valor do seu salário: R$"))
if sal < 500:
    salN = (sal * 0.15) + sal
elif sal < 1000:
    salN = (sal * 0.10) + sal
else:
    salN = (sal * 0.05) + sal
print("Seu novo salário é: RR${}".format(salN))

