def calcular_promedios(verbales: str, numericas: str) -> int:

    verbal_skills = list(map(int, verbales.split()))
    n_skills = list(map(int, numericas.split()))
    average_score = sum(verbal_skills + n_skills) / (len(verbal_skills) + len(n_skills))
    below_average_count = 0
    for i in range(len(verbal_skills)):
        if verbal_skills[i] < average_score and n_skills[i] < average_score:
            below_average_count += 1

    return below_average_count