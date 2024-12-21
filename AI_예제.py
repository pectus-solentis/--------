import json
import os

class FileManager:
    def __init__(self, file_path="db.json"):
        self.file_path = file_path

    def load_data(self):
        if os.path.isfile(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    return dict(sorted(json.load(file).items()))
            except json.JSONDecodeError as error:
                print(f"Error reading JSON file: {error}")
        return {}

    def save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

class Validator:
    @staticmethod
    def is_all_korean(text):
        return all('\uAC00' <= char <= '\uD7A3' for char in text)

    @staticmethod
    def is_numeric(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def validate_student_id(student_id):
        return len(student_id) == 5 and student_id.isdigit()

class InputHandler:    
    @staticmethod
    def get_student_id():
        while True:
            student_id = input("점수를 입력할 학생의 학번을 입력하십시오: ")
            if Validator.validate_student_id(student_id):
                return student_id
            print("학번은 5자리 숫자여야 합니다.")

    @staticmethod
    def get_student_name():
        while True:
            student_name = input("입력할 학생의 이름을 한글로만 입력하십시오: ")
            if Validator.is_all_korean(student_name):
                return student_name
            print("입력하신 값에 한글 외의 문자가 포함되어 있습니다.")

    def student_identifier(self):
        student_id = self.get_student_id()
        student_name = self.get_student_name()

        return f"{student_id} {student_name}"

    @staticmethod
    def get_scores():
        subjects = ["국어", "영어", "수학", "사회", "과학"]
        scores = {}
        for subject in subjects:
            while True:
                score = input(f"{subject} 점수를 입력하십시오: ")
                if Validator.is_numeric(score):
                    score = float(score)
                    if 0 <= score <= 100:
                        scores[subject] = score
                        break
                print(f"{subject} 점수는 0에서 100 사이여야 합니다.")
        return scores

class Calculator:
    @staticmethod
    def calculate_max(scores):
        return max(scores, key=scores.get)

    @staticmethod
    def calculate_min(scores):
        return min(scores, key=scores.get)

    @staticmethod
    def calculate_average(scores):
        return sum(scores.values()) / len(scores)

class StudentDatabaseHandler:
    inputHandler = InputHandler()
    
    def __init__(self):
        self.file_manager = FileManager()
        self.student_and_scores = self.file_manager.load_data()

    def add_student(self):
        student = self.inputHandler.student_identifier()
        scores = self.inputHandler.get_scores()
        self.student_and_scores[student] = scores
        self.file_manager.save_data(self.student_and_scores)

    def view_student(self):
        student = self.inputHandler.student_identifier()
        if student in self.student_and_scores:
            self.print_student_scores(student, self.student_and_scores[student])
        else:
            print("데이터베이스에 해당 학생이 없습니다.")

    def list_students(self):
        print("이 데이터베이스에 저장된 학생들의 목록입니다.")
        for student in self.student_and_scores:
            print(student)

    def print_student_scores(self, student, scores):
        print(f"{student} 학생의 과목별 점수는 다음과 같습니다.")
        for subject, score in scores.items():
            print(f"{subject}: {score}")
        max_subject = Calculator.calculate_max(scores)
        min_subject = Calculator.calculate_min(scores)
        avg_score = Calculator.calculate_average(scores)
        print(f"최고점수: {scores[max_subject]} ({max_subject})")
        print(f"최저점수: {scores[min_subject]} ({min_subject})")
        print(f"평균점수: {round(avg_score, 2)}")

def main():
    handler = StudentDatabaseHandler()
    while True:
        action = input("입력 / 조회 / 목록 / 종료 중 하나를 선택하십시오: ").strip()
        if action == "입력":
            handler.add_student()
        elif action == "조회":
            handler.view_student()
        elif action == "목록":
            handler.list_students()
        elif action == "종료":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하십시오.")

if __name__ == "__main__":
    main()
