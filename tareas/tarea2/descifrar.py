# Descifra un mensaje utilizando RSA. 
def descifrar(d, n):
    # Leemos el archivo de texto donde se encuentra el mensaje.
    file = open('texto.txt', 'r')
    data = file.readlines()
    file.close()

    msg = []
    # Calculamos c^d (mod n) para cada uno de los elementos del mensaje.
    for renglon in data:
        for palabra in renglon.split(' '):
            msg.append(pow(int(palabra), d, n))
    print(msg)

    modulo = []
    # Le aplicamos (mod 26) a cada uno de los elementos del mensaje descifrado.
    for elemento in msg:
        modulo.append(elemento % 26)
    print(modulo)
        
def main():
    descifrar(1543, 2257)

if __name__ == "__main__":
    main()
