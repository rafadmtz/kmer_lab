# Casos de Prueba


### Caso normal

**Entrada**

- DNA: `ATGCG`
- k: `3`

**Salida esperada**


ATG
TGC
GCG


---

### Caso límite

Cuando **k es igual a la longitud de la secuencia**.

**Entrada**

- DNA: `ATG`
- k: `3`

**Salida esperada**


ATG


---

### Caso de trazado manual

Realizar un **trazado manual del algoritmo**.

**Ejemplo**


seq = ATGCG
k = 3


| Posición |
|----------|
| 0 | ATG |
| 1 | TGC |
| 2 | GCG |