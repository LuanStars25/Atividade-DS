n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

match (n1, n2):
    case (a, b) if a > b:
        print("O 1° número é maior")
    case (a, b) if a < b:
        print("O 2° número é maior")
    case _:
        print("Os dois números são iguais")