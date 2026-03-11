import sys

def exponenciacion_binaria(base, exponente, modulo):
    """
    Calcula (base^exponente) % modulo usando el método de exponenciación binaria.
    """
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if exponente & 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        exponente >>= 1
    return resultado

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        try:
            b = int(sys.argv[1])
            e = int(sys.argv[2])
            m = int(sys.argv[3])
            print(exponenciacion_binaria(b, e, m))
        except ValueError:
            pass