print("====================================")
print("ACESSO AO CINEMA")
print("====================================")

idade = int(input("digite sua idade:"))
carteirinha = int(input("voce tem carteirinha de estudante? (s/n):"))

if idade > 18 and carteirinha == "s":
   print("Entrada com meia-entrada permitida")
else:
    print("Entrada permitida somente com ingresso inteiro")

print("====================================")