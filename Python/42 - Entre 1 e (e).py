#Entre 1 e "e":
e = int(input("Insira valor de E: "))
if e <= 0:
    x = -1
else:
    x = 1
for timer in range (1, e + x, x):
    if timer % 2 == 0:
        print(timer)
