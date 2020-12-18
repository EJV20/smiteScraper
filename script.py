import sys

from random import seed
from random import randint
import json
import request_handler as rh

from cli_handler import getDictionary


def get_args_in_dict():
    args = getDictionary(sys.argv)
    print(args)
    return args


def get_session():
    session = read_session()
    if session is None:
        print("Created Session")
        session = rh.create_session()
        write_session(session=session)
    else:
        print("Testing Session")
        code = rh.test_session(session=session)
        if str(code) != "200":
            print("Session no longer active, Created Session")
            session = rh.create_session()
            write_session(session=session)
        else:
            print("Session still active")

    return session


def handle_patches(session):
    curr_patch = rh.get_patch(session)
    patch_saved = float(0)
    with open("patch.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            patch_saved = str(lines[0].rstrip())

    if float(curr_patch) > float(patch_saved):
        with open("patch.txt", "w") as f:
            f.write(str(curr_patch))
        return True
    else:
        return False


def read_session():
    session = None
    with open("session.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 0:
            session = str(lines[0])
    
    return session


def write_session(session):
    with open("session.txt", "w") as f:
        f.write(str(session))


def get_god_data(session):
    update = handle_patches(session)
    if update:
        rh.get_gods(session)

    data = {}
    with open("gods.json", "r") as f:
        data = json.load(f)
    gods = list(data.keys())
    return gods



def get_results(args, gods):
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


def main():
    args = get_args_in_dict()
    session = get_session()
    god_data = get_god_data(session=session)

    get_results(args, god_data)


if __name__ == "__main__":
    main()
