import random

while True:
    print("5자리의 정수를 입력해야 합니다.")
    inputted = input("5자리 숫자를 입력하십시오.").isdigit()
    if inputted:
        inputted_int = int(inputted)
        if not 0 < inputted_int < 100000:
            print("5자리의 정수를 입력해야 합니다.")    
        else:
            inputted_str = str(inputted_int)
            break
            
attack = []
for i in range(len(inputted_str)):
    attack.append(inputted_str[i])
# 입력받은 숫자는 예외처리를 위해서 주어진 구간 안에 있음을 검증해야 하기 때문에 int형으로 받았다가 일이 끝나면 str형으로 바꿔줍니다.

to_strike = str(random.randint(10000, 99999))
shot = []
for i in range(len(to_strike)):
    shot.append(to_strike[i])

strike = 0
for i in range(len(attack)):
    if attack[i] == shot[i]:
        strike += 1
ball = 0
for i in range(len(attack)):
    if attack[i] in shot:
        ball += 1

print("맞춰야 할 숫자는 "+ to_strike + "입니다.")
print(str(strike) + " strike " + str(ball) + " ball")