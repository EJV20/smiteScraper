import json

with open('god.json') as f:
    data = json.load(f)

gods = []
with open('godList.txt') as f1:
    lines = f1.readlines()
    for line in lines:
        gods.append(line.rstrip())

i = 0
while i < len(gods):
    print(data["gods"][i])
    i += 1