matriz =[]
filas=0
columnas=0

def pedirtamaño(i, j):
    global filas, columnas
    filas= int(input("Cantidad de filas: "))
    columnas= int(input("Cantidad de columnas: "))


def leervalor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero.")

def agregarelemento(elemento):
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            dato=leervalor(f"Valor [{i+1}, {j+1}]:")
            matriz[i].append(dato)

def menu():
    print("""
1. Asignar tamaño
2. agregar elemento
3. salir    
""")
    op=leervalor()
    return op

def main():
    while True:
        op=menu()
        if op==1:
            pedirtamaño()
        elif op==2:
            agregarelemento()
        elif op==3:
            print("Adios...")
            break

main()