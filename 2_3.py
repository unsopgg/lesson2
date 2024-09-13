c = input("Введите строку: ")
zn = input("Введите знак: ")
c = c.split(zn)
min_c = c[0]
for i in range(len(c)):
    if len(c[i])<len(min_c):
        min_c = c[i]
print(min_c)