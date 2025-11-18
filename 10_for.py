# for 문
# - 이터러블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# 리스트 반복
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(f"I like {fruit}")
# I like apple
# I like banana
# I like cherry

# 문자열 반복
# my_str = "codingon"
# for cha in my_str:
#     print(cha) # c o d i n g o n

# 튜플 반복
# coords = [(1, 2), (10, 15), (-6, 8)]
#언패킹 (구조분해 가능)
# for x, y in coords:
#     print(f"x좌표 : {x}, y좌표는 {y}")
# x좌표 : 1, y좌표는 2
# x좌표 : 10, y좌표는 15
# x좌표 : -6, y좌표는 8

# dict 반복
# person = {
#     "name" : "kim", 
#     "age" : 28, 
#     "address" : "jeju"
# }

# 기본
# for key in person:
#     print(f"key : {key}, value : {person[key]}")
# key : name, value : kim
# key : age, value : 28
# key : address, value : jeju

# value 만 가져오기
# for value in person.values():
#     print(f"value : {value}")
# value : kim
# value : 28
# value : jeju

# items : 모든 쌍(키, 값) 가져오기
# for key, value in person.items():
#     print(f"key : {key}, value : {value}")
# key : name, value : kim
# key : age, value : 28
# key : address, value : jeju

# set 반복
# my_set = {1, 2, 3, 4}

# for s in my_set:
#     print(s) # 1, 2, 3, 4

# 실습 1. for문 기본 문법 문제
# 문제 1. 리스트의 값을 두 배로 변환하기
# numbers = [3, 6, 1, 8, 4]
# doubled = []
# for num in numbers:
#     doubled.append(num * 2)
#     print(doubled)
# [6]
# [6, 12]
# [6, 12, 2]
# [6, 12, 2, 16]
# [6, 12, 2, 16, 8]

# 해설 : 새로운 리스트 생성 후 진행 

# 문제 2. 문자열의 길이 구해서 새 리스트 만들기
# words = ["apple", "banana", "kiwi", "grape"]
# list = []
# for word in words:
#     list.append(len(word))
#     print(list)
# [5]
# [5, 6]
# [5, 6, 4]
# [5, 6, 4, 5]

# 문제 3. 좌표 튜플에서 x, y 좌표 나누기
# coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

# x_values = []
# y_values = []

# for x, y in coordinates:
#     x_values.append(x)
#     y_values.append(y)

# print(f"x 좌표 :, {x_values}")
# print(f"y 좌표 :, {y_values}")


# x 좌표 :, [1, 3, 5, 7]
# y 좌표 :, [2, 4, 6, 8]

# for 문과 range()
# range ()함수 : 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step) 
# - start : 생량 가능, 기본 값 = 0
# - end : end -1까지 생성
# - step : 생략 가능, 기본 값 = 1

# range(1, 5)

# for i in range(1, 5):
#     print(i) # 1 2 3 4

# for i in [1,2,3,4]:
#     print(i) # 1 2 3 4

# # start 생략
# for i in range(5):
#     print(i) # 0 2 3 6 8 10

# # 간격 (step) 지정
# for i in range(0, 11, 2):
#     print(i)
# for i in range(11, 0, -2):
#     print(i) # 11 9 7 5 3 1

# 실습 2. for 문과 range
# 문제 1. 입력 받은 수의 합 구하기

# user_number = input("수를 입력하세요")
# x = [user_number]

# for user_number in x:
#     range(1, int(user_number))
#     x = sum(range(1, int(user_number)+1))
#     print(x) # 100 / 4950


# 문제 2. 구구단 만들기
# user_number = int(input("수를 입력하세요. :"))

# for i in range(1, 10):
#     print(f"{user_number} X {i} = {user_number * i}")
# # 수를 입력하세요. :12
# 12 X 1 = 12
# 12 X 2 = 24
# 12 X 3 = 36
# 12 X 4 = 48
# 12 X 5 = 60
# 12 X 6 = 72
# 12 X 7 = 84
# 12 X 8 = 96
# 12 X 9 = 108

# 문제 3. 3의 배수 합 구하기
x = 0
for i in range(3, 101, 3):
    x += i
print(x) # 1683


# 문제 4. 짝수이면서 5의 배수인 수 출력하기
n = int(input("수를 입력하세요. "))
for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i) # 10 20 30 40 50