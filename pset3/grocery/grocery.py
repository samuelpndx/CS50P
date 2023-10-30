def main():
    grocery_list = make_list()

    print()

    keys = list(grocery_list.keys())
    keys.sort()

    for i in keys:
        print(f"{grocery_list[i]} {i}")


def make_list():
    items = {}
    while True:
        try:
            item = input().upper()
            items[item] += 1
        except KeyError:
            items[item] = 1
        except EOFError:
            return items

main()