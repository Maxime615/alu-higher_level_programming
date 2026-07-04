#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the module, sorted alphabetically
    module_names = sorted(dir(hidden_4))

    # Print only names that do not start with "__"
    for name in module_names:
        if not name.startswith("__"):
            print("{}".format(name))
