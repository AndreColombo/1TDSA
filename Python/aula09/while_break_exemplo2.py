# comando break

i = 1
while i <= 100:
    print(f"i: {i}")
    if i == 35:
        print("=> Bingo! <=")
        break
    i += 1
print("FORA DO WHILE")
