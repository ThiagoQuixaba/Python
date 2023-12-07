#Frações?:
top = 1
soma_top = 0
bottom = 1
soma_bottom = 0
while bottom < 50:
    soma_top += top
    soma_bottom += bottom
    top += 2
    bottom += 1
total = soma_top / soma_bottom
print(f"{soma_top}/{soma_bottom} ou {total}")