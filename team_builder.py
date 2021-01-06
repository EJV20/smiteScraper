from random import seed
from random import randint

def filter_on_panth(panth, g):
    gods = list(g.keys())
    d = {}
    for god in gods:
        if str(g[god]["Pantheon"]).lower() == str(panth).lower():
            d[god] = god
    
    return d
    

def get_num(args):
    if "num" in args:
        return int(args["num"])
        
    return 5



def get_results(args, gods):
    godTeam = []
    
    num = get_num(args)

    if "panth" in args:
        pantheon = args["panth"]
        gods = filter_on_panth(panth=pantheon, g=gods)

    gods = list(gods.keys())

    if len(gods) < num:
        num = len(gods)

    print("\n Team is \n")
    i = 0
    while i < num:
        seed()
        x = randint(0, len(gods) - 1)
        newGod = gods[x]
        if newGod not in godTeam:
            godTeam.append(newGod)
            i += 1

    for gt in godTeam:
        print(gt)
        
    return gt