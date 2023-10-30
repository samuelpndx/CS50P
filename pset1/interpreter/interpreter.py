x, y, z = input("Expression: ").split(" ")

match y:
    case "+":
        sum = int(x) + int(z)
        print(f"{sum:.1f}")
    case "-":
        sum = int(x) - int(z)
        print(f"{sum:.1f}")
    case "*":
        sum = int(x) * int(z)
        print(f"{sum:.1f}")
    case "/":
        sum = int(x) / int(z)
        print(f"{sum:.1f}")
