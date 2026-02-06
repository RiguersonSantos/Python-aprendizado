import math;

angulo = float(input("Fale um ângulo qualquer: "));

rad = math.radians(angulo);

print(f"{math.sin(rad):.2f}");
print(f"{math.cos(rad):.2f}");
print(f"{math.tan(rad):.2f}")