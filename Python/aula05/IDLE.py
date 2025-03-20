3 == 3   # True
3 != 3   # False
3 > 5   # False
5 > 3   # True
5 > 5   # False
5 >= 5   # True
var = 5   # False
var   # 5
if var == 5:
    print("os números são iguais")   # os números são iguais

if var != 5:
    print("os números são diferentes")
    print("dentro do if")

if var != 7:
    print("os números são diferentes")   # os números são diferentes
    print("dentro do if")   # dentro do if

if var > 2:
    print("o valor de var é maior do que 2")   # o valor de var é maior do que 2


True and True   # True
True or False   # True
True and False   # False
True or True   # True
not True   # False
not False   # True
a = 5
b = 10

(a > 3) and (b < 15)   # True
(a > 6) and (b < 15)   # False
not ((a > 3) and (b < 15))   # False
if (a > 3) and (b < 15):
    print("passou no teste")   # passou no teste

if (a > 6) and (b < 15):
    print("passou no teste")
else:
    print("não passou no teste")   # não passou no teste
