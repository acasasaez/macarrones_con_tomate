def funcion():
    while True:
        while True:
            try:
                a = int(input("valor1"))
                b =int(input("valor2"))
            
            
                break
            except :
                print("Error")
           
        if a >=1 and 9>=a and b >=1 and 9>=b:
                for i in range (a):
                    for j in range (b):
                        print("*",end = "" )
                break
        
        else:
                print("Introduzca un número del 1 al 9")

funcion()