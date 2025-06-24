

comprador_entrada={}

#------------------------------------1
def comprador():
    while True:
        nombre_comprador=input("Ingrese nombre de comprador: ")
        if nombre_comprador in comprador_entrada:
            print("Ya existe un comprador con ese nombre")
        else:
            comprador_entrada[nombre_comprador]=[]
            return nombre_comprador

def tipo_de_entrada():
    while True:
        tipo_entrada=input("Ingrese tipo de entrada (G/V): ").upper()
        if tipo_entrada == "G":
            comprador_entrada[tipo_entrada]=[]
            return tipo_entrada
        elif tipo_entrada == "V":
            comprador_entrada[tipo_entrada]=[]
            return tipo_entrada
        else:
            print("Solo se puede G/V: ")
            

def codigo_de_confirmacion():
    while True:
        codigo=input("Ingrese código de confirmación: ")
        cantidad_numeros=0
        cantidad_mayusculas=0
        cantidad_espacios=0
        cantidad_caracteres=len(codigo)
        for letra in codigo:
            if letra.isnumeric():
                cantidad_numeros+=1
            elif letra.isspace():
                cantidad_espacios+=1
            elif letra.isupper():
                cantidad_mayusculas+=1
        if cantidad_caracteres<=5:
            print("Código no válido. Intente otra vez. ")
        elif cantidad_mayusculas<=0:
            print("Código no válido. Intente otra vez. ")
        elif cantidad_espacios>=1:
            print("Código no válido. Intente otra vez. ")
        elif cantidad_numeros<=0:
            print("Código no válido. Intente otra vez. ")
        else:
            comprador_entrada[codigo]=[]
            print("Código validado. ¡Entrada registrada con éxito! ")
            return codigo
#-------------------------------------------------------1       

#-------------------------------------------------------2
def buscar_comprador():
    while True:
        nombre_buscado=input("Ingrese nombre de comprador a buscar: ")
        if nombre_buscado in comprador_entrada:
            print(comprador_entrada)
            return
        else:
            print("El comprador no se encuentra.")
            return
#-------------------------------------------------------2

#-------------------------------------------------------3
def cancelar_compra():
    while True:
        nombre_cancelar=input("Ingrese nombre de comprador a cancelar: ")
        if nombre_cancelar in comprador_entrada:
            del comprador_entrada[nombre_cancelar]
            print("¡Compra Cancelada!")
            return
        else:
            print("No se pudo cancelar la compra")
#-------------------------------------------------------3

while True:
    print("MENU PRINCIPAL")
    print("1.- Comprar entrada")
    print("2.- Consultar comprador")
    print("3.- Cancelar compra")
    print("4.- Salir")

    opcion=input("Ingrese opción: ")

    match opcion:
        case "1":
            comprador()
            tipo_de_entrada()
            codigo_de_confirmacion()
        case "2":
            buscar_comprador()
        case "3":
            cancelar_compra()
        case "4":
            print("Programa terminado...")
            break