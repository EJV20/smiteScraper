help_val = """
Help Page

num=<number of random gods to get>
"""


def getDictionary(args):
    d = {}
    for arg in args:
        if "=" in arg:
            key_val = arg.split("=")
            key = key_val[0].lower()
            val = key_val[1].lower()
            if d.get(key) is not None:
                current_val = d.get(key)
                if type(current_val) is list:
                    d[key] = current_val.append(val)
                else:
                    new_list = [d[key], val]
                    d[key] = new_list
            else:
                d[key] = val

        if arg == "-h":
            print(help_val)

    return d
