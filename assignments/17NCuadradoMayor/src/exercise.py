

def main():
    #Escribe tu código debajo de esta línea
    numero = int (input("Escribe un numero : "))
    cuadrado = 1
    resultado =0
    while resultado < numero:
        cuadrado = cuadrado + 1
        resultado = cuadrado**2
    print (cuadrado)
    pass

if __name__=='__main__':
    main()
