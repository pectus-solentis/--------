student_no = input("점수를 입력할 학생의 학번을 입력하십시오.")
student_name = input("점수를 입력할 학생의 이름을 입력하십시오.")
student = student_no + " " + student_name
score_kor = int(input("학생의 국어 점수를 입력하십시오.") or -1)
while score_kor < 0 or score_kor > 100:
	print("국어 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")
	score_kor = int(input("학생의 국어 점수를 입력하십시오.") or -1)
	if 0 <= score_kor <= 100:
		break	
score_eng = int(input("학생의 영어 점수를 입력하십시오.") or -1)
while score_eng < 0 or score_eng > 100:
	print("영어 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")
	score_eng = int(input("학생의 영어 점수를 입력하십시오.") or -1)
	if 0 <= score_eng <= 100:
		break	
score_math = int(input("학생의 수학 점수를 입력하십시오.") or -1)
while score_math < 0 or score_math > 100:
	print("수학 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")
	score_math = int(input("학생의 수학 점수를 입력하십시오.") or -1)
	if 0 <= score_math <= 100:
		break	
score_soc = int(input("학생의 사회 점수를 입력하십시오.") or -1)
while score_soc < 0 or score_soc > 100:
	print("사회 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")
	score_soc = int(input("학생의 사회 점수를 입력하십시오.") or -1)
	if 0 <= score_soc <= 100:
		break	
score_sci = int(input("학생의 과학 점수를 입력하십시오."  )or -1)
while score_sci < 0 or score_sci > 100:
	print("과학 과목 점수는 0 ~ 100 사이의 값을 가져야 합니다.")
	score_sci = int(input("학생의 과학 점수를 입력하십시오.") or -1)
	if 0 <= score_sci <= 100:
		break	
#학생의 학번과 이름, 과목별 점수 받기
score = {"국어":score_kor,"영어":score_eng,"수학":score_math,"사회":score_soc,"과학":score_sci}
students_and_score = {student:score}
#2차원 딕셔너리에 저장

student_search_no = input("조회할 학생의 학번을 입력하십시오.")
student_search_name = input("조회할 학생의 이름을 입력하십시오.")
student_search = student_search_no + " " + student_search_name
confirm = f"{student_search} 학생의 과목별 점수는 다음과 같습니다."
if student_search in students_and_score:
	student_to_view = students_and_score[student_search]
	print(confirm)
	print(student_to_view)
#조회할 학생의 이름과 점수가 담긴 딕셔너리 호출
	max = max(student_to_view.values())
	min = min(student_to_view.values())
#입력한 학생의 최고점수와 최저점수 얻기
	score_max = {}
	score_min = {}
	for key, value in student_to_view.items():
		if value == max:
			score_max = {key:value}
	for key, value in student_to_view.items():
		if value == min:
			score_min = {key:value}
#최고점, 최저점과 과목명을 각각 값, 키로 하는 딕셔너리 생성 
	average = 0
	average = sum(student_to_view.values()) / len(student_to_view)
	score_average = {"평균점수" : average}
#평균점수 구하기
	print("최고점수를 얻은 과목과 그 점수는 다음과 같습니다.")
	print(score_max)
	print("최저점수를 얻은 과목과 그 점수는 다음과 같습니다.")
	print(score_min)
	print("평균점수는 다음과 같습니다.")
	print(score_average)
#최고점, 최저점, 평균점수 출력
else:
	print("데이터베이스에 입력되지 않은 학생입니다. 학번과 이름을 확인해보세요.")
#예외처리 : 데이터베이스에 입력되지 않은 학생을 검색했을 경우