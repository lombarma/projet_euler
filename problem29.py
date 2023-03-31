def pb29():
    l = []
    for i in range(2, 101):
        for j in range(2, 101):
            l.append(i**j)
    return sorted(list(set(l)))

print(len(pb29()))