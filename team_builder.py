from random import seed
from random import randint

def filter_on_panth(panth, g):
    gods = list(g.keys())
    d = {}
    for god in gods:
        if str(g[god]["Pantheon"]).lower() == str(panth).lower():
            d[god] = god
    
    return d



def get_results(args, gods):
    godTeam = []

    if "panth" in args:
        pantheon = args["panth"]
        gods = filter_on_panth(panth=pantheon, g=gods)

    gods = list(gods.keys())

    if len(gods) < int(args["num"]):
        args["num"] = len(gods)

    print("\n Team is \n")
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