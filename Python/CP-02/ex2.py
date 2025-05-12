carros = []
consumos = []
litros = []
custos = []
i = 0

while i < 5:
    i += 1
    print(f"Veículo {i}")
    carro = input("Nome: ")
    carros.append(carro)
    consumo = float(input("Km por litro: "))
    consumos.append(consumo)
    litro = 1000 / consumo
    litros.append(litro)
    custo = litro * 6.89
    custos.append(custo)

print("\nRelatório Final:")
print(
    f"1 - {carros[0]} - {consumos[0]:.1f} - {litros[0]:.1f} litros - R$ {custos[0]:.2f}"
)
print(
    f"2 - {carros[1]} - {consumos[1]:.1f} - {litros[1]:.1f} litros - R$ {custos[1]:.2f}"
)
print(
    f"3 - {carros[2]} - {consumos[2]:.1f} - {litros[2]:.1f} litros - R$ {custos[2]:.2f}"
)
print(
    f"4 - {carros[3]} - {consumos[3]:.1f} - {litros[3]:.1f} litros - R$ {custos[3]:.2f}"
)
print(
    f"5 - {carros[4]} - {consumos[4]:.1f} - {litros[4]:.1f} litros - R$ {custos[4]:.2f}"
)

if (
    consumos[0] > consumos[1]
    and consumos[0] > consumos[2]
    and consumos[0] > consumos[3]
    and consumos[0] > consumos[4]
):
    menor = carros[0]
elif (
    consumos[1] > consumos[0]
    and consumos[1] > consumos[2]
    and consumos[1] > consumos[3]
    and consumos[1] > consumos[4]
):
    menor = carros[1]
elif (
    consumos[2] > consumos[0]
    and consumos[2] > consumos[1]
    and consumos[2] > consumos[3]
    and consumos[2] > consumos[4]
):
    menor = carros[2]
elif (
    consumos[3] > consumos[0]
    and consumos[3] > consumos[1]
    and consumos[3] > consumos[2]
    and consumos[3] > consumos[4]
):
    menor = carros[3]
else:
    menor = carros[4]

print(f"O menor consumo é o do {menor}")
