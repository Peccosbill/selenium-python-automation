a = [5, 8, 2, 1, 10, 25, 32, 45, 3, 8, 13, 7]

for i in range(1, len(a)):
    for j in range(0, len(a)-i):
        if a[j] > a[j+1]:
            temportal = a[j]
            a[j] = a[j+1]
            a[j+1] = temportal
        print(a)

print(a)

