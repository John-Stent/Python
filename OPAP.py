import requests
import json
import datetime
from collections import Counter

d = datetime.datetime.now()
M = d.strftime("%m")

if d.hour < 9:
    D = d.day-1
else:
    D = d.day

Numbers = []
for i in range(1, D+1):
    number_str = str(i)
    A = number_str.zfill(2)
    x = requests.get('https://api.opap.gr/draws/v3.0/1100/draw-date/2021-{M}-{D}/2021-{M}-{D}/draw-id'.format(D=A, M=M))
    z = x.json()
    Z = z[0]
    X = requests.get("https://api.opap.gr/draws/v3.0/1100/{Z}".format(Z=Z))
    a = json.loads(X.text)
    winning = a["winningNumbers"]['list']
    Numbers.extend(winning)

print("The numbers from the first draw of each day of the current month are:", Numbers)
print("\nIn total there are:", len(Numbers), "Numbers\n")

g = Counter(Numbers)
y = len(Numbers) / D   # Each number can only appear 1 time per day since we count one draw of each day
G = [(i, g[i] / y * 100) for i, count in g.most_common()]

for (x, y) in G:
    print("The number {x} has {Y}% chance to appear".format(x=x, Y=y))





