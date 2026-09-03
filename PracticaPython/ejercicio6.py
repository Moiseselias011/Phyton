#clave valor
persona={"nombre":"Juan","edad":30,"ciudad":"Buesnos Aires"}
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

#keys(): devuelve una vista de todas las claves del diccionario.
print(persona.keys())
#values(): devuelve una vista de todos los valores del diccionario.
print(persona.values())
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
print(persona.items())
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
persona.update({"pais":"Argentina"})
print(persona)