def suma(a, b):
    return a + b


def resta(*, minuendo, sustraendo):
    return minuendo - sustraendo


def precio_final(precio, iva=21):
    return precio * (1 + iva / 100)


def convertir_metros(metros, unidad="cm"):
    if unidad == "mm":
        return metros * 1000
    return metros * 100


def area_rectangulo(base, altura=None):
    if altura is None:
        altura = base
    return base * altura
