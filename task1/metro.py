def count_passengers(N, entries, exits, T):
    count = 0
    for entry, exit in zip(entries, exits):
        if entry <= T <= exit:
            count += 1
    return count

N = int(input())
entries = []
exits = []
for _ in range(N):
    entry, exit = map(int, input().split())
    entries.append(entry)
    exits.append(exit)
T = int(input())

print(count_passengers(N, entries, exits, T))
