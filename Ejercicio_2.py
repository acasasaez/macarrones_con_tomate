def fuct (b = str(input("Introducir cadena"))):
    a = 0
    for i in b:
        a+=1
    if a>= 3 and 10>a:
            print ("La cadena tiene una longitud mayor o igual que 3 y menor que 10 ")
    else:
            print ("La cadena no tiene una longitud mayor o igual que 3 y menor que 10 ")
 
fuct()