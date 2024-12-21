while True:
    inputted = input("5자리 숫자를 입력하십시오.")
    inputted_verify = inputted.isdigit()
    inputted_set = set(inputted)
    inputted_int = int(inputted)
    if inputted_verify:
        if len(inputted_set) != len(inputted):
            print("중복된 숫자가 들어있습니다.")
        if 0< inputted_int < 100000:
            break
        else: print("5자리의 정수를 입력해야 합니다.")
    else: print("숫자가 아닌 걸 입력하셨습니다.")