import json
import os

def is_all_korean(text):
	for char in text:
		if not ('\uAC00' <= char <= '\uD7A3'):
			return False
	return True
#입력된 텍스트가 한글로만 구성되어 있는지 검사하는 함수

def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#입력된 텍스트가 숫자로만 구성되어 있는지 검사하는 함수

class StudentDatabase:
    def __init__(self, filename="db.json"):
        self.filename = filename
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.isfile(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
                    self.students = dict(sorted(self.students.items()))
            except json.JSONDecodeError:
                self.students = {}
        else:
            self.students = {}
    
    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.students, f, indent=4, ensure_ascii=False)

    def add_student(self, student, scores):
        self.students[student] = scores
        self.students = dict(sorted(self.students.items()))
        self.save_data()

    def get_student_data(self, student_search):
        return self.students.get(student_search)
    
def student_id_input():
    student_id = input("점수를 입력할 학생의 학번을 입력하십시오.")
    return student_id
    #학생의 학번 받기

def student_id_try(student_id):
    student_grade = int(student_id[0:1])
    student_class = int(student_id[1:3])
    student_no = int(student_id[3:5])
    while True:
        if not len(student_id) == 5:
            print("학번은 5자리 숫자여야 합니다.")
        else: break
    while student_grade < 1 or student_grade > 3:
        print("학년은 1부터 3까지의 값을 가져야 합니다.")
        student_grade = int(input("점수를 입력할 학생의 학년을 입력하십시오."))
    while student_class < 1 or student_class > 20:
        print("학급은 1부터 20까지의 값을 가져야 합니다.")
        student_class = int(input("점수를 입력할 학생의 학급을 입력하십시오."))
    while student_no < 1 or student_no > 40:
        print("학생 번호는 1부터 40까지의 값을 가져야 합니다.")
        student_no = int(input("점수를 입력할 학생의 번호를 입력하십시오."))
    print(student_grade, student_class, student_no)
    return student_grade, student_class, student_no
        
def student_id_create(student_grade, student_class, student_no):
    student_grade_str = str(student_grade).zfill(1)
    student_class_str = str(student_class).zfill(2)
    student_no_str = str(student_no).zfill(2)
    student_id_checked = student_grade_str + student_class_str + student_no_str
    return student_id_checked

def student_name_input():
    while True:
        student_name = input("입력할 학생의 이름을 한글로만 입력하십시오.")
        if not is_all_korean(student_name):
            print("입력하신 값에 한글 외의 문자가 포함되어 있습니다.")
        else: break
    return student_name
    #학생의 이름 받기 및 예외처리

def student_identifier(student_id_checked, student_name):
    student = student_id_checked + " " + student_name
    #학생 식별자 (학번 + 이름) 만들기
    return student

def scores_input():
    def get_score(subject):
        while True:
            pre_score = input(f"학생의 {subject} 점수를 입력하십시오.")
            if isNumeric(pre_score):
                score = float(pre_score)
                if 0 <= score <= 100:
                    return score
            print(f"{subject} 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")   
    subjects = ["국어", "영어", "수학", "사회", "과학"]
    scores = {}	
    for subject in subjects:
        scores[subject] = get_score(subject)
    return scores
    #학생의 과목별 점수 받기 및 예외처리

def student_data():
	while True:
		student_search_id = input("조회할 학생의 학번을 입력하십시오.")
		if not len(student_search_id) == 5:
			print("학번은 5자리 숫자여야 합니다.")
		else: break
	while True:
		student_search_name = input("조회할 학생의 이름을 한글로만 입력하십시오.")
		if not is_all_korean(student_search_name):
			print("입력하신 값에 한글 외의 문자가 포함되어 있습니다.")
		else: break
	student_search = student_search_id + " " + student_search_name
	if student_search in student_and_scores:
		confirm = f"{student_search} 학생의 과목별 점수는 다음과 같습니다."
		student_to_view = student_and_scores[student_search]
		print(confirm)
		print(student_to_view)
	#조회할 학생의 이름과 점수가 담긴 딕셔너리 호출
		max_temp = max(student_to_view.values())
		min_temp = min(student_to_view.values())
	#입력한 학생의 최고점수와 최저점수 얻기
		subject_max = []
		for key, value in student_to_view.items():
			if value == max_temp:
				subject_max.append(key)
		subject_max.append(max_temp)
		subject_min = []
		for key, value in student_to_view.items():
			if value == min_temp:
				subject_min.append(key)
		subject_min.append(min_temp)
	#최고점, 최저점과 과목명을 각각 값, 키로 하는 딕셔너리 생성 
		average = sum(student_to_view.values()) / len(student_to_view)
		score_average = {"평균점수" : round(average,2)}
	#평균점수 구하기
		print("최고점수를 얻은 과목과 그 점수는 다음과 같습니다.")
		print(subject_max)
		print("최저점수를 얻은 과목과 그 점수는 다음과 같습니다.")
		print(subject_min)
		print("평균점수는 소수점 2째 자리까지 반올림해서 다음과 같습니다.")
		print(score_average)
	#최고점, 최저점, 평균점수 출력
	else:
		print("데이터베이스에 입력되지 않은 학생입니다. 학번과 이름을 확인해보세요.")
	#예외처리 : 데이터베이스에 입력되지 않은 학생을 검색했을 경우

db = StudentDatabase()

start = ""
while start == "":
	print("학생의 데이터를 입력하시겠습니까, 입력된 데이터를 조회하시겠습니까? 입력된 학생들의 목록을 보시겠습니까?")
	start = input("입력 / 조회 / 목록 / 종료 로 답변하십시오.")
	if start == "입력":
		db.add_student(student, scores)
		start = ""  
	elif start == "조회":
		student_data = db.get_student_data(student_search)
		if student_data:
			print("조회")
		else:
			print("데이터베이스에 입력되지 않은 학생입니다.")
		start = ""
	elif start == "목록":
		print("이 데이터베이스에 저장된 학생들의 목록입니다.")
		print(list(student_and_scores.keys()))
		start = ""
	elif start == "종료":
		print("프로그램을 종료합니다.")
	else:
		print("잘못된 입력입니다.")
		start = ""