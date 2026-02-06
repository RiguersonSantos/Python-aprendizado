from math import trunc, floor;


nReal = float(input("Digite um numero real para saber a parte inteira: "));

nInt = trunc(nReal);

print("A parte inteira do numero {0} é {1}".format(nReal, nInt))