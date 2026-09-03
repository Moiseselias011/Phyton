#mi_tubla = [1,3,5,1,7,8,1]

#print  (mi_tubla.count(1)) # dice cuantas veces se repite el numero

#print (mi_tubla.index(7))  # te dice en que lugar se encuentra tu numero
#print (mi_tubla.index(1, 4)) #se puede dar un numero de donde empieza tambien

#print (len(mi_tubla))  # longitud de la tupla 



#--------------------------------------------------------------------------------------------------

persona = {"nombre" : "Moises", "edad" : 31 , "ciudad" : "san luis"}

#print( persona["nombre"])

#print( persona["edad"])

#print(  persona["ciudad"])

#-------------------------------------------------------------------------------------------------------

print (persona.keys())     # solo los casos
print (persona.values())   # solo los valores
print (persona.items())    # solo los casos y valores

persona.update({"profecion":"programador"})
print(persona)                               # agrega 