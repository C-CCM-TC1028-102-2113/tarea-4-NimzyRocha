def main():
    #escribe tu código abajo de esta línea
    cant=float(input())
    suma = 0
    cont = 0
    while cant>0:
        suma = suma + cant
        cont = cont+1
        cant=float(input())
    if suma != 0:
        promedio = suma/cont
        print (promedio)
    else:
        print ("0")
    pass
if __name__=='__main__':
    main()
