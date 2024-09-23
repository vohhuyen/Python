import json

def manage_student_scores():
    student_scores = {}

    while True:
        name = input("Nhập tên học sinh (hoặc 'dừng' để kết thúc): ")
        if name.lower() == 'dừng':
            break
        score = float(input(f"Nhập điểm số cho {name}: "))
        student_scores[name] = score

    average_score = sum(student_scores.values()) / len(student_scores) if student_scores else 0
    print(f"Điểm trung bình: {average_score:.2f}")

    highest_scorer = max(student_scores, key=student_scores.get, default="Không có học sinh nào")
    highest_score = student_scores.get(highest_scorer, 0)
    print(f"Học sinh có điểm cao nhất: {highest_scorer} với điểm {highest_score}")

    with open('student_scores.json', 'w') as file:
        json.dump(student_scores, file)
    print("Dữ liệu đã được lưu vào file 'student_scores.json'.")

manage_student_scores()
