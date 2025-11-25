
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

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

# 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
dist = round(m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1), 2)), 2)

print(f"두 점 사이의 거리는: {dist}")


# 📌 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
a = 18
b = 24

# 최대공약수
gcd = m.gcd(a, b)

# 최소공배수
lcm = m.lcm(a, b)

print(f"최대 간식 개수: {gcd}")
print(f"최소 간식 개수: {lcm}")