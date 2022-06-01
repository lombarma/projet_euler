from string import ascii_lowercase

filename = "names.txt"

d = dict()

for index, letter in enumerate(ascii_lowercase):
    d[letter] = index + 1

data = []
lower_data = []
with open(filename, mode='r', encoding='utf-8') as file:
    f = file.read()
    for i in f.split(","):
        data.append(i[1:len(i) - 1])
for i in data:
    lower_data.append(i.lower())

lower_data = sorted(lower_data)
"""print(lower_data[937])  # prénom# colin a la 938
for i in lower_data[937]:
    print(d[i])"""

total_score = 0
unique_sum = 0
unique_pos = 0

for index, name in enumerate(lower_data):  # index = position
    for i in name :
        unique_sum = d[i]
        unique_pos = index + 1
        total_score += unique_sum*unique_pos
print(total_score)






