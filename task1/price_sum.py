with open('products.csv', 'r') as file:
    lines = file.readlines()

adult_total = 0
pensioner_total = 0
child_total = 0

for line in lines[1:]:
    parts = line.strip().split(',')

    adult_total += float(parts[1])
    pensioner_total += float(parts[2])
    child_total += float(parts[3])

print(f"{adult_total:.2f} {pensioner_total:.2f} {child_total:.2f}")
