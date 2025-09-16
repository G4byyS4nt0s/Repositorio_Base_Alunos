nome = input ("digite o nome do aluno")
nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))

media = (nota1 + nota2 + nota3) / 3

if media  >= 7:
   print("APROVADO")

elif media  >= 4:
   print("RECUPERAÇÃO")

else: 
   print("REPROVADO")

print(f"A media do aluno {nome} é {media:.1f}")