'''
while 문
- 조건이 True인 동안 코드를 반복하는 반복문
- 조건이 False가 되면 반복을 멈춤
- 반복횟수가 정해지지 않았을 때 사용
'''

# while문 기본 문법
# 조건 : 참 / 거짓을 구분할 수 있는 문장
# while 조건:
    #반복할 코드


# 무한 루프
# 사용 시 주의, 반드시 종료 조건이 있어야 함
# while True:
#     print("반복중")

# 예제 1
# light = "green"
# while light == "green":
#     print("계속 가세요!")
#     light = input("신호등의 신호를 입력하세요(green/yellow/red)")

# print("중지!!")

#계속 가세요!
# 신호등의 신호를 입력하세요(green/yellow/red)green
# 계속 가세요!
# 신호등의 신호를 입력하세요(green/yellow/red)green
# 계속 가세요!
# 신호등의 신호를 입력하세요(green/yellow/red)green
# 계속 가세요!
# 신호등의 신호를 입력하세요(green/yellow/red)yellow
# 중지!!

# 예제 2. 별도의 반복 변수를 정의
i =0

while i < 5:
    print(i, "반복")
    i += 1
print("반복 종료")

# 0 반복
# 1 반복
# 2 반복
# 3 반복
# 4 반복
# 반복 종료

# 실습 2. while문 연습 문제
# # 문제 1. 비밀 코드 맞추기(1)

# secret_code = input("비밀 코드를 입력하세요: ")

# while secret_code != "kimwjdhyun":
#     print("비밀 코드가 틀렸습니다. 다시 시도하세요.")
#     secret_code = input("비밀 코드를 입력하세요: ")
    
# print("입장완료! 환영합니다.")

# # 비밀 코드를 입력하세요: 123
# # 비밀 코드가 틀렸습니다. 다시 시도하세요.
# # 비밀 코드를 입력하세요: 123
# # 비밀 코드가 틀렸습니다. 다시 시도하세요.
# # 비밀 코드를 입력하세요: 123
# # 비밀 코드가 틀렸습니다. 다시 시도하세요.
# # 비밀 코드를 입력하세요: 456
# # 비밀 코드가 틀렸습니다. 다시 시도하세요.
# # 비밀 코드를 입력하세요: kimwjdhyun
# # 입장완료! 환영합니다.

'''
# 해설
secret_code = "codingon3"
user_input = ""

while user_input != secret_code:
    user_input = input("비밀코드를 입력하세요.")
print("입장이 허용되었습니다.")
'''

#문제 2. 업다운 게임

# print("1~100 사이 무작위 수를 생성 중입니다.")

# random = int(input("1~100 사이 무작위 수를 생성 중입니다."))
# count = 0

# while random != '48' :
#     random = input("숫자를 입력하세요. :")
#     count += 1

#     if random > "48":
#         print(f"{random}보다 작아요.")
#     elif random < "48":
#         print(f"{random}보다 커요.")
#     else:
#         print(f"{count}번 만에 정답을 맞췄습니다.")


# # 1~100 사이 무작위 수를 생성 중입니다.
# # 1~100 사이 무작위 수를 생성 중입니다.48
# # 숫자를 입력하세요. :60
# # 60보다 작아요.
# # 숫자를 입력하세요. :30
# # 30보다 커요.
# # 숫자를 입력하세요. :30
# # 30보다 커요.
# # 숫자를 입력하세요. :50
# # 50보다 작아요.
# # 숫자를 입력하세요. :48
# # 5번 만에 정답을 맞췄습니다.
'''
# 해설
asnswer = 99
num = 0 # 사용자 입력 받을 변수
time = 0 # 실행 횟수를 저장할 수 있는 변수

while num != asnswer :
    num = int(input("1~100 사이의 수를 입력해주세요. :"))
    time += 1

    if num > asnswer :
        print(f"정답이 {num}보다 작아요.")
    elif num < asnswer :
        print(f"정답이 {num}보다 커요.")

print(f"{time}번 만에 정답을 맞췄습니다.")

# 1~100 사이의 수를 입력해주세요. :12
# 정답이 12보다 커요.
# 1~100 사이의 수를 입력해주세요. :19
# 정답이 19보다 커요.
# 1~100 사이의 수를 입력해주세요. :98
# 정답이 98보다 커요.
# 1~100 사이의 수를 입력해주세요. :99
# 4번 만에 정답을 맞췄습니다.
'''

# import random 모듈에서 배울예정, 랜덤을 불러오는 것

# 루프 제어문
# running = True
# while running:
#     if 조건1 :
#         running = False
    
#     if 조건2 :
#         running = False

# break

# while True :
#     if 조건 :
#         break

'''
# 예제 1
i = 0

while True :
    print(i, "실행")
    my_select = input("메뉴를 골라주세요. :")

    if my_select == "종료" :
        break
    
    i += 1

print("반복문 종료")

# 0 실행
# 메뉴를 골라주세요. :파스타
# 1 실행
# 메뉴를 골라주세요. :돼지국밥
# 2 실행
# 메뉴를 골라주세요. :소머리국밥
# 3 실행
# 메뉴를 골라주세요. :양념갈비
# 4 실행
# 메뉴를 골라주세요. :삼겹살
# 5 실행
# 메뉴를 골라주세요. :꼬들목살
# 6 실행
# 메뉴를 골라주세요. :차돌박이
# 7 실행
# 메뉴를 골라주세요. :냉면
# 8 실행
# 메뉴를 골라주세요. :된장찌개
# 9 실행
# 메뉴를 골라주세요. :종료
# 반복문 종료

# continue
i = 0
while i < 5 :
    i += 1
    if i % 2 == 0 :
        continue
    print(i)
print("반복 종료")

# 1
# 3
# 5
# 반복 종료
'''

# 실습 3. while문 연습문제(2)
# 문제 1. 비밀 코드 맞추기(2)

secret_code = "codingon3"

while True :
    code = input("비밀코드를 입력하세요. :")

    if code == "codingon3" :
        break
    else:
        print("비밀코드가 틀렸습니다. 다시 시도하세요.")

print("입장완료! 환영합니다.")

# 비밀코드를 입력하세요. :1
# 비밀코드가 틀렸습니다. 다시 시도하세요.
# 비밀코드를 입력하세요. :3
# 비밀코드가 틀렸습니다. 다시 시도하세요.
# 비밀코드를 입력하세요. :5
# 비밀코드가 틀렸습니다. 다시 시도하세요.
# 비밀코드를 입력하세요. :codingon3  
# 입장완료! 환영합니다.


# 문제 2. 유효한 나이만 평균 내기

times = 0
sum_age = 0

while True:
    age = int(input("나이를 입력하세요. : "))
    
    if age < 0 or age > 120:
        continue
    
    times += 1
    sum_age += age  
    
    if times == 5:
        break

average = sum_age // 5  
print(f"총 나이 합계는 {sum_age}, 평균은 {average}입니다.")

# 나이를 입력하세요. : 100
# 나이를 입력하세요. : 150
# 나이를 입력하세요. : -20
# 나이를 입력하세요. : 50
# 나이를 입력하세요. : 100
# 나이를 입력하세요. : 60
# 나이를 입력하세요. : 80
# 총 나이 합계는 390, 평균은 78입니다.