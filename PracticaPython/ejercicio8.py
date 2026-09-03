def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("juan")   
saludo("vanesa") 

#------------------------------------------------------------------------------------------

def suma (a,b):
    return a + b

resultado = suma(7,8)
print(resultado)    


#-------------------------------------------------------------------------------------------
b = 2
cuadrado = lambda x: x ** b
print(cuadrado(5)) 

#-------------------------------------------------------------------------------------------
a = 10
dividido = lambda x: x / a
print(dividido(200))

#------------------------------------------------------------------------------------------

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  
print(suma_variable(4, 5, 6, 7))