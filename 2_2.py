b = input("Введите строку (слова разделяйте пробелами)")
b = b.split(';')
max_b = b[0]
for i in range(len(b)):
    if len(b[i])>len(max_b):
        max_b = b[i]
print(max_b)