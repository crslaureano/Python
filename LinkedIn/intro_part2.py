"""
Autor       : @crslaureano
Curso       : LinkedIn - Python
Nivel       : Principiante
Tag         : if, for, while, def
"""

# Condicionales if-elif-else
import random

# Ejemplo mayoria de edad
# edad = random.randint(1, 36)

# if edad >= 18:
    # print(f"Tu edad {edad}, eres mayor")
# else:
    # print(f"Menor de edad, aun tienes {edad}")

# ingreso = True if edad >= 18 else False

# print("Mayor de edad") if edad >= 18 else print("Menor de edad")

# print("Mayor" if edad >= 18 else "Menor")

# Ejemplo examen Muy bueno, bueno, regular, bajo

notas = [random.randint(0, 20) for i in range(10)]
valoracion = list()

for nota in notas:
    if nota>=18 and nota<=20:
        valoracion.append("Muy Bueno")
    elif nota>=15 and nota<=17:
        valoracion.append("Bueno")
    elif nota>=13 and nota<=14:
        valoracion.append("Regular")
    elif nota>=11 and nota<=12:
        valoracion.append("regular")
    else:
        valoracion.append("bajo")

notas_valoradas = list(zip(notas, valoracion))
# print(notas)
# print(valoracion)
# print(notas_valoradas)

# for n, v in zip(notas, valoracion):
    # print(f"> {n:<3} -> {v}")


# Ejemplo While

print(notas)
longitud = len(notas)
registro = 0

while registro<longitud:
    if notas[registro]>=18 and notas[registro]<=20:
        registro += 1
        print(f"{registro} Muy Bueno")
    elif notas[registro]>=15 and notas[registro]<=17:
        registro += 1
        print(f"{registro} Bueno")
    elif notas[registro]>=13 and notas[registro]<=14:
        registro += 1
        print(f"{registro} Regular")
    elif notas[registro]>=11 and notas[registro]<=12:
        registro += 1
        print(f"{registro} regular")
    else:
        registro += 1
        print(f"{registro:} bajo")

# Funciones

def promedio(*args):
    elementos = len(args)
    if elementos == 0:
        return 0.0
    return sum(args)/elementos

def registro(elementos:int) -> list:
    return list(random.randint(1, 10) for i in range(elementos))

entrada_nota = [random.randint(0,10) for i in range(10)]

print(entrada_nota)
print(promedio(*entrada_nota))
print(promedio(*registro(10)))

