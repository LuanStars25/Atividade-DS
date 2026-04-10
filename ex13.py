#ex13 - DS1SUB - sisteminha de nota

nota = float(input("Digite a nota: "))

if nota >= 18:
    print("Aprovadoooo!")
elif nota >= 8 and nota < 17:
    print("Ficou na RCP")
else:
    print("Reprovouuu")