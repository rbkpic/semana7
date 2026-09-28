matriz =[]
filas=0
columnas=0

def pedirtamaño(i, j):
    global filas, columnas
    filas=i
    columnas=j

pedirtamaño(3, 3)
print

def leervalor():
    while True:
        try:
            valor = int(input("Dime un valor numerico: "))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero.")

def agregarelemento(elemento):
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input("Valor: ")))

pedirtamaño(2, 2)
print(filas, columnas)
agregarelemento()