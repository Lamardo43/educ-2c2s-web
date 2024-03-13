def check_weirdness(n):
    if 1 <= n <= 100:
        if n % 2 != 0:
            return "Weird"
        else:
            if 2 <= n <= 5:
                return "Not Weird"
            elif 6 <= n <= 20:
                return "Weird"
            else:
                return "Not Weird"
    else:
        return "Not"


n = int(input())

print(check_weirdness(n))
