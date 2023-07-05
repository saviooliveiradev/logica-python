gratuido = False
preço = 150.00


nome = str(input("Qual é seu nome: "))
preço_barato = float(input("Digite um preço adequado para você:R$"))
preço_razoavel = float(input("E um preço razoável:R$"))

print(f"Olá, {nome},")

if gratuido:
    print("Obaa! Quero aprender agora!")

elif preço <= preço_barato:
    print("Quero comprar!")

elif preço_razoavel < preço_razoavel:
    print("Deixa eu pensar uns 5 minutinhos")

else:
    print("Quem sabe no futuro, agora não posso")

