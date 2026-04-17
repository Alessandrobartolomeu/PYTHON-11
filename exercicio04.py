print("========================================")
print("PROMOÇÃO - FRETE GRÁTIS")
print("========================================")

valor = float(input("Digite o valor da compra (R$): "))
vip = input("Cliente VIP? (s/n): ").lower()

if valor > 100 or vip == "s":
    print("Você ganhou frete grátis!")
else:
    print("Frete será cobrado.")

print("========================================")
