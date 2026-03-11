import sys

def exponenciacion_binaria(base, exponente, modulo):
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if exponente & 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        exponente >>= 1
    return resultado

if __name__ == "__main__":
    entrada = sys.stdin.read().split()
    
    if len(entrada) >= 3:
        try:
            b = int(entrada[0])
            e = int(entrada[1])
            m = int(entrada[2])
            
            print(exponenciacion_binaria(b, e, m))
        except ValueError:
            pass