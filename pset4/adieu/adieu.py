import inflect

p = inflect.engine()
mylist = []
while True:
    try:
        mylist.append(input("Name: "))
    except EOFError:
        break

print("\nAdieu, adieu, to", p.join(mylist))
