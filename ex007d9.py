salario = float(input("DIga-me o seu salário em reais: R$"));
acrescimo = (15 / 100) * salario;

novoSalario = salario + acrescimo;

print("O seu antigo salário no valor de R${0:.2f} recebeu um acréscimo de R${1:.2f} e passou a ser de R${2:.2f}".format(salario, acrescimo, novoSalario))

