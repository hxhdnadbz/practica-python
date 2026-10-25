'''Funciones definidas por el usuario'''

#Funciones simples
def saludar():
    print ("¡Hola!")
saludar()

#Funciones con  retorno de valores
def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print (f"El resultado de la suma es: {resultado}")


#Funciones con argumentos predefinidos
def saludar(nombre, saludo = "¡Hola!"):
    print (f"{saludo} {nombre}")
saludar("Juan")

#Funciones con retorno de múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
resultado = operaciones(10, 5)
print (operaciones(20, 2))

#Funciones con numero variable de argumentos
def goat(*player):
    for names in player:
        print (f"{names} es un gran jugador")
goat("Messi", "Cristiano Ronaldo", "Neymar", "Mbappé", "Lewandowski")

#funciones con argumentos de palabras clave
def jugador(**player):
    for key, value in player.items():
        print (f"{key} es un gran jugador y su nacionalidad es {value}")
jugador(Messi = "Argentina", 
        Cristiano_Ronaldo = "Portugal", Neymar = "Brasil", 
        Mbappé = "Francia", Lewandowski = "Polonia"
        )

'''Funciones dentro de funciones'''
def outer_function():
    print ("Esta es la función externa")
    def inner_function():
        print ("Esta es la función interna")
    inner_function()
outer_function()

'''Funciones del lenguaje'''

'''print (len"Hola") #Devuelve la longitud de la cadena'''
print (type(10)) #Devuelve el tipo de dato de la variable
print (isinstance(10, int)) #Devuelve True si la variable es del tipo especificado

'''variables globales y locales'''
x = 10 #Variable global
def funcion():
    x = 5 #Variable local
    print (f"Variable local: {x}")
funcion()
print (f"Variable global: {x}")
'''las variables locales tienen prioridad sobre las variables globales con el mismo nombre,
las locales sólo se usan dentro de la función donde se definen, mientras que las globales 
se pueden usar en cualquier parte del código'''
       
'''Ejercicio'''

def my_num(my_num1, my_num2):
    counter = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print (my_num1 + my_num2)
        elif number % 3 == 0:
            print (my_num1)
        elif number % 5 == 0:
            print (my_num2)
        else:
            print (number)
            counter += 1
    return counter

my_num("Fizz", "Buzz")


