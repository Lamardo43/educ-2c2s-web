with open('example.txt', 'r', encoding="utf-8") as file:
    text = file.read()

words = text.split()

max_length = max(len(word.strip(",.!?")) for word in words)

max_length_words = [word.strip(",.!?") for word in words if len(word.strip(",.!?")) == max_length]

for word in max_length_words:
    print(word)
