print("Exemplo com if-elif-else")
print("------------------------")

final_placa = int(input("Número: "))
if final_placa == 1 or final_placa == 2:
    print("Segunda-Feira")
elif final_placa == 3 or final_placa == 4:
    print("Terça-Feira")
elif final_placa == 5 or final_placa == 6:
    print("Quarta-Feira")
elif final_placa == 7 or final_placa == 8:
    print("Quinta-Feira")
elif final_placa == 9 or final_placa == 0:
    print("Sexta-Feira")
else:
    print("Número inválido!")

print("Exemplo com match-case")
print("------------------------")

final_placa = int(input("Número: "))
match final_placa:
    case 1 | 2:
        print("Segunda-Feira")
    case 3 | 4:
        print("Terça-Feira")
    case 5 | 6:
        print("Quarta-Feira")
    case 7 | 8:
        print("Quinta-Feira")
    case 9 | 0:
        print("Sexta-Feira")
    case _:
        print("Número inválido!")
