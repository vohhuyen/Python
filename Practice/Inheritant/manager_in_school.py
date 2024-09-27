class Personal:
    def __init__(self, name, gender, dayofbirth, address):
        self.name = name
        self.gender = gender
        self.dayofbirth = dayofbirth
        self.address = address
    
    def input_info(self):
        self.name = input("Enter your name: ")
        self.gender = input("Enter your gender: ")
        self.dayofbirth = input("Enter your date of birth (YYYY-MM-DD): ")
        self.address = input("Enter your address: ")
    
    def __str__(self):
        return (f"Personal name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Birthday: {self.dayofbirth}\n"
                f"Address: {self.address}")

class Student(Personal):
    def __init__(self, name, gender, dayofbirth, address, id_student, score, email):
        super().__init__(name, gender, dayofbirth, address)
        self.set_student_id(id_student)
        self.set_grade(score)
        self.set_email(email)

    def set_student_id(self, student_id: str):
        if len(student_id) != 8:
            raise ValueError("Mã sinh viên phải chứa 8 ký tự.")
        self.id_student = student_id

    def set_grade(self, grade: float):
        if 0 <= grade <= 10:
            self.score = grade
        else:
            raise ValueError("Điểm phải từ 0 đến 10.")

    def set_email(self, email: str):
        if '@' not in email or ' ' in email:
            raise ValueError("Email phải chứa '@' và không có khoảng trắng.")
        self.email = email

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Student ID: {self.id_student}\n"
                f"Score: {self.score}\n"
                f"Email: {self.email}")

class Teacher(Personal):
    def __init__(self, name, gender, dayofbirth, address, id_teacher, salary, email):
        super().__init__(name, gender, dayofbirth, address)
        self.set_teacher_id(id_teacher)
        self.set_salary(salary)
        self.set_email(email)

    def set_teacher_id(self, teacher_id: str):
        if len(teacher_id) != 8:
            raise ValueError("Mã giáo viên phải chứa 8 ký tự.")
        self.id_teacher = teacher_id

    def set_salary(self, salary: float):
        if salary < 0:
            raise ValueError("Lương không được âm.")
        self.salary = salary

    def set_email(self, email: str):
        if '@' not in email or ' ' in email:
            raise ValueError("Email phải chứa '@' và không có khoảng trắng.")
        self.email = email

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Teacher ID: {self.id_teacher}\n"
                f"Salary: {self.salary}\n"
                f"Email: {self.email}")


if __name__ == "__main__":
    student = Student("", "", "", "", "12345678", 9.0, "student@example.com")
    student.input_info()
    print(student) 


    teacher = Teacher("", "", "", "", "87654321", 5000.0, "teacher@example.com")
    teacher.input_info()
    print(teacher) 
