try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

#-------------------------------------------------------------------------------------------
def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")    