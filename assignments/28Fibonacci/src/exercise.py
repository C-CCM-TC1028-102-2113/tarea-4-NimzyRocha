
def main():
    #escribe tu código abajo de esta línea
    indice = int (input("Enter a number: "))
    indice = indice-1
    serie = 1
    num = 0
    cont=1
    while indice != 0:
        serie = num + serie    
        cont = cont +1     
        num = serie - num    
        indice = indice - 1   
    print(serie)
    pass

if __name__=='__main__':
    main()
