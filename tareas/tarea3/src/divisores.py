# Regresa los divisores de un número n.
def divisores(n):
    div = []
    for i in range (1, n):
        if ((n % i) == 0):
            div.append(i)
    
    return div

if __name__ == "__main__":
    print(divisores(72))
