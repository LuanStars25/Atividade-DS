#ex 17 - Login simples
usuario = input("Usuário: ")
senha = input("Sistema: ")
if usuario == "admin" and senha == "123": 
    print("Login realizado")
else:
    print("Usuário ou senha incorretos")