'''Estructuras de datos en Python'''

'''Listas'''
my_list = [1, 2, 3, 4, 5]#son datos ordenados y mutables, se pueden modificar
print (my_list)
add.my_list = [6, 7, 8] #Agrega una lista al final de la lista
print (my_list)
pop.my_list = my_list.pop() #Elimina el último elemento de la lista
print (my_list)


'''Tuplas'''
my_tuple = (1, 2, 3, 4, 5)#son datos ordenados e inmutables, no se pueden modificar
print (my_tuple)

'''Conjuntos'''
my_set = {1, 2, 3, 4, 5} #son datos desordenados y no permiten elementos duplicados
print (my_set)

'''Diccionarios'''
my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
#son datos desordenados y mutables, se pueden modificar, se accede a los elementos mediante una clave
print (my_dict)

'''Funciones en estructuras de datos'''
#Listas
my_list.append(6) #Agrega un elemento al final de la lista
print (my_list)
my_list.remove(3) #Elimina un elemento de la lista
print (my_list)
#Tuplas
#Las tuplas son inmutables, no se pueden modificar
#Conjuntos
my_set.add(6) #Agrega un elemento al conjunto
print (my_set)
my_set.remove(3) #Elimina un elemento del conjunto
print (my_set) 
#Diccionarios
my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
my_dict["pais"] = "España" #Agrega un elemento al diccionario
print (my_dict)