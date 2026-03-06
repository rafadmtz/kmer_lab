# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA
seq = input("DNA:").upper()

if not seq:
    print("Secuencia vacia.")
    exit(1)

#Validar secuencia
for x in seq:
    if x not in "ACTG":
        print(f"Caracter no valido: {i}")
        exit(1)


# 2. Leer el valor de k
k =  int(input("k (int): "))

# 3. Recorrer la secuencia con una ventana de tamañASAo k
for i in range(len(seq) - k + 1):
     
    # 4. Extraer el k-mer de la posición actual
    kmer = seq[i:i-k]

    # 5. Mostrar el k-mer
    print(f"Posicion {i} --> {kmer}")