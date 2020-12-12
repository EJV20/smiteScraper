import sys

from random import seed
from random import randint

from webscraper import scrape_gods, scrape_gods_plus
from cli_handler import getDictionary


args = getDictionary(sys.argv)
print(args)
gods = scrape_gods_plus()
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
