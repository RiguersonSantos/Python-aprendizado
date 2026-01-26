dinheiro = float(input('Qual valor disponivel para transação você possui? R$'))
dolar = float(5.28)

soma = dinheiro / dolar

print("A quantidade de dolares disponiveis para você comprar é de ${:.2f}".format(soma))