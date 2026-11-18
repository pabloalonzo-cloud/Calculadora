import math

from operaciones import suma


def leer_numero(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("Error: debes escribir un número válido.")
            continue
        if not math.isfinite(numero):
            print("Error: debes escribir un número válido.")
            continue
        return numero


def leer_entero(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            return int(texto)
        except ValueError:
            print("Error: debes escribir un número entero.")


def main():
    a = leer_numero("Primer número: ")
    b = leer_numero("Segundo número: ")
    print(f"Resultado: {suma(a, b)}")


if __name__ == "__main__":
    main()