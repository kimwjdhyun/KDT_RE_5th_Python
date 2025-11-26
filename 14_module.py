
# 모듈(module) : 파이썬 코드가 들어있는 파일
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것

# 모듈 불러오기(1)
import hello   # hello.py 파일을 불러옴

hello.greeting("kim")   # hello 모듈 안에 있는 greeting 함수 사용

# 모듈 불러오기(2)
from hello import greeting  # hello.py 파일에서 greeting 함수만 불러옴

greeting("lee")   # greeting 함수 바로 사용 가능
# Hello, kim
# Hello, lee

# 모듈 불러오기(3)
from hello import *   # hello.py 파일에서 모든 함수 불러옴
introduce("sin", 20)   # introduce 함수 바로 사용 가능
# 제 이름은 sin이고, 나이는 20살 입니다.

# 모듈 불러오기(4)
import hello as h   # hello.py 파일을 h라는 이름으로 불러옴 
h.introduce("lim", 28)  # 제 이름은 lim이고, 나이는 28살 입니다.
h.introduce("kim", 28) # 제 이름은 kim이고, 나이는 28살 입니다.



# 실습3. 계산기 모듈 만들어보기
import calc
calc.add(4, 8)                    # 12

from calc import subtract
calc.subtract(20,13)              # 7

from calc import *
calc.multiply(48, 6)              # 288

import calc as c
c.divide(3, 0)                    # 0으로 나눌 수 없습니다.
c.divide(36, 4)                   # 9.0


# 패키지(package) : 모듈을 모아놓은 폴더
# - 모듈을 폴더 단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
from my_package import calc as c
c.add(10, 20)               # 30

# 패키지에서 모듈 불러오기(2)
from my_package.calc import add
add(20, 30)                 # 50

# 파이썬 표준 라이브러리

# math 모듈 : 수학적 연산에 사용되는 모듈
import math as m

# 1. 올림 / 내림
# ceil : 올림, 소수점 지정 x
print(m.ceil(3.14))         # 4

# floor : 내림, 소수점 지정 x
print(m.floor(3.14))        # 3

# round : 반올림 - 파이썬 내장 함수(소수점 둘째자리까지 반올림)
print(round(3.141592, 2))   # 3.14

# 2. 제곱, 제곱근
#pow(x, y) : 제곱 - x^y
print(m.pow(2, 3))          # 8.0

#sqrt(x) : 제곱근 반환
print(m.sqrt(16))           # 4.0

# 3. 상수
#pi : 원주율
print(m.pi)                 # 3.141592653589793

# 4. 수학 계산 편의 기능
# factorial(x) : x! (팩토리얼)
print(m.factorial(3))       # 6
# gcd(x, y) : x와 y의 최대공약수
print(m.gcd(12, 8))         # 4
# lcm(x, y) : x와 y의 최소공배수
print(m.lcm(12, 8))         # 24




# 실습 4. math 모듈 사용해보기
# 문제 1. 실제 거리 계산 : 좌표 두점 사이 거리 구하기

import math
def point(x1, y1, x2, y2):
    point1 = int(m.sqrt((x2 - x1))**2 + (y2 - y1)**2)
    point2 = int(m.pow((x2 - x1), 2) + m.pow((y2 - y1), 2))
    point1 = m.sqrt(point2)
    return point1
print(point(1, 2, 3, 4))               # 2.8284271247461903
print(round(point(1, 2, 3, 4)))        # 3

# 문제 2. 상품 나누기 : 최소 공배수와 최대 공약수
import math
def classroom(s, t):
    gcd = m.gcd(s, t)
    lcm = m.lcm(s, t)
    
    print("최대 공약수", gcd)     # 최대 공약수 6
    print("최소 공배수", lcm)     # 최소 공배수 72
classroom(18, 24)



# 해설
# 실습2.
# 📌 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기

# x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# # x1, y1 = int(x1), int(y1)
# x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

# # 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
# dist = round(m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1), 2)), 2)

# print(f"두 점 사이의 거리는: {dist}")


# # 📌 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
# a = 18
# b = 24

# # 최대공약수
# gcd = m.gcd(a, b)

# # 최소공배수
# lcm = m.lcm(a, b)

# print(f"최대 간식 개수: {gcd}")
# print(f"최소 간식 개수: {lcm}")

# random 모듈 : 랜덤 값(난수) 생성 시 사용
import random as r

# 1. 난수 생성
# random() : 0.0 이상 1.0 미만의 실수(float) 난수 반환
print(r.random())           # 0.0 ~ 1.0 미만의 실수 난수 반환

# uniform(a, b) : a 이상 b 미만의 실수 난수 반환
print(r.uniform(1, 10))    # 1.0 ~ 10.0 미만의 실수 난수 반환

# randint(a, b) : a 이상 b 이하의 정수(int) 난수 반환
print(r.randint(1, 100))    # 1 ~ 10 이하의 정수 난수 반환

# randrange(start, stop, step) : 범위 안의 정수 난수 반환, 간격 지정 가능
print(r.randrange(0, 101, 5))  # 1 ~ 100 이하의 홀수 정수 난수 반환


# 2. 랜덤 선택
fruits = ['apple', 'banana', 'watermelon', 'grape', "orenge"]

# choice(seq) : 시퀀스)에서 임의의 요소 1개 반환
print(r.choice(fruits))     # fruits 리스트에서 임의의 요소 1개 반환

# choices(seq, k) : 시퀀스에서 "중복을 허용해서" k개 요소 리스트 반환
print(r.choices(fruits, k=2))  # fruits 리스트에서 임의의 요소 2개 반환

# 섞기
# sample(seq, k) : 시퀀스에서 "중복 없이" k개 요소 리스트 반환
print(r.sample(fruits, k=2))   # fruits 리스트에서 임의의 요소 2개 반환

# shuffle(seq) : 시퀀스의 요소들을 무작위로 섞음 -> 원본 시퀀스를 변경
numbers = [1, 2, 3, 4, 5]
print(r.shuffle(numbers))  # None
print(numbers)             # 섞인 numbers 리스트 출력

# 실습 1. 로또 번호 뽑기
import random as r

def lotto(num):
    return r.sample(range(1, 46), k=num)
print(sorted(lotto(6)))  
# [11, 17, 23, 27, 37, 39]
# [1, 5, 11, 22, 31, 41]
# [8, 9, 21, 23, 26, 39]
# [10, 12, 14, 23, 32, 45]

# 해설
# 실습3. 로또 번호 뽑기
# 1 ~ 45사이의 정수중에서 랜덤으로 6개의 숫자를 뽑는다
# 6개의 숫자는 중복이 있어서는 x
# 오름차순으로 결과를 정렬한다!

# 1) 짧은 식
# result = sorted(random.sample(range(1, 46), k=6))
# print(result)

# # 2) 반복묺 활용
# lotto = []
# while len(lotto) < 6:
#     number = random.randint(1, 45)
#     if number in lotto:
#         continue

#     lotto.append(number)

# lotto.sort()
# print(lotto)

# 실습 2. 가위 바위 보 게임 만들기
# import random as r 

# user = input("무엇을 낼지 골라주세요 : ")

# def game(user):
#     computer = r.choice(["가위", "바위", "보"])
#     if user == computer:
#         return " 무승부 "
#     elif user == "가위" and computer == "보":
#         return " 승리! "
#     elif user == "바위" and computer == "가위":
#         return " 승리! "
#     elif user == "보" and computer == "바위":
#         return " 승리! "
#     else:
#         return " 패배! "
# print(game(user))   
# 무엇을 낼지 골라주세요 : 보
#  무승부
# 무엇을 낼지 골라주세요 : 바위
#  승리!
# 무엇을 낼지 골라주세요 : 가위
#  승리!
# 무엇을 낼지 골라주세요 : 가위
#  패배!

# 해설
# 3판 2선승 가위바위보
# while문 활용
# 실습4. 가위 바위 보 게임 만들기
# RPS = ["가위", "바위", "보"]
# win_count = 0

# while win_count < 3:
#     com_choice = random.choice(RPS)
#     user_choice = input("가위, 바위, 보 중에 골라주세요!✌️✊🤚: ")

#     print(f"유저의 선택: {user_choice}")
#     print(f"컴퓨터의 선택: {com_choice}")

#     if user_choice == com_choice:
#         print("비겼습니다")
#     elif ((user_choice == "가위" and com_choice == "보") or
#           (user_choice == "바위" and com_choice == "가위") or
#           (user_choice == "보" and com_choice == "바위")):
#         print("이겼습니다")
#         win_count += 1
#     elif user_choice in RPS:
#         print("졌습니다")
#     else:
#         print("잘못된 입력이에요")


# datetime 모듈 : 날짜와 시간과 관련된 기능을 제공하는 모듈
# 날짜와 시간의 생성, 조작, 형식 변환과 같은 시간 관련 기능을 제공

import datetime as dt

# 1. 날짜 / 시간 구하기
# 현재 날짜와 시간 구하기
now = dt.datetime.now()
print(now)    # 2025-11-26 10:19:59.636853  

# 오늘 날짜만 구하기
today = dt.date.today()
print(today)      # 2025-11-26

# 2. 날짜 / 시간 형식 변환
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)            # 2025-11-26 10:22:54

parsed = dt.datetime.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)               # 2025-11-26 10:26:10

# 3. 날짜 / 시간 연산
d = dt.date(2025, 5, 8)
passed_time = today - d
print(f"{passed_time.days}일 지났습니다.")   # 202일 지났습니다.

# 4. 요일반환 : weekday
# 0 : 월요일 ~ 7 : 일요일

days = ["월", "화", "수", "목", "금", "토", "일"]
day_num = today.weekday()
print(days[day_num], "요일")                        # 수 요일

# datetime 또는 date 객체에는 년 / 월 / 일 / 시간 등이 속성으로 들어있음.
print(dt.datetime.now().year)                        # 2025
print(dt.datetime.now().month)                       # 11
print(dt.datetime.now().day)                         # 26
print(dt.datetime.now().hour)                        # 10
print(dt.datetime.now().minute)                      # 37
print(dt.datetime.now().second)                      # 15

# 실습 3. 다음 생일까지 남은 날짜 계산하기
import datetime as dt

def birthday(month, day):
    today = dt.date.today()
    year = dt.datetime.now().year
    next_bd = dt.date(year, month, day)
    left_bd = (next_bd - today).days
    if left_bd < 0:
        next_bd = dt.date(year + 1, month, day)
        left_bd = (next_bd - today).days
        return f"생일까지 {left_bd}일 남았습니다!"
    elif left_bd == 0:
        return "생일 축하합니다!"
    else:
        return f"생일까지 {left_bd}일 남았습니다!"
print(birthday(5, 8))       # 생일까지 163일 남았습니다!
print(birthday(11, 26))     # 생일 축하합니다!
print(birthday(1, 20))     # 생일까지 29일 남았습니다!


# # 해설
# # 실습 3. 다음 생일까지 남은 날짜 계산하기
# birth_month, birtg_day = map(int, input("생일을 입력하세요. (예 03-14):").split("-"))

# # 오smf 날짜 구하기
# today = dt.date.today()

# # 올해 생일을 date 객체로 변환
# birth_this_year = dt.date(today.year, birth_month, birtg_day)

# # 오늘 늘짜와 올해의 생일을 비교
# if today > birth_this_year:
#     # 올해 생일이 지났으면 내년으로 설정
#     birth_next = dt.date(today.year + 1, birth_month, birtg_day)
# else:
#     #올해로 설정
#     birth_next = birth_this_year

# # 남은 일수 계산
# days_left = (birth_next - today).days

# print(f"다음 생일까지 {days_left}일 남았습니다!")


# calender 모듈 
# 날짜와 달력 관련 기능을 제공

import calendar as c

# 1. 달력 조회
print(c.prmonth(2025, 9)) # 특정 연도의 특정 달 달력 출력
print(c.prcal(2025)) # 특정 연도의 달력 출력


#    September 2025
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30


#                                   2025

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2                      1  2
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
# 27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
#                                                     31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                1  2  3  4                         1
#  7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 28 29 30 31               25 26 27 28 29 30 31      29 30

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
# 27 28 29 30 31            24 25 26 27 28 29 30      29 30 31


# 텍스트로 값을 반환

print(c.month(2025, 11))
#    November 2025
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

# 요일 반환
print(c.weekday(2025, 11, 26))  # 2 (수요일) : 0~6 (월~일), 인덱스 값으로 반환

print(c.weekday(2026, 1, 20)) # 1 (화요일)
print(c.weekday(2026, 4, 16)) # 3 (목요일)
print(c.weekday(2026, 5, 8))  # 4 (금요일)
print(c.weekday(1999, 1, 20)) # 2 (수요일)
print(c.weekday(1998, 5, 8))  # 4 (금요일)

# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능을 제공

import time as t

# 1. 시간 반환
# time()
# Unix 타임스탬프로 반환 (1970.1.1부터 경과 초)
print(t.time())         # 1764128037.3967812

# ctime()
# 현재 시간의 문자열 형태 반환
print(t.ctime())         # Wed Nov 26 12:33:57 2025
print(t.ctime(0))        # 기준시로 반환 :Thu Jan  1 09:00:00 1970

# strftime() : 원하는 포맷의 문자열로 시간 객체를 변환
it = t.localtime()
formatted = t.strftime("%Y-%m-%d %H:%M:%S", it)
print(formatted)         # 2025-11-26 12:37:28

# strptime() : 문자열을 struct_time 객체로 변환
parsed = t.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)         # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=26, tm_hour=12, tm_min=40, tm_sec=1, tm_wday=2, tm_yday=330, tm_isdst=-1)

# 2. 시간 지연
# sleep(seconds) : 지정한 초만큼 프로그램이 일시 정지
t.sleep(1)   # 1초 일시 정지
print("time sleep")

# 시간 측정하기
# start = t.time()

# for i in range(5):
#     print(i)
#     t.sleep(1)

# end = t.time()
# print(f"수행 시간 : {end - start: .2f}초")
# 0
# 1
# 2
# 3
# 4
# 수행 시간 :  5.01초

# 실습 4. 타자 연습 게임 만들기

# import time as t
# import random as r

# num = 0
# words = [
#     "apple", "banana", "orange", "grape", "lemon",
#     "peach", "melon", "cherry", "plum", "pear",
#     "school", "friend", "family", "flower", "garden",
#     "window", "bottle", "pencil", "summer", "winter",
#     "happy", "future", "travel", "animal", "market",
#     "doctor", "planet", "energy", "nature", "memory"
# ]

# input("[ 타자 연습게임 ] \n 엔터키를 누르면 시작합니다.")
# start = t.time()

# for word in r.choices(words, k=10):
#     while True:
#         user_input = input(f"{num+1}. {word} : ")
        
#         if user_input == word:
#             print("정답입니다!")
#             num += 1
#             break
#         else:
#             print("오타! 다시 도전!")

#     if num == 10:
#         print("게임 클리어!")
#         break

# end = t.time()
# print(f"총 타자 시간 : {end - start:.2f}초 입니다!")


#해설
# 실습 6. 타자 연습게임
# import time as t
# import random as r

# words = [
#     "apple", "banana", "orange", "grape", "lemon",
#     "peach", "melon", "cherry", "plum", "pear",
#     "school", "friend", "family", "flower", "garden",
#     "window", "bottle", "pencil", "summer", "winter",
#     "happy", "future", "travel", "animal", "market",
#     "doctor", "planet", "energy", "nature", "memory"
# ]
# n = 1
# input("[ 타자 게임 ] 준비되면 엔터!")
# start = t.time()

# while n < 11:
#     print(f"{n}번 문제")
#     question = r.choice(words)
#     print(question)
    
#     while True:
#         user_answer = input()
#         if question == user_answer:
#             print("통과!")
#             n += 1
#             break

#         else:
#             print("오타! 다시 도전!")

# end = t.time()
# play_time = end - start
# print(f"총 소요시간 {play_time:.2f}초")



# sys 모듈
# 파이썬 이터프리터와 관련된 다양한 기능 제공

import sys

# 1. 파이썬 버전 정보
print(sys.version)      # 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]

# 운영체제
print(sys.platform)     # win32

# 프로그램 종료
print("프로그램 시작")       # 프로그램 시작
# sys.exit()   # 강제 종료
print("실행되지 않는 코드")  # 실행되지 않는 코드



# os 모듈
# 운영체제와 상호작용할 수 있도록 도와주는 기능 제공

import os

# getcwd() : 현재 작업 디렉토리 반환
print(os.getcwd())    # C:\Users\dkreh\Desktop\KDT_RE_5th\2_Python

# listdir() : 디렉토리 내 파일, 디렉토리 목록 반환
print(os.listdir())  # ['.git', '00_practice.py', '01_variable.py', '02_data_type.py', '03_opperator.py', '04_input.py', '05_list.py', '06_tuple.py', '07_set.py', '08_dictionary.py', '09_if.py', '10_for.py', '11_while.py', '12_function.py', '13_class.py', '14_module.py', 'calc.py', 'coding_test.py', 'hello.py', 'my_package', 'python_study', '__pycache__']

# 폴더 생성
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")

print(os.listdir())  # 'sample_folder' 생성!

