# Uso de Inteligencia Artificial

## Herramienta utilizada
Claude (Anthropic) — asistente de IA conversacional.

## Para qué se utilizó

La IA se utilizó como apoyo en las siguientes partes del trabajo:

- **Documentación** — Se utilizó para estructurar y redactar `contexto.md` y `pruebas.md`, asegurando que cubrieran todos los elementos requeridos por la rúbrica (problema, entradas, requisitos funcionales y no funcionales, algoritmo, casos de prueba).
- **Ejecución de casos de prueba** — Se utilizó para correr el programa (`kmer_lab.py`) con los casos de prueba definidos e inferir las salidas reales, las cuales fueron luego verificadas contra las salidas esperadas.
- **Revisión del algoritmo** — Se utilizó para verificar que la descripción del algoritmo en `contexto.md` reflejara con precisión los pasos implementados en el código, incluyendo la validación de la secuencia y el cálculo del contenido GC.

## Sugerencias generadas por la IA

- Expandir `pruebas.md` con una segunda sección de ejecución real, separando claramente la *definición* de los casos de su *verificación*.
- Actualizar el algoritmo en `contexto.md` para incluir los pasos de validación y cálculo de GC que el código ya implementaba pero no estaban documentados.
- Agregar una columna de conteo GC en el trazado manual para hacer el análisis más explícito.

## Modificaciones realizadas por el estudiante

- El código de `kmer_lab.py` fue escrito íntegramente por el estudiante sin intervención de la IA.
- El estudiante definió los casos de prueba y las entradas; la IA ayudó a formatearlos y completar la sección de resultados.
- La descripción del problema y los requisitos fueron redactados originalmente por el estudiante; la IA los revisó y completó donde faltaban detalles.