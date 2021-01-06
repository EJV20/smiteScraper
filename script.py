import sys

import json
import request_handler as rh
import team_builder as tb

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
        if "Invalid session id" in str(code):
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

    print("Curr Patch: " + str(curr_patch))
    print("Patch Saved: " + str(patch_saved))
    if float(curr_patch) > float(patch_saved):
        with open("patch.txt", "w") as f:
            f.write(str(curr_patch))
        return True
    else:
        return False


def read_session():
    session = None
    try:
        with open("session.txt", "r+") as f:
            lines = f.readlines()
            if len(lines) > 0:
                session = str(lines[0])
    except:
        return None
    
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

    return data


def main():
    args = get_args_in_dict()
    session = get_session()
    god_data = get_god_data(session=session)

    tb.get_results(args, god_data)


if __name__ == "__main__":
    main()
