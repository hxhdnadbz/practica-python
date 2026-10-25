'''Operadores'''
#Operadores aritméticos
print (f"Suma: 5 + 3 = {5 + 3}") #suma
print (f"Resta: 5 - 3 = {5 - 3}") #resta
print (f"Multiplicación: 5 * 3 = {5 * 3}") #multiplicación
print (f"División: 5 / 3 = {5 / 3}") #división
print (f"División entera: 5 // 3 = {5 // 3}") #división entera
print (f"Módulo: 5 % 3 = {5 % 3}") #módulo
print (f"Exponenciación: 5 ** 3 = {5 ** 3}") #exponenciación

#operadores de comparación
print (f" Iguadad: 5 == 3 = {5 == 3}") #igualdad
print (f" Desigualdad: 5 != 3 = {5 != 3}") #desigualdad
print (f" Mayor que: 5 > 3 = {5 > 3}") #mayor que
print (f" Menor que: 5 < 3 = {5 < 3}") #menor que
print (f" Mayor o igual que: 5 >= 3 = {5 >= 3}") #mayor o igual que
print (f" Menor o igual que: 5 <= 3 = {5 <= 3}") #menor o igual que

#operadores lógicos
print (f" AND: True and False = {True and False}") #AND
print (f" OR: True or False = {True or False}") #OR
print (f" NOT: not True = {not True}") #NOT

#Opradores de asignación(se pueden combinar con operadores aritméticos)
x = 5 #asignación simple
x += 1 #asignación con suma
x -= 1 #asignación con resta
x *= 2 #asignación con multiplicación
x /= 2 #asignación con división
x //= 2 #asignación con división entera
x %= 2 #asignación con módulo
x **= 2 #asignación con exponenciación
print (f" x = {x}")

#operadores de identidad (se comprueba si dos variables son el mismo objeto en memoria)
a = [1, 2, 3]
b = a #b es una referencia a a
print (f" a is b = {a is b}") #True
b = [1, 2, 3] #b es una nueva lista con los mismos elementos que a
print (f" a is b = {a is b}") #False   
print (f" a is not b = {a is not b}") #True

#operadores de pertenencia (se comprueba si un elemento está en una secuencia)
print (f" 1 in a = {1 in a}") #True
print (f" 4 in a = {4 in a}") #False

#operadores bit a bit (se aplican a los bits de los números enteros)
x = 5 #binario: 0101
y = 3 #binario: 0011
print (f" AND: x & y = {x & y}") #AND (binario: 0001)
print (f" OR: x | y = {x | y}") #OR (binario: 0111)
print (f" XOR: x ^ y = {x ^ y}") #XOR (binario: 0110)
print (f" NOT: ~x = {~x}") #NOT (binario: 1010)
print (f" Desplazamiento a la izquierda: x << 1 = {x << 1}") #desplazamiento a la izquierda (binario: 1010)
print (f" Desplazamiento a la derecha: x >> 1 = {x >> 1}") #desplazamiento a la derecha (binario: 0010) 

'''Estructuras de control'''
#Estructura condicional if
x = 5
if x > 0:
    print ("x es positivo")

#Estructura condicional if-else
x = -5
if x > 0:   
    print ("x es positivo")
else:
    print ("x es negativo o cero")

#Estructura condicional if-elif-else
x = 0
if x > 0:
    print ("x es positivo")
elif x < 0:
    print ("x es negativo")
else:
    print ("x es cero")

'''Estructuras de control de bucle o iteración'''

#Estructura de control for
for i in range(5):
    print (f"i = {i}")

#Estructura de control while
x = 0
while x < 5:
    print (f"x = {x}")
    x += 1

#estructura de control break
for i in range(5):
    if i == 3:
        break
    print (f"i = {i}")

#estructura de control continue
for i in range(5):
    if i == 3:
        continue
    print (f"i = {i}")

#manejo de excepciones
try:
    x = 5 / 0
except ZeroDivisionError:
    print ("Error: división por cero")
finally:
    print ("Fin del programa")

#Ejercicio:
for i in range (10,56):
    if i % 2 == 0: 
        if i % 3 == 0:  
            continue
        elif i == 16:
            continue
        print (i)

for i in range (10,56):
    if i % 2 == 0 and i % 3 != 0 and i != 16:
        print (f"i = {i}")