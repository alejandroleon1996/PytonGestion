numeros = [19, 7, 99, 24, 54, 88, 58]
for i in range(len(numeros)):
    for j in range(len(numeros) - i-1):
        if numeros[j] > numeros[j+1]:
            numeros[j],numeros[j+1]=numeros[j+1], numeros[j]
print(numeros)