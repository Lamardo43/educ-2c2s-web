def count_substrings(s):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    n = len(s)

    for i in range(n):
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score > kevin_score:
        return "Stuart", stuart_score
    elif kevin_score > stuart_score:
        return "Kewin", kevin_score
    else:
        return "NoOne", stuart_score


s = input()
winner, score = count_substrings(s)
print(winner, score)
