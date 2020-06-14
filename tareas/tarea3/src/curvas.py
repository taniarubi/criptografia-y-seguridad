from campo_finito import inverso

'''
Regresa los puntos que pertenecen a la curva elíptica 
E: y^2 = x^3 + Ax + B (mód n)
'''
def encontrar_puntos(A, B, n):
    puntos = []
    # Sabemos que x pertenece al conjunto [0, 70].
    for i in range (0, n):
        # Sabemos que y pertenece al conjunto [0, 70]. 
        for j in range (0, n):
            # Encontramos el valor de x^3 + Ax + B (mód n)
            valor = (pow(i, 3, n) + ((A * i) % n) + B) % n
            # Encontramos los posibles valores para y.
            y2 = pow(j, 2)
            # Verificamos que el par satisface la ecuación.
            if (((y2 - valor) % n) == 0):
                puntos.append((i, j))
    
    print("La curva elíptica E tiene " + str(len(puntos) + 1) + " puntos.")
    return puntos

# Regresa la suma de dos puntos P y Q en E. 
def suma_puntos(P, Q, A, p):
    # Casos especiales.
    if (P == None):
        return Q
    if (Q == None):
        return  P
        
    x1, y1 = P
    x2, y2 = Q
    
    if (x1 == x2):
        m = (3 * x1 * x1 + A) * inverso(2 * y1, p)
    else:
        m = (y1 - y2) * inverso(x1 - x2, p)
        
    x3 = m * m - x1 - x2
    y3 = m * (x1 - x3) - y1
    suma = (x3 % p, y3 % p)
    return suma

# Regresa el órden de un elemento en E.
def orden(P, a, p):
    # Como P = P y y_1 = 0 entonces P+P = infinito.
    if(P[1] == 0):
        return 2
    
    # Calculamos 2P.
    P2 = suma_puntos(P, P, a, p)
    aux = P2
    
    orden = 3
    for i in range(0, p):
        # Calculamos P + kP
        aux = suma_puntos(P, aux, a, p)
        # Si encontramos a 2P, entonces hemos encontrado el órden.
        if(aux == P2):
            break
        orden += 1
    return orden

# Regresa el órden de cada uno de los elementos en la lista puntos.
def get_ordenes(puntos, a, p):
    ordenes = []
    for punto in puntos:
        o = orden(punto, a, p)
        ordenes.append(o)
    
    return ordenes
    
if __name__ == "__main__":
    print(encontrar_puntos(1, 28, 71))
    print(get_ordenes(encontrar_puntos(1, 28, 71), 1, 71))
    