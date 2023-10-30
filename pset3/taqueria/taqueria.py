def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    order("Item: ", menu)
    print()

def order(prompt, menu):
    total = 0.0
    while True:
        try:
            item = input(prompt).title()
            total = total + float(menu[item])
            print(f"${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            break

main()