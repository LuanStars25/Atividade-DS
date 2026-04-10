#15 - Sistema de desconto

valor = float(input("Valor da compra: "))

if valor >= 200:
    print("Desconto de 20%")
elif valor >= 100:
    print("Desconto de 10%")
else:
    print("Sem desconto")