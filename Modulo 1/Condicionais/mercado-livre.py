import time

print("--------------------------")
print("***🚚 MERCADO LIVRE 🚚***")
print("--------------------------")

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

print("Carregando......")

time.sleep(3)

if usuario == "gabyy" and senha == "1234":
    print("✅ Login bem-sucedido!!! ✅")
    print(f"Bem vindo {usuario}")
else:
    print("❌ USUÁRIO OU SENHA INCORRETO ❌")