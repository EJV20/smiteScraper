import sys

from random import seed
from random import randint
import json

from cli_handler import getDictionary


args = getDictionary(sys.argv)
print(args)

data = {}
with open("gods.json", "r") as f:
    data = json.load(f)
gods = list(data.keys())

godTeam = []
if "num" in args:
    num_team = int(args["num"])
    i = 0
    while i < num_team:
        seed()
        x = randint(0, len(gods) - 1)
        newGod = gods[x]
        if newGod not in godTeam:
            godTeam.append(newGod)
            i += 1
else:
    seed()
    x = randint(0, len(gods) - 1)
    godTeam.append(gods[x])


for gt in godTeam:
    print(gt)
