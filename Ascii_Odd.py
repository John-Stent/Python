from collections import Counter

S = 0
with open("./two_cities_ascii.txt") as f:
    c = Counter()
    for line in f:
        c += Counter(line)  # Counting the times each character Appears
c = dict(c)

for i in c:
    S = S+c[i]  # Summing all characters

c.update((x, round(y/S * 100)) for x, y in c.items()) # Calculating Percentage

for (x, y) in c.items():
    if ord(x) % 2 != 0 and y >= 1:
        a = y * "*"
        print(x, ":", a)
