# CALCULADORA CIENTÍFICA

## Descripción

Calculadora científica por consola desarrollada en Python por estudiantes de la FNI (Ingeniería de Sistemas e Ingeniería Informática). Permite realizar operaciones matemáticas básicas y avanzadas desde un menú, valida las entradas del usuario para evitar errores y guarda un historial de las operaciones realizadas durante la ejecución.

## Operaciones

| N.º | Operación | Función | Estado |
|---|---|---|---|
| 1 | Suma | `suma(a, b)` | ✅ Completada |
| 2 | Resta | `resta(a, b)` | ✅ Completada |
| 3 | Multiplicación | `multiplicacion(a, b)` | ✅ Completada |
| 4 | División (controla división por cero) | `division(a, b)` | ✅ Completada |
| 5 | Potencia | `potencia(base, exponente)` | ✅ Completada |
| 6 | Módulo (controla divisor cero) | `modulo(a, b)` | ✅ Completada |
| 7 | Raíz cuadrada (no acepta negativos) | `raiz_cuadrada(n)` | ✅ Completada |
| 8 | Porcentaje | `porcentaje(porcentaje, cantidad)` | ✅ Completada |
| 9 | Valor absoluto | `valor_absoluto(n)` | ✅ Completada |
| 10 | Factorial (enteros no negativos) | `factorial(n)` | ✅ Completada |
| 11 | Promedio | `promedio(numeros)` | ✅ Completada |
| 12 | Redondeo | `redondear(valor, decimales)` | ✅ Completada |
| 13 | Ver historial | `mostrar_historial(historial)` | ✅ Completada |
| 14 | Limpiar historial | `limpiar_historial(historial)` | ✅ Completada |

También incluye validación de entradas no numéricas y un ciclo que permite realizar varias operaciones sin reiniciar el programa.

## Estructura del proyecto

```
Calculadora/
├── README.md
├── calculadora.py    # Menú, entrada de datos y resultados
└── operaciones.py    # Funciones matemáticas
```

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/pabloalonzo-cloud/Calculadora.git
cd Calculadora
```

2. Ejecutar el programa (requiere Python 3):

```bash
python calculadora.py
```

3. Elegir una opción del menú, introducir los valores y leer el resultado. Para terminar, elegir `0`.

## Ejemplos de uso

**Potencia (opción 5):**

```
Elige una opción: 5
Base: 2
Exponente: -2
Resultado: 2 ^ -2 = 0.25
```

**Porcentaje (opción 8):**

```
Elige una opción: 8
Porcentaje: 15
Cantidad: 200
Resultado: 15% de 200 = 30
```

**Factorial (opción 10):**

```
Elige una opción: 10
Número: 5
Resultado: 5! = 120
```

**Promedio (opción 11):**

```
Elige una opción: 11
¿Cuántos números? 3
Número 1: 2
Número 2: 4
Número 3: 6
Resultado: promedio = 4
```

**Redondeo (opción 12):**

```
Elige una opción: 12
Valor: 3.14159
Decimales: 2
Resultado: redondeo(3.14159, 2) = 3.14
```

**Manejo de errores:**

```
Elige una opción: 4
Primer número: 10
Segundo número: 0
Error: No se puede dividir entre cero.
```

```
Elige una opción: 7
Número: -4
Error: No existe la raíz cuadrada de un número negativo.
```

**Historial (opciones 13 y 14):**

```
Elige una opción: 13

--- HISTORIAL ---
1. 2 ^ -2 = 0.25
2. 15% de 200 = 30
```

## Tecnologías

- **Python 3**
- **Git** y **GitBash**
- **GitHub** (repositorio e Issues)
- **Markdown**
- **Visual Studio Code**

## Autor

**Pablo Ernesto Alonzo Magne**