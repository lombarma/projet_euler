import inflect
p = inflect.engine()
def lenOfWord(n: int):
    s = p.number_to_words(n)
    return len(s.replace(" ", "").replace("-", ""))

cpt=0
for i in range(1, 1001):
    cpt+=lenOfWord(i)
print(cpt)

