#variable
edad = 17
calificacion = 70
frutas = ["manzana", "banana", "naranja"]
contador = 0



# if 

if  edad >= 18:
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