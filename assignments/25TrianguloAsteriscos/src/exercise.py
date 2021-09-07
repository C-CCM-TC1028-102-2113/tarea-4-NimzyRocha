
def main():
    #Escribe tu código debajo de esta línea
    h = int (input("Enter triangle height: "))
    cont = h
    contdos = 0
    while cont != 0 :
        cont = cont - 1
        espacio = cont * " "
        contdos = contdos + 1
        asterisco = contdos * "*"
        print (espacio,asterisco)
    pass


if __name__=='__main__':
    main()
