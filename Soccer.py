# a. After the first 10 kicks (5 kicks per team)
def count_score_first_10_penalties():
    scores = set()
    for a in range(6):        
        for b in range(6):    
            scores.add((a, b))
    return len(scores)

# b. After 20 kicks (10 kicks per team)
def count_score_first_20_penalties():
    scores = set()
    for a in range(11):       
        for b in range(11):   
            scores.add((a, b))
    return len(scores)

# c. Outcomes under the "sudden death" law
def count_sudden_death_scores():
    sudden_death_scores = set()
    for round in range(1, 6):  
        sudden_death_scores.add(f"Round {round}: A score, B no score (1-0)")
        sudden_death_scores.add(f"Round {round}: B score, A no score (0-1)")
    return len(sudden_death_scores), sudden_death_scores

a = count_score_first_10_penalties()
b = count_score_first_20_penalties()
c_count, c_details = count_sudden_death_scores()

print("Different scores after first 10 balls:", a)
print("Different scores after 20 balls:", b)
print("Different ending numbers according to sudden death law:", c_count)
print("Details of sudden death law situations:")
for detail in c_details:
    print(" -", detail)