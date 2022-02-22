print("Hasta que numero quieres hacer la secuencia de Fibonacci?")
n=int(input())
print("Comienza la secuencia")
n1=0
n2=1
n3=1
while(n3<n):
    print(n3)
    n3=n1+n2
    n1=n2
    n2=n3