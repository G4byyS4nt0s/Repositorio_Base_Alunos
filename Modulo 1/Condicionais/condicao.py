nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade"))
carteira = input("Possui carteira? (1-Sim | 2-Não)")

if idade >=18:
    print("Maior de idade")
    if carteira =="1":
        print("Pode dirigir ✅")
    else:
         print("Não pode dirigir ❌")
else:
    print("Menor de idade")