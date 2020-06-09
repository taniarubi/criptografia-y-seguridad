# Regresa el mínimo común divisor de dos números. 
def mcd(a, b):
    if (b == 0):
        return a 
    else:
        return mcd(b, a % b)

'''
La función phi de Euler regresa el número de enteros positivos que son menores
o iguales a n y que además son primos relativos con n. 
'''
def phi_Euler(n):
    relativos = []
    for i in range (1, n):
        if (mcd(n, i) == 1):
            relativos.append(i)
    return len(relativos)

# Nos dice si a es una raíz primitiva de Zp.
def es_primitiva(a, p):
    for i in range (1, p):
        if(pow(a, i, p) == 1):
            orden = i
            break
    return (orden == p-1) and (mcd(a, p) == 1)

def main():
    print (phi_Euler(10007))
    print(es_primitiva(5, 10007))

if __name__ == "__main__":
    main()
