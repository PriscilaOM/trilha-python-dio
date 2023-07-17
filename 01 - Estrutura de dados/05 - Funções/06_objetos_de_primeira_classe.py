def somar(a, b):
    return a + b

def multiplicar(a,b):
    return a * b

def subtrair(a,b):
    return a - b

def dividir(a,b):
    return a / b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10,2,multiplicar)
exibir_resultado(5,2,subtrair)
#função chamando função

op = somar

print(op(1,23))
