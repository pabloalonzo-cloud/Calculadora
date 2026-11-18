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