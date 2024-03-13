n = int(input())

num = 0

if 1 <= n <= 20:
    for i in range(1, n+1):
        if i > 9:
            num *= 100
        else:
            num *= 10
        num += i
    print(num)
else:
    print("Not a prime number")