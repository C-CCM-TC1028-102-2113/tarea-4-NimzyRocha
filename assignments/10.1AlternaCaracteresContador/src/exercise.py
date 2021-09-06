def main():
    #escribe tu código abajo de esta línea
    num = int (input())
    cont = 0
    digito = "#"
    while num>cont:
        cont = cont +1
        if digito == "#":
            print (cont,"-",digito)
            digito = "%"
        else:
            if digito == "%":
                print (cont,"-",digito)
                digito = "#"
    pass

if __name__=='__main__':   
    main()
