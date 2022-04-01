##Funciones con parametros

from unittest import result


def print_param(daddy):
    print(daddy)
    print(daddy)
    
print_param(77)

singer = 'marcianeke'
print_param(singer)



def volumen(radio):
    result = 4/3 * 3.1416 * radio **3
    print(result)

radio = 5
big = 7
volumen(radio)

def multiply_by_2(number):
    number = number * 2
    print(number)

multiply_by_2(big)
print(big)

# Funcion de 2 parametros

def concat_strings(str1, str2):
    longstr = str1 + " " + str2
    print(longstr)

text1 = 'pasito a pasito'
text2 = 'suave, suavecito'

concat_strings(text1, text2)