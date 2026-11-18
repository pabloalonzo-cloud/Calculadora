import math

from operaciones import (
    suma, resta, multiplicacion, division, potencia, modulo,
    raiz_cuadrada, porcentaje, valor_absoluto, factorial,
    promedio, redondear,
)


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


def formato(n):
    if isinstance(n, float) and math.isfinite(n) and n == int(n):
        return str(int(n))
    return str(n)


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print(" 1. Suma")
    print(" 2. Resta")
    print(" 3. Multiplicación")
    print(" 4. División")
    print(" 5. Potencia")
    print(" 6. Módulo")
    print(" 7. Raíz cuadrada")
    print(" 8. Porcentaje")
    print(" 9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    print("13. Ver historial")
    print("14. Limpiar historial")
    print(" 0. Salir")


def pedir_dos_numeros():
    a = leer_numero("Primer número: ")
    b = leer_numero("Segundo número: ")
    return a, b


def ejecutar_operacion(opcion):
    if opcion == "1":
        a, b = pedir_dos_numeros()
        return f"{formato(a)} + {formato(b)}", suma(a, b)
    if opcion == "2":
        a, b = pedir_dos_numeros()
        return f"{formato(a)} - {formato(b)}", resta(a, b)
    if opcion == "3":
        a, b = pedir_dos_numeros()
        return f"{formato(a)} * {formato(b)}", multiplicacion(a, b)
    if opcion == "4":
        a, b = pedir_dos_numeros()
        return f"{formato(a)} / {formato(b)}", division(a, b)
    if opcion == "5":
        base = leer_numero("Base: ")
        exponente = leer_numero("Exponente: ")
        return f"{formato(base)} ^ {formato(exponente)}", potencia(base, exponente)
    if opcion == "6":
        a, b = pedir_dos_numeros()
        return f"{formato(a)} % {formato(b)}", modulo(a, b)
    if opcion == "7":
        n = leer_numero("Número: ")
        return f"raíz({formato(n)})", raiz_cuadrada(n)
    if opcion == "8":
        p = leer_numero("Porcentaje: ")
        c = leer_numero("Cantidad: ")
        return f"{formato(p)}% de {formato(c)}", porcentaje(p, c)
    if opcion == "9":
        n = leer_numero("Número: ")
        return f"|{formato(n)}|", valor_absoluto(n)
    if opcion == "10":
        n = leer_numero("Número: ")
        return f"{formato(n)}!", factorial(n)
    if opcion == "11":
        cantidad = leer_entero("¿Cuántos números? ")
        numeros = [leer_numero(f"Número {i + 1}: ") for i in range(cantidad)]
        return "promedio", promedio(numeros)
    if opcion == "12":
        valor = leer_numero("Valor: ")
        decimales = leer_entero("Decimales: ")
        return f"redondeo({formato(valor)}, {decimales})", redondear(valor, decimales)
    raise ValueError("Opción no válida. Elige un número del menú.")


def mostrar_historial(historial):
    print("\n--- HISTORIAL ---")
    if not historial:
        print("El historial está vacío.")
        return
    for i, registro in enumerate(historial, start=1):
        print(f"{i}. {registro}")


def limpiar_historial(historial):
    historial.clear()
    print("Historial borrado.")


def main():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        if opcion == "13":
            mostrar_historial(historial)
            continue
        if opcion == "14":
            limpiar_historial(historial)
            continue
        try:
            descripcion, resultado = ejecutar_operacion(opcion)
        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")
            continue
        registro = f"{descripcion} = {formato(resultado)}"
        historial.append(registro)
        print(f"Resultado: {registro}")


if __name__ == "__main__":
    main()