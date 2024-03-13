s = input()

result = ''

for char in s:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char

print(result)
