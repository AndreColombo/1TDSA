i = 1
if i > 0:
    print("dentro do if")  # dentro do if

while i <= 10:
    print("dentro do while")  # dentro do while... (infinitas vezes)

i = 1
while i <= 10:
    print("dentro do while")
    i += 1  # dentro do while... (10 vezes)

while i <= 10:
    print(f"i: {i}")
    i += 1  # erro pois i=11 (comando anterior)

i = 1
while i <= 10:
    print(f"i: {i}")
    i += 1

i = 1
while i <= 100:
    print(f"i: {i}")
    i += 1  # dentro do while... (10 vezes)
