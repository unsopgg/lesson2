a = input("Введите строку (слова разделяйте пробелами)")
a = a.split(' ')
max_a = a[0]
for i in range(len(a)):
    if len(a[i])>len(max_a):
        max_a = a[i]
print(max_a)