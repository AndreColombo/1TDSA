seq = 10
seq   # 10
type(seq)   # <class 'int'>
seq = [3.1, 7.8, 1.0, 10.0, 9.5]
seq   # [3.1, 7.8, 1.0, 10.0, 9.5]
type(seq)   # <class 'list'>
seq[0]   # 3.1
seq[1]   # 7.8
seq[2]   # 1.0
len(seq)   # 5
seq[5]   # Traceback (most recent call last):
         #   File "<pyshell#10>", line 1, in <module>
         #     seq[5]
         # IndexError: list index out of range
seq[1] = 6.0
seq   # [3.1, 6.0, 1.0, 10.0, 9.5]
i = 0
while i <= 4:
    print(seq[i])
    i += 1
# 3.1
# 6.0
# 1.0
# 10.0
# 9.5 
   
i = 0
while i <= 4:
    if seq[i] > 8:
        print(seq[i])
    i += 1
# 10.0
# 9.5
   
seq = 6.0
seq   # 6.0
type(seq)   # <class 'float'>


'''
String
 - sequência homogênea e imutável
 - cadeia de char
 - construtor str()
 - criação através de aspas ''
'''
   # "\nString\n - sequência homogênea e imutável\n - cadeia de char\n - construtor str()\n - criação através de aspas ''\n"
ling = 'Linguagem Python'
ling   # 'Linguagem Python'
texto = str()
type(texto)   # <class 'str'>
texto = ''
texto   # ''
texto = 'Linguagem Python'
texto   # 'Linguagem Python'
len(texto)   # 16
texto[0]   # 'L'
texto[1]   # 'i'
texto[2]   # 'n'
texto[16]   # Traceback (most recent call last):
            #   File "<pyshell#50>", line 1, in <module>
            #     texto[16]
            # IndexError: string index out of range
texto[0] = 'X'   # Traceback (most recent call last):
                 #   File "<pyshell#51>", line 1, in <module>
                 #     texto[0] = 'X'
                 # TypeError: 'str' object does not support item assignment


'''
Listas
 - sequência heterogênea e mutável
 - construtor list()
 - criação pode ocorrer com colchetes []
'''
   # '\nListas\n - sequência heterogênea e mutável\n - construtor list()\n - criação pode ocorrer com colchetes []\n'
lista = list()
type(lista)   # <class 'list'>
lista = []
lista   # []
lista = [3, True, 3.14, 'Python']
lista   # [3, True, 3.14, 'Python']
len(lista)   # 4
lista[2] = 3.16
lista   # [3, True, 3.16, 'Python']
lista[0] = 20
lista   # [20, True, 3.16, 'Python']
lista[3] = 'Java'
lista   # [20, True, 3.16, 'Java']
type(lista)   # <class 'list'>


'''
Tupla
 - sequência heterogênea e imutável
 - construtor tuple()
 - pode ser criada com parênteses - ()
'''
   # '\nTupla\n - sequência heterogênea e imutável\n - construtor tuple()\n - pode ser criada com parênteses - ()\n'
tupla = tuple()
tupla   # ()
type(tupla)   # <class 'tuple'>
tupla = ()
tupla   # ()
tupla = (123)
tupla   # 123
type(tupla)   # <class 'int'>
tupla = (123, )
tupla   # (123,)
type(tupla)   # <class 'tuple'>
tupla = (3, True, 3.14, 'Python')
tupla   # (3, True, 3.14, 'Python')
len(tupla)   # 4
tupla[1]   # True
tupla[3]   # 'Python'

i=0
while i<len(tupla):
    print(tupla[i])
    i+=1
   # 3
   # True
   # 3.14
   # Python

i=0
while i < len(lista):
    print(lista[i])
    i+=1
   # 20
   # True
   # 3.16
   # Java

i=0
while i<len(texto):
    print(texto[i])
    i+=1
   # L
   # i
   # n
   # g
   # u
   # a
   # g
   # e
   # m
   #  
   # P
   # y
   # t
   # h
   # o
   # n

tupla   # (3, True, 3.14, 'Python')
tupla[1] = False   # Traceback (most recent call last):
                   #   File "<pyshell#119>", line 1, in <module>
                   #     tupla[1] = False
                   # TypeError: 'tuple' object does not support item assignment


'''
Intervalo
 - sequência numérica homogênea e imutável
 - construtor range()

 - três parâmetros - range(inicio, fim, passo)
 - dois parâmetros - range(inicio, fim) - passo será de 1 em 1
 - um parâmetro - range(fim)
'''
   # '\nIntervalo\n - sequência numérica homogênea e imutável\n - construtor range()\n\n - três parâmetros - range(inicio, fim, passo)\n - dois parâmetros - range(inicio, fim) - passo será de 1 em 1\n - um parâmetro - range(fim)\n'
intervalo = range()   # Traceback (most recent call last):
                      #   File "<pyshell#131>", line 1, in <module>
                      #     intervalo = range()
                      # TypeError: range expected at least 1 argument, got 0
intervalo = range(0)
intervalo   # range(0, 0)
intervalo = range(5, 10, 2)
intervalo   # range(5, 10, 2)
lista = list(intervalo)
lista   # [5, 7, 9]
tupla = tuple(intervalo)
tupla   # (5, 7, 9)
lista[0] = 15
lista   # [15, 7, 9]
tupla[0] = 15   # Traceback (most recent call last):
                #   File "<pyshell#142>", line 1, in <module>
                #     tupla[0] = 15
                # TypeError: 'tuple' object does not support item assignment
intervalo[0] = 70   # Traceback (most recent call last):
                    #   File "<pyshell#143>", line 1, in <module>
                    #     intervalo[0] = 70
                    # TypeError: 'range' object does not support item assignment