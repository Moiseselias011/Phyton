frutas=["banana","manzana","uva"]

#agrega un elemento al final de la lista.
frutas.append("pera")
print(frutas)


#inserta un elemento en una posición específica de la lista.
frutas.insert(2,"kiwi")
print(frutas)


#elimina la primera aparición de un elemento en la lista.
frutas.remove("manzana")
print(frutas)


#elimina y devuelve el elemento en una posición específica de la lista.
fruta_eliminada = frutas.pop(1)
print(frutas)
print("fruta eliminada:", fruta_eliminada)


#ordena los elementos de la lista en orden ascendente.
frutas.sort()
print(frutas)


#nvierte el orden de los elementos en la lista
frutas.reverse()
print(frutas)

