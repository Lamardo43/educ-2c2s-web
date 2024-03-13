n = int(input())
students = [[input(), float(input())] for _ in range(n)]

second_highest_score = sorted(set(score for name, score in students))[1]

second_highest_students = sorted(name for name, score in students if score == second_highest_score)

for student in second_highest_students:
    print(student)
