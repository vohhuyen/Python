import json

def manage_student_scores():
    student_scores = {}

    while True:
        name = input("Enter student's name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        score = float(input(f"Enter score for {name}: "))
        student_scores[name] = score

    average_score = sum(student_scores.values()) / len(student_scores) if student_scores else 0
    print(f"Average score: {average_score:.2f}")

    highest_scorer = max(student_scores, key=student_scores.get, default="No students")
    highest_score = student_scores.get(highest_scorer, 0)
    print(f"Top scorer: {highest_scorer} with a score of {highest_score}")

    with open('student_scores.json', 'w') as file:
        json.dump(student_scores, file)
    print("Data has been saved to 'student_scores.json'.")

manage_student_scores()
