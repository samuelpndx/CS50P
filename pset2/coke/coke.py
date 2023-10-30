def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = insert_coin()
        amount_due = update_amount(amount_due, coin)

def is_valid(coin):
    match coin:
        case 5 | 10 | 25:
            return True
        case _:
            return False

def insert_coin():
    coin = int(input("Insert Coin: "))
    if is_valid(coin):
        return coin
    else:
        return 0

def update_amount(amount, coin):
    amount -= coin
    if amount > 0:
        return amount
    else:
        print("Change Owed:", abs(amount))
        return 0

main()