nome_produto = input("Digite o nome do produto: ")
valor_produto = float( input("Digite o valor do produto: %"))
desconto = float(input("Digite o desconto: "))
valor_desconto = valor_produto * desconto / 100
valor_final = valor_produto - valor_desconto

print("-------------------------------")
print(f"Produto: {nome_produto}\nPreço final: {valor_final}")
print("-------------------------------")