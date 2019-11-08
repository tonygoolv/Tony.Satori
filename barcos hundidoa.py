
def ingresarDatos():
    cb = int(input("ingrese cantidad de barcos: "))
    tamb = []
    for i in range(cb):
        tamb.append(int(input("ingrese tamaño barco: ")))
    
    tam = int(input("ingrese tamaño tablero: "))
    tablero = []
    for i in range(tam):
        s = input("ingrese fila: ")
        tablero.append(list(s))
    return cb, tamb, tam, tablero

def enmarcar(tablero):
    n = len(tablero)
    ceros = ['0']*(n+2)
    for fila in tablero:
        fila.insert(0,'0')
        fila.insert(n-1,'0')
    tablero.insert(0,ceros)
    tablero.insert(n,ceros)
    return tablero

def aislado(barco,tablero):
    d = barco[-1]
    valido = True
    if d == 'H':
        t = len(barco)-1
        for b in barco[:t]:
            x,y = b
            if tablero[x-1][y-1]==1 or tablero[x-1][y]==1 or tablero[x-1][y+1]==1:
                valido = False
            if tablero[x+1][y-1]==1 or tablero[x+1][y]==1 or tablero[x+1][y+1]==1:
                valido = False
    print(valido)

def barcosAislados(cb,barcos,tablero,tamb):
    contb = 0
    i = 0
    conta = 0
    while contb < cb:
        barquito = []
        x,y = barcos[i]
        while i < len(barcos) and (x == barcos[i][0] or y == barcos[i][1]):
            if x == barcos[i][0]:
                d = 'H'
            if y == barcos[i][1]:
                d = 'V'
            barquito.append(barcos[i])
            i = i + 1
        barquito.append(d)
        contb = contb + 1
    
        a = aislado(barquito,tablero)
        if a == True:
            conta = conta+1
    if conta == cb:
        return True
    else:
        return False
    
        
def verificarTablero():
    cb,tamb,tam,tablero = ingresarDatos()
    tablero = enmarcar(tablero)
    print (tablero)
    tam = tam + 2
    barcos = []
    for i in range(tam):
        for j in range(tam):
            if tablero[i][j] == '1':
                barcos.append((i,j))
    correcto = len(barcos) == sum(tamb)
    correcto = correcto and barcosAislados(cb,barcos,tablero,tamb)
    #return correcto
    print(barcos)
    
verificarTablero()
