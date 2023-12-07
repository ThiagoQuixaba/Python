#Ordem crescente:
A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))
if A <= B:
    print(A, B)
else:
    C = A
    A = B
    B = C
    print(A, B)