def takefirst(elem):
    return elem[0]

values = {}
for _ in range(int(input())):
    k = input().split()
    a, b, c = k[0], k[1], int(k[2])
    if a not in values:
        values.setdefault(a, {b:c})
    elif a in values and b not in values[a]:
        values[a].update({b:c})
    else:
        values[a][b] = values[a][b]+c

sorted_values = dict(sorted(values.items()))
for i in sorted_values:
    sorted_values[i] = dict(sorted(sorted_values[i].items()))

for i in sorted_values:
    print(i+':')
    for k in sorted_values[i]:
        print(k, sorted_values[i][k])

