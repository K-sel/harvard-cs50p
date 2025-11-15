text = input("camelCase: ")

result = []
current_word = ""

for char in text:
    if char.isupper() and current_word:
        result.append(current_word)
        current_word = char
    else:
        current_word += char

if current_word:
    result.append(current_word)

sep = "_"
snake_cased = sep.join(result).lower()
print(f"snake_case: {snake_cased}")
