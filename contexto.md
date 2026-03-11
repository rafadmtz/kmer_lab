# Descripción del Proyecto

## 1. Problema
Generar todos los fragmentos consecutivos de longitud **k (k-mers)** a partir de una secuencia de DNA proporcionada por el usuario, calcular el contenido de GC de cada k-mer e identificar cuál o cuáles tienen el mayor contenido de bases G y C.

## 2. Datos de entrada
- Una secuencia de DNA introducida por el usuario.
- Un número entero **k** que representa el tamaño del **k-mer**.

## 3. Requisitos funcionales
- Leer una secuencia de DNA.
- Leer el valor de **k**.
- Validar que la secuencia solo contenga los caracteres `A`, `C`, `T`, `G`.
- Recorrer la secuencia con una ventana deslizante de tamaño k.
- Generar todos los **k-mers** de longitud **k**.
- Mostrar cada **k-mer** junto con su posición.
- Calcular el contenido de GC de cada k-mer.
- Identificar el valor máximo de contenido GC entre todos los k-mers.
- Mostrar los **k-mers** que tengan el mayor contenido de GC.

## 4. Requisitos no funcionales
- El programa debe aceptar secuencias en **mayúsculas o minúsculas**.
- La secuencia debe convertirse a **mayúsculas** antes de procesarse.
- El programa debe terminar con un mensaje de error si la secuencia está vacía o contiene caracteres inválidos.
- El código debe ser **legible** y seguir convenciones básicas de estilo.

## 5. Algoritmo

1. Leer la secuencia de DNA e convertirla a mayúsculas.
2. Validar que la secuencia no esté vacía y que solo contenga `A`, `C`, `T`, `G`.
3. Leer el valor de **k**.
4. Recorrer la secuencia desde la posición `0` hasta `len(seq) - k` (inclusive) usando una ventana deslizante.
5. En cada posición `i`, extraer el k-mer `seq[i:i+k]` y almacenarlo en una lista.
6. Mostrar cada k-mer junto con su posición.
7. Recorrer la lista de k-mers y contar el número de bases `G` y `C` en cada uno.
8. Registrar el conteo máximo de GC encontrado.
9. Recorrer nuevamente la lista y mostrar todos los k-mers cuyo conteo GC sea igual al máximo.