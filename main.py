def fibonacci(numero):
    if type(numero) != int:
        raise ValueError("O número fornecido deve ser do tipo inteiro")
    elif numero < 0:
        raise ValueError("O número fornecido deve ser maior ou igual a 0")

    if numero == 0 or numero == 1:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

def fatorial(numero):
    if type(numero) != int:
        raise ValueError("O número fornecido deve ser do tipo inteiro")
    elif numero < 0:
        raise ValueError("O número fornecido deve ser maior ou igual a 0")

    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

def int_para_romano(numero):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    algarismo_romano = ''
    i = 0
    while numero > 0:
        for _ in range(numero // valores[i]):
            algarismo_romano += simbolos[i]
            numero -= valores[i]
        i += 1
    return algarismo_romano


