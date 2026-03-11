# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA
seq = input("DNA:").upper()

if not seq:
    print("Secuencia vacia.")
    exit(1)

#Validar secuencia
for x in seq:
    if x not in "ACTG":
        print(f"Caracter no valido: {x}")
        exit(1)


# 2. Leer el valor de k
k =  int(input("k (int): "))



#Lista para almacenar los k-mers
gc_kmer=[]


# 3. Recorrer la secuencia con una ventana de tamaño k
for i in range(len(seq) - k + 1):
     
    # 4. Extraer el k-mer de la posición actual
    kmer = seq[i:i+k]
    gc_kmer.append(kmer)
    
    # 5. Mostrar el k-mer
    print(f"Posicion {i} --> {kmer}")
    

#Variable para almacenar el maximo conteo de GC
max_gc=0
    
    
# 6. Contar el contenido de GC en cada k-mer y encontrar el maximo   
for j in gc_kmer:
    
    conteo_gc=(j.count("G")+j.count("C"))
    
    if conteo_gc > max_gc:
        max_gc=conteo_gc


print("K-mers con mayor contenido de gc")


# 7. Mostrar los k-mers con el mayor contenido de GC y su posicion
for j, k in enumerate(gc_kmer):
    if (k.count("G")+k.count("C"))==max_gc:
        print(f"Posicion {j} --> {k}")



# 8. Mostrar la secuencia original y los k-mers con el mayor contenido de GC en formato de ventana deslizante
print('Ventana deslizante con k-mers')

print(seq)
for j, k in enumerate(gc_kmer):
    print(" "*(j)+k)
