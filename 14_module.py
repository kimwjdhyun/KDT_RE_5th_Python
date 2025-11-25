
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

