a = ['a', 'b', 'c', 'b']

for c in range(len(a) - 1, -1, -1):
    if a.count(a[c]) > 1:
        a.pop(c)

print(a) 
