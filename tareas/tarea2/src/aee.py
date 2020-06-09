'''
Regresa una tupla (mcd, s, t) que obtenemos al aplicar el algoritmo extendido
de Euclides, donde as + bt = mcd(a, b) son los elementos que conforman la tupla.
'''
def aee(a, b):
    s = 0; s_i = 1
    t = 1; t_i = 0
    g = b; g_i = a

    while g != 0:
        cociente = g_i // g
        g_i, g = g, g_i - cociente * g
        s_i, s = s, s_i - cociente * s
        t_i, t = t, t_i - cociente * t
    return (g_i, s_i, t_i)

# Calcula el inverso de 7 en Z_{2160}.
def main():
    g, s, t = aee(7, 2160)
    # El inverso multiplicativo de a módulo m existe si y sólo si (a,m) = 1.
    if g != 1:
        print("No tiene inverso multiplicativo.")
    else:
        inverso = s % 2160
        print(inverso)
    
if __name__ == "__main__":
    main()
