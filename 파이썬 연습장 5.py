import random

class human:
    def __init__ (self):
        self.name = input("이름을 입력하십시오.")
        self.age = input("나이를 입력하십시오.")
        self.gender = input("성별을 입력하십시오.")
    def introduction(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살, 성별은 {self.gender}입니다.")

class mage(human):
    def __init__ (self):
        super().__init__()
        self.dorm_assign()
    def dorm_assign(self):
        self.dorm = random.choice(dorm_list)
    def introduction(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살, 성별은 {self.gender}입니다.")
        print(f"제가 배정받은 기숙사는 {self.dorm}입니다.")

dorm_list = ["그리핀도르", "래번클로", "후플푸프", "슬리데린"]

intro = mage()
intro.introduction()