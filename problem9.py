# remove minimum element of a list
a = [5, 4, 3, 2, 1]
minimum = a[0]
for i in a:
    if i < minimum:
        minimum = i
print(minimum)
