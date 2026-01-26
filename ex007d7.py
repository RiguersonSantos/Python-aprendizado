largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
tinta = 1 / 2

tintaNecess = tinta * area

print("A area em metros quadrados é de {:.2f} e a tinta necessária é de {:.1f} litros".format(area, tintaNecess))