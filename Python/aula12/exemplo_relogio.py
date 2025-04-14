import time

ha = int(input("Digite a hora do alarme: "))
ma = int(input("Digite o minuto do alarme: "))
sa = int(input("Digite o segundo do alarme: "))

h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print(f"{h}:{m}:{s}")
            time.sleep(1)
            if h == ha and m == ma and s == sa:
                print("ALARME!")
                break
            s += 1
        if h == ha and m == ma:
            break
        m += 1
    if h == ha:
        break
    h += 1
