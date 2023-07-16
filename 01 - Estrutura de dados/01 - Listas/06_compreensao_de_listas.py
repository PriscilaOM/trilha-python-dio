# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
#1°parte retorno 2°parte e a iteração 3° parte if

print(pares)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)    
    
# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)


for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)
