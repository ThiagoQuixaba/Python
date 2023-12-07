ni = int(input("Digite o número inicial: "))
i = ni
k = float
nf = int(input("Digite o número final: "))
while i < nf:
    x = 0
    j = 1
    while j < i:
        k = i % j
        if k == 0:
            x = x + 1
        j = j + 1    
    if x == 1:
        print(i)
    i = i + 1    