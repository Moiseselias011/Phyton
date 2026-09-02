#variable

a = 3.23
b = 2.23
c = 2.34

#ejercicios

suma = (a+b) * c                               # 1
suma_es = a + b                                # 2
son_iguales = a != b                           # 3
dividido_entero = a // b                       # 4
resultado_and = (b < 3.23) and (2.23 > c)      # 5
resultado_or = (b < 3.23) or (2.23 > c)        # 6
resultado_not = not (2.23 > c)                 # 7

#vista por consola 

print ("1 el resultado es :" + str(suma))
print ("2 el resultado es :" + str(suma_es))
print ("3 el resultado es :" + str(son_iguales))
print ("4 el resultado es :" + str(dividido_entero))
print ("5 el resultado es :" + str(resultado_and))
print ("6 el resultado es :" + str(resultado_or))
print ("7 el resultado es :" + str(resultado_not))



#---------------------------------------------------------------------------------------------

#variable

edad = 17
calificacion = 70
frutas = ["manzana", "banana", "naranja"]
contador = 0



# if 

if  a >= 18:
   print ("eres mayor de 18? " )
else:
   print ("eres menor de 18 ") 

# elif
if  calificacion >= 95:
   print("EXELENTE ")

elif calificacion >= 85:
   print("Muy bueno") 
elif calificacion >= 70:
   print("bueno")
else:
   print("desaprovado")        


# for

for fruta in frutas:
    print(fruta)




# while 
while contador < 5:

    print(contador)
    contador += 1

# while con true break cierra subitamente
while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

#for con range 

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)




#--------------------------------------------------------------------------------