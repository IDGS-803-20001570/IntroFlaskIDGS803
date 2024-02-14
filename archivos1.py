from io import open

# archivo_texto = open('nombres.txt','a')
# archivo_texto.write('\n Datos en el Archivo')
# archivo_texto.close()

# archivo_texto = open('nombres.txt','r')
# print(archivo_texto.read())

# archivo_texto.seek(0)
# #manejo de la posición lectura

# print(archivo_texto.read())
# archivo_texto.close()

# LEE LÍNEA POR LÍNEA
# archivo_texto = open('nombres.txt','r')
# print(archivo_texto.readline())
# archivo_texto.close()

archivo_texto = open('nombres.txt','r')
for lineas in archivo_texto.readlines():
    print(lineas.rstrip())
archivo_texto.close()

# rstrip() --> QUITA SALTOS DE LÍNEAS ADICIONALES