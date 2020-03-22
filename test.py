a = []
b = []
for i in range(3):
    a.append(1)
for j in range(3):
    b.append(a)
print(b)

for i in b:
    v = 0
    for j in i:
        v +=j
print(v)
        

