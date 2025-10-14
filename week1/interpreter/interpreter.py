expression = input("Expression: ")

nb1, symbol, nb2 = expression.split(" ")

x = int(nb1)
z = int(nb2)

if symbol == "+":
    result = x + z
elif symbol == "-":
    result = x - z
elif symbol == "*":
    result = x * z
elif symbol == "/":
    result = x / z

print(f"{result:.1f}")
