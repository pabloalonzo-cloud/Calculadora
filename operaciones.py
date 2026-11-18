def suma (a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b;

def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("Cero no puede elevarse a un exponente negativo.")
    if base < 0 and exponente != int(exponente):
        raise ValueError("Una base negativa necesita un exponente entero.")
    return base ** exponente
    
def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero.")
    return a % b
    
def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No existe la raíz cuadrada de un número negativo.")
    return math.sqrt(n)
    
def porcentaje(porcentaje, cantidad):
    return cantidad * porcentaje / 100

def valor_absoluto(n):
    return abs(n)
    
def factorial(n):
    if n < 0 or n != int(n):
        raise ValueError("El factorial solo se define para enteros no negativos.")
    return math.factorial(int(n))