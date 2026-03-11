# Casos de Prueba

## 1. Definición de casos de prueba

---

### Caso normal

**Entrada**
- DNA: `ATGCG`
- k: `3`

**Salida esperada**
```
Posicion 0 --> ATG
Posicion 1 --> TGC
Posicion 2 --> GCG
K-mers con mayor contenido de gc
Posicion 2 --> GCG
```

**Explicación**  
Secuencia con longitud mayor que k. Se generan 3 k-mers (len - k + 1 = 5 - 3 + 1 = 3). El k-mer con mayor contenido GC es `GCG` con 2 bases G/C.

---

### Caso límite

Cuando **k es igual a la longitud de la secuencia**.

**Entrada**
- DNA: `ATG`
- k: `3`

**Salida esperada**
```
Posicion 0 --> ATG
K-mers con mayor contenido de gc
Posicion 0 --> ATG
```

**Explicación**  
Cuando k = len(seq), el rango produce exactamente un k-mer: la secuencia completa. Verifica que el algoritmo no se rompe en el caso borde donde la ventana tiene el mismo tamaño que la secuencia.

---

### Trazado manual del algoritmo

**Entrada**
```
seq = ATGCG
k = 3
```

**Ejecución paso a paso del loop principal:**

`range(len(seq) - k + 1)` = `range(5 - 3 + 1)` = `range(3)` → iteraciones: 0, 1, 2

| i | seq[i:i+k] | k-mer | Conteo GC |
|---|------------|-------|-----------|
| 0 | seq[0:3]   | ATG   | 1 (G)     |
| 1 | seq[1:4]   | TGC   | 2 (G, C)  |
| 2 | seq[2:5]   | GCG   | 3 (G, C, G) → **máximo** |

**Resultado:** el k-mer con mayor contenido GC es `GCG` en posición 2.

---

## 2. Ejecución de los casos de prueba

---

### Caso normal — ejecución real

**Entrada utilizada**
```
DNA: ATGCG
k: 3
```

**Salida obtenida**
```
Posicion 0 --> ATG
Posicion 1 --> TGC
Posicion 2 --> GCG
K-mers con mayor contenido de gc
Posicion 2 --> GCG
```

**Verificación**  
✅ Coincide con la salida esperada. Se generaron los 3 k-mers correctos y se identificó `GCG` como el de mayor contenido GC.

---

### Caso límite — ejecución real

**Entrada utilizada**
```
DNA: ATG
k: 3
```

**Salida obtenida**
```
Posicion 0 --> ATG
K-mers con mayor contenido de gc
Posicion 0 --> ATG
```

**Verificación**  
✅ Coincide con la salida esperada. Con k igual a la longitud de la secuencia, se produce exactamente un k-mer y el programa lo maneja correctamente sin errores.