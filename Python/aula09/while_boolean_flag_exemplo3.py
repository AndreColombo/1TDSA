executa = input("Executa? (sim ou não) \n: ")
cont = 0

while executa == "sim":  # var executa -> controladora do while
    cont += 1  # var cont -> contadora/acumuladora
    executa = input("Executa novamente? (sim ou não) \n: ")

print(f"O bloco while executou {cont} vezes!")
