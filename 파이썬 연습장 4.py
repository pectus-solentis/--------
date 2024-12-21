message1 = "WOW!! ThIs mOvIe...    was @@aMAZING@@!!     I couldn't BELIEVE how **good** the actors were.  The plot was    so~~ thrilling."
message2 = "Worst movie EVER!!!    I can't believe I spent $15 on this...    the acting was horrIBle, and the plot? non-existent!! :(  do NOT recommend.   :("

def preprocessing(message):
    message = message.lower()
    message = message.strip()
    # 덧글의 모든 영문자를 소문자로 치환하고 덧글 앞뒤의 공백문자를 제거
    special_chars = "!@#$%^&*()_+-=[]{};':\",./<>?`~"
    # 특수문자 목록 정의
    for char in special_chars:
        message = message.replace(char, '')
    # 특수문자 제거
    while "  " in message:
        message = message.replace("  ", " ")
    # 연속된 공백을 하나의 공백으로 치환
    return message

text1 = preprocessing(message1)
text2 = preprocessing(message2)
text_input = preprocessing(input("임의의 덧글을 영문으로만 입력하십시오."))

print(text1)
print(text2)
print(text_input)