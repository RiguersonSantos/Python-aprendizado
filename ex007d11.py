dias = int(input("DIga quantos dias você alugou o veiculo: "));
km = float(input("Diga quantos kms você rodou com o veiculo: "));

aluguel = dias * 60;
rodado = km * 0.15;
valorFinal= aluguel + rodado;

print("Alugando por {0:.0f} dias, deu R${1:.2f} e rodando {2:.2f} kms que deu R${3:.2f}, com o veiculo, o valor final fica em: \n" \
     " R${4:.2f}".format(dias, aluguel, km, rodado, valorFinal ))