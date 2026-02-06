from math import hypot;


comp_catetoOp = float(input("Digite o comprimento do cateto Oposto: cm"));
comp_catetoAdja = float(input("Digite o comprimento do cateto adjascente: cm"));

hipotenusa = hypot(comp_catetoOp, comp_catetoAdja);

print("O comprimento da hipotenusa fica em {0:.2f}".format(hipotenusa))