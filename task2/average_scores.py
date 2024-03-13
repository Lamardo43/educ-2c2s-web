def compute_average_scores(scores):
    num_students = len(scores[0])
    averages = []
    for student in range(num_students):
        total_score = sum(scores[subject][student] for subject in range(len(scores)))
        average_score = total_score / len(scores)
        averages.append(average_score)
    return tuple(averages)


if __name__ == "__main__":
    N, X = map(int, input().split())
    scores = []
    for _ in range(X):
        scores.append(list(map(float, input().split())))

    average_scores = compute_average_scores(scores)
    for average in average_scores:
        print("{:.1f}".format(average))
