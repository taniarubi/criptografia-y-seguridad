'''
Regresa una tupla (mcd, s, t) que obtenemos al aplicar el algoritmo 
extendido de Euclides, donde as + bt = mcd(a, b) son los elementos que 
conforman la tupla.
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

# Calcula todas las unidades en Z_{156}.
def unidades():
    for i in range(0, 156):
        g, s, t = aee(i, 156)
        # El inverso multiplicativo de a modulo m existe sii (a,m) = 1
        if g != 1:
            continue 
        else:
            inverso = s % 156
            print("(" + str(i) + ", " + str(inverso) + ")")
            
if __name__ == "__main__":
    unidades()