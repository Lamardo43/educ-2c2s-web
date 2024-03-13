n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

mood = 0
for num in arr:
    if num in set_A:
        mood += 1
    elif num in set_B:
        mood -= 1

print(mood)
