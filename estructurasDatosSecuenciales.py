temp = [30.5, 19.8, 12.3, 31.0, 19.9, 34.4, 25.3]

# Imprimir el primer elemento de la lista
print("Primer elemento de la lista con posición 0", temp[0])

# Imprimir el tercer elemento de la lista
print("\nCuarto elemento de la lista con posición 3", temp[3])

# Imprimir del tercer al quinto elemento de la lista sin incluir el quinto
print("\nCuarto y sexto elemento de la lista con posición 3, 4 y 5 sin incluir este último: ", temp[3:5])

print("\nLongitud de la lista: ", len(temp), "\n")

# Para recorrer la lista
for i in range(len(temp)):
    print("Elementos de la lista, posicion", i+1, ":", temp[i])

# .append es utilizado para agregar elemntos a la lista
# pero siempre los agrega al final de la lista
temp.append(18.3)
print("\nLista de temperatura con el nuevo elemento 18.3:", temp)
print("\nNuevo octavo elemento en la posición 7:", temp[7])

# .insert es utilizado para agregar elementos a la lista en una posición específica
# mueve lo que etsaba antes en esa posición a la derecha
temp.insert(5, 12.5)
print("\nLista de temperatura con el nuevo elemento 22.1 en la posición 3:", temp, "\nLonigtud de la lista con el nuevo elemento:", len(temp))

# eliminar un elemento de la lista
temp.remove(12.3)
print("\nLista de temperatura sin el elemento 12.3:", temp, "\nLongitud de la lista sin el elemento:", len(temp))

# nueva lista de idas de la semana
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# si la temperatura 31.0 está en la lista temp, entonces con index se obtiene la posición del valor
if 31.0 in temp:
    pos = temp.index(31.0)

print("\nEl día que la tempratura fue de 31.0 fue el dia", dias[pos], "que corresponde a la posición en la lista de días:", pos)
