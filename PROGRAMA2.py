def nuevoTema(tema):
    print("==== " ,tema, "====")
   
if __name__=="__main__":
    nuevoTema("Operadores Aritméticos")
    #print("===== OPERADORES ARITMETICOS =====")
    print("Operador exponente -> 5 ** 3 =", 5**3)
    print("Operador cociente -> 5 // 3 =", 5//3)

    #ACTIVIDAD: IMPRIMIR LAS TABLAS DE VERDAD DE LOS OPERADORES LÓGICOS
    #print("===== OPERADORES LÓGICOS =====")
    nuevoTema("OPERADORES LÓGICOS")
    print("Operador AND (TRUE AND FALSE) =", True and False)
    print("Operador AND (TRUE AND TRUE) =", True and True)
    print("Operador AND (FALSE AND TRUE) =", False and True)
    print("Operador AND (FALSE AND FALSE) =", False and False)
    print("===== OPERADORES DE  COMPARACIÓN =====")
    print("2==3 ", 2==3)
    print("2>=3 ", 2>=3)
    print("2<=3 ", 2<=3)
    print("2!=3 ", 2!=3)
    print("2>3 ", 2>3)
    print("2<3 ", 2<3)

    nuevoTema("VARIABLES")
    variable="10"
    _variable="6.28"
    Variable3="juancho"
    dosPalabras="Hola Mundo"
    dos_palabras="Estilo Phyton"
    print(Variable3,"\n", variable,dos_palabras,dosPalabras)

    a,b,c=5,10,"Welcome"
    print(a)
    print(b)
    print(c)


    nuevoTema("Enteros")
    w=105
    x=7486666
    y=-256
    

    nuevoTema("Flotantes")
    x=1297.50
    print(x, type(x))
    y=0.59554
    print(y, type(y))


    nuevoTema("booleanos")
    lis=[8]
    print(lis, "is", bool(lis))
    val=none
    print(val,type(val))
    val=true
    print(val, type(val))

    nuevoTema("listas")
    a=[10,20.5,"python list"]
    print(a)
    print(a[1])
    a[1]="hola"
    print(a)

    nuevoTema("Tuplas")
    t=(25,"tupla",1+10j,45.6)
    print(t)
    print(t[1])
    print("t[0:3]=", t[0:3])


    nuevoTema("Diccionarios")
    d={1:"Valor1", 2:"valor2","nombre":"juancho"}
    print(d,type(d))
    print("d[1]=",d[1])
    print("d[Nombre]= ", d["Nombre"])



