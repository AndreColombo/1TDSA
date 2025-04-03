i = int(input("Início: "))
f = int(input("Fim: "))

if i < f:
    while i < f:
        if i % 2 == 0:
            print(f"i: {i}")
        i += 1
elif i > f:
    while i > f:
        if i % 2 != 0:
            print(f"i: {i}")
        i -= 1
else:
    print(f"Os valores são iguais! - i: {i} | f: {f}")
