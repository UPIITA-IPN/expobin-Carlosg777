def exponenciacion_binaria(base, exponente, modulo):
    """
    Calcula (base^exponente) % modulo usando el método de exponenciación binaria.
    
    Argumentos:
        base (int): La base
        exponente (int): El exponente (no negativo)
        modulo (int): El módulo (debe ser > 0)
    
    Retorna:
        int: Resultado de (base^exponente) % modulo
    """
    # Inicializamos el resultado
    resultado = 1
    
    # Reducimos la base módulo para trabajar con números más pequeños
    base = base % modulo
    
    # Mientras el exponente no sea cero
    while exponente > 0:
        # Si el bit menos significativo del exponente es 1
        if exponente & 1:  # equivalente a exponente % 2 == 1
            # Multiplicamos el resultado por la base actual y reducimos módulo
            resultado = (resultado * base) % modulo
        
        # Elevamos la base al cuadrado y reducimos módulo
        base = (base * base) % modulo
        
        # Desplazamos el exponente un bit a la derecha (dividimos entre 2)
        exponente >>= 1  # equivalente a exponente = exponente // 2
    
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo del profesor
    base = 2
    exp = 1234
    mod = 789
    resultado = exponenciacion_binaria(base, exp, mod)
    print(f"{base}^{exp} mod {mod} = {resultado}")
    
    # Otro ejemplo
    base2, exp2, mod2 = 5, 17, 23
    resultado2 = exponenciacion_binaria(base2, exp2, mod2)
    print(f"{base2}^{exp2} mod {mod2} = {resultado2}")