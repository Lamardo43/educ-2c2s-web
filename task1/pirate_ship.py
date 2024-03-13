n, m = map(int, input().split())

cargo = []
for _ in range(m):
    name, weight, value = input().split()
    weight, value = int(weight), int(value)
    cargo.append((name, weight, value))

cargo.sort(key=lambda x: x[2], reverse=True)

total_weight = 0
for name, weight, value in cargo:
    if total_weight + weight <= n:
        print(f"{name} {weight} {value}")
        total_weight += weight
    else:
        remaining_weight = n - total_weight
        fraction = remaining_weight / weight
        fraction_value = round(fraction * value, 2)
        print(f"{name} {remaining_weight} {fraction_value}")
        break
