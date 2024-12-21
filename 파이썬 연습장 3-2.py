import random

def start(inputted):
    while True:
        print("5자리의 정수를 입력해야 합니다.")
        inputted = input("5자리 숫자를 입력하십시오.")
        inputted_verify = inputted.isdigit()
        if inputted_verify:
            inputted_int = int(inputted)
            if 0< inputted_int < 100000:
                break
    attack = []
    for i in range(len(inputted)):
        attack.append(inputted[i])
    return attack
# 입력받은 숫자의 예외처리

to_strike = str(random.randint(10000, 99999))
shot = []
for i in range(len(to_strike)):
    shot.append(to_strike[i])

strike = 0
for i in range(len(list(start))):
    if list(start)[i] == shot[i]:
        strike += 1

ball = 0
for item in list(start):
    if item in shot:
        ball += 1

print("맞춰야 할 숫자는 "+ to_strike + "입니다.")
print(str(strike) + " strike ")