'''
함수 (function)
- 특정 작업을 수행하는 코드들의 모음
- 복잡한 코드를 작은 단위로 나눌 수 있게 모아준다.
- 특정한 코드들을 재사용할 수 있게 한다.
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def 사용
def 함수이름 (매개변수):
    # 실행할 코드
    print(매개변수)
    return"반환값"

# 함수의 실행(호출 call)
result = 함수이름("인자")
print(result)

# 매개 변수(Parameter) : 매개 + 변수
# 매개 : 둘 사이를 연결해줌
# 함수가 실행될 때 인자로부터 입력되는값을 함수의 코드블록으로 전달하는 역할

# 함수의 필요성 예제
a = 10
b = 20

if a > b :
    print(a - b)
else :
    print(a + b)

c = 30
d = 40

if c > d :
    print(c - d)
else :
    print(c + d)

def my_func(a, b) :
    if a > b :
        return a - b
    else : 
        return a + b
print(my_func(10, 20))
print(my_func(30, 40))

실습 1. 사칙연산 계산기 함수 만들기
문제 1. 사친견산 계산기 함수 만들기
a = float(input())
b = float(input())
operator = input()

def calculate(a, b, operator) :
    if operator == "+" :
        return a + b
    elif operator == "-" :
        return a - b
    elif operator == "*" :
        return a * b
    elif operator == "/" :
        return a / b
    else : 
        return "지원하지 않는 연산입니다"

result = calculate(a, b, operator)
print(result)

# 키워드 인자
# 예시 1. 
print("안녕하세요", "반갑습니다!", sep="-", end="/")

# 예시 2.
def my_func(a, b, c = None, operator = None) :
    if operator == "+":
        return a + b
    else : 
        return c
print(my_func(10, 20))  # None
print(my_func(10, 20, operator = "+")) # 30

# 기본값 인자
# 단, 기본값 매개 변수는 뒤쪽에 위치해야 한다.
def greet(name, message = "안녕하세요~!") :
    print(f"{name}님, {message}")

# 호출 시 인자 생략 -> 기본값 사용
greet("kimwjdhyun") # kimwjdhyun님, 안녕하세요~!
greet("kimwjdhyun", "복 많이 받으세요~!") # kimwjdhyun님, 복 많이 받으세요~!

# 위치 가변 인자 (*args)
# 여러 개의 값을 유동적으로 받을 수 있음
# 값이 튜플 형태로 받아짐

def add_all(*args) :
    return sum(args)

print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9)) # 45

# 키워드 가변 인자 (**kwargs)
# 여러 키워드 인자를 유동적으로 받을 수 있다. 
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwargs) :
    for key, value in kwargs.items() :
        print(f"{key} : {value}")

print_info(name = "kimwjdhyun", age = 28, city = "jeju")

# name : kimwjdhyun
# age : 28
# city : jeju

# 실습 2. 가변인자 연습하기
# *args 사용 연습
# 문제 1. 숫자 여러 개의 평균 구하기

def average(*args) :
    # 예외처리
    if len(args) == 0:
        return "입력값이 없습니다"
    return sum(args) / len(args)

print(average(1,2,3,4,5,6,7,8,9)) # 5.0

# 문제 2 . 가장 긴 문자열 찾기(max 한수에 대해 찾아보고 풀기)
def my_str(*args) : 
    longest_str = max(args, key=len)
    return longest_str

print(my_str("안녕하세요", "반갑습니다", "별일 없으시죠>", "새해 복 많이 받으세요~!")) # 새해 복 많이 받으세요~!


# 해설 문제 2. 
def longgest(*args) :
    answer = " "
    for s in args :
        if len(s) > len(answer) :
            answer = s
    return answer

print(longgest("watermelon", "lemon", "banana")) # watermelon

# **kwargs 사용 연습
# 문제 3. 사용자 정보 출력 함수
def user_info(**kwargs) :
    for key, value in kwargs.items():
        print(f"{key} : {value}") 
user_info(name = "김정현", age = 28, email = "dkrehd7953@naver.com")
# name : 김정현
# age : 28
# email : dkrehd7953@naver.com

# 문제 4. 할인 계산기
def calculater(**kwargs) :
    for key, value in kwargs.items() :
        print(f"{key} : {value * 0.9}")
calculater(price1 = 10000, price2 = 20000, price3 = 1000000)

# price1 : 9000.0
# price2 : 18000.0
# price3 : 900000.0

# 문제 4. 할인 계산기
def discount_prices(**kwargs):
    for key, value in kwargs.items():
        disconted = value * 0.9
        print(f"{key} : 할인가 {disconted} 원가 {value}")
discount_prices(apple = 2000, watermelon = 20000, chocolate = 2500)

# apple : 할인가 1800.0 원가 2000
# watermelon : 할인가 18000.0 원가 20000
# chocolate : 할인가 2250.0 원가 2500

# 전역 변수 : 함수 밖에 선언된 변수
# 지역 변수 : 함수 안에 선언된 변수

# 예제 1
x = 200 # 전역 변수

def my_func() :
    #지역변수
    x = 10
    print(x) # 안나옴

my_func() # 함수 안 10
print("함수 밖", x) # 함수 밖 200

# 예제 2 
x = 10

def my_func2() :
    x = 20 
    x += 5
    print("지역변수", x)

my_func2() # 지역변수 25
print("전역 변수", x) # 전역 변수 10

x = 10

# 예제 3 (에러 발생)
x = 20

def my_func2() :
    # x = 20 # UnboundLocalError : 전역변수를 함수안에서 수정할 경우 에러 발생
    x += 5
    print("지역변수", x)

my_func2() # 지역변수 25
print("전역 변수", x)

# 예제 4. global 사용 예제
x = 10

def my_func3() :
    global x # 전역변수 사용 선언
    x += 5
    print("지역변수", x)

my_func3()  # 지역변수 15

print("전역변수", x) # 전역변수 15(global 사용으로 전역 변수도 변하게 됨.)

# 권장되는 패턴
# 부수 효과(side effect)를 발생시키지 않는 함수를 위주로 프로그래밍
x = 10

def my_func4(x) : # 함수안에서 새로 지역변수를 만들어서 실행하는 방법
    x += 5
    return x

x = my_func4(x)
print("전역변수", x) # 전역변수 15

# 실습 3. 전역 변수 연습하기
# 문제 : 로그인 / 로그아웃 전역 상택 관리

current_user = ""

def login(name):
    global current_user
    if current_user:
        print("이미 로그인되어 있습니다")
    else:
        current_user = name
        print(f"{name}님 로그인 성공")

def logout():
    global current_user
    if not current_user:
        print("로그인된 사용자가 없습니다")
    else:
        current_user = ""
        print("로그아웃되었습니다")

login("kimwjdhyun")
login("codingon")
logout()
logout()
login("codingon")
print(current_user)

# kimwjdhyun님 로그인 성공
# 이미 로그인되어 있습니다
# 로그아웃되었습니다
# 로그인된 사용자가 없습니다
# codingon님 로그인 성공
# codingon