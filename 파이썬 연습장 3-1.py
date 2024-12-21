import random

while True:
    while True:
        inputted = input("5자리 숫자를 입력하십시오.")
        inputted_verify = inputted.isdigit()
        inputted_set = set(inputted)
        inputted_int = int(inputted)
        if inputted_verify:
            if len(inputted_set) != len(inputted):
                print("중복된 숫자가 들어있습니다.")
                continue
            if 0< inputted_int < 100000:
                break
            else: print("5자리의 정수를 입력해야 합니다.")
        else: print("숫자가 아닌 걸 입력하셨습니다.")
    attack = []
    for i in range(len(inputted)):
        attack.append(inputted[i])
    # 입력받은 숫자의 예외처리
    while True:
        to_strike = str(random.randint(10000, 99999))
        to_strike_set = set(to_strike)
        if len(to_strike_set) != len(to_strike):
            continue
        else: break

    shot = []
    for i in range(len(to_strike)):
        shot.append(to_strike[i])

    strike = 0
    for i in range(len(attack)):
        if attack[i] == shot[i]:
            strike += 1

    ball = 0
    for item in attack:
        if item in shot:
            ball += 1

    print("맞춰야 할 숫자는 "+ to_strike + "입니다.")
    print(str(strike) + " strike " + str(ball) + " ball")

    if strike == 5:
        print("5스트라이크를 달성하셨습니다. 게임을 종료합니다.")
        break