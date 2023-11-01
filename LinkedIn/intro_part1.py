"""
Curso Docente   : Ana Maria Pinto
Curso Nombre    : Python
Nivel           : Principiate
"""
# declaracion de la variable utilizar snake_case
mi_variable = "Hola Mundo!"
# print(mi_variable) # funciones tipo buil-in

# tipos de variables
variable_int = 4
variable_float = 3.14
variable_string = "@crslaureano"
variable_bool = True

# print(variable_int, variable_float, variable_string, variable_bool, sep='\n')

# Operadores
# (), **, /, *, +-, segun orden de importancia
operacion = (2+3)**2 + (3/4 - 1)
# print(operacion)

user_name = "@crslaureano"
# print(user_name*3, user_name+"God", sep='\n')

# Simbolos de comparacion
# mayoria de edad
edad = 18
# print(edad>=18)
# print(edad<=18)
# print(edad==18)

# Estructuras de Datos

# Lista

my_list1 = list()
my_list2 = []

print(my_list1 is my_list2)

my_list1.append("Hola")
my_list1.append("Mundo!")
my_list2.extend([1, 2, 3, 4])
my_list2.append([5, 6])

print(my_list1)
print(my_list2)

# Tuplas

my_tuple1 = tuple()
my_tuple2 = ()
my_tuple3 = 1,

print(type(my_tuple1))
print(type(my_tuple2))
print(type(my_tuple3))

# Diccionarios
dictionary_f1 = dict()
dictionary_f2 = {
    "key" : "value",
}
dictionary_f3 = dict(
    key = "value",
)

print(dictionary_f1)
print(dictionary_f2)
print(dictionary_f3)
