produto = float(input("Digite o valor do produto em reais: R$"));
desconto = (5 / 100) * produto;
novoValor = produto - desconto;

print("O produto com valor de R${0:.2f}, ficou por R${1:.2f} com o desconto de R${2:.2f}".format(produto, novoValor, desconto))