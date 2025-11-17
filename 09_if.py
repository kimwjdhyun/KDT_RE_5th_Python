'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참 / 거짓을 구분할 수 있는 문장
'''

# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행
# 들여쓰기 중요!!
# a = int(input())
# if a > 10:
#     print("a는 10보다 커요.")
# print("조건문 종료")

# # 들여쓰기 에러 예시
# if a>10:
#   print("조건문 종료")

# print("a는 10보다 커요.") # IndentationError : 들여쓰기 오류

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
# if a > 100:
#    pass # 비워둘 경우 pass를 써야함(안쓸경우 에러 발생)

weather = input("오늘 날씨는 어떤가요?")
weather1 = "비"
weather2 = "맑음"
if weather==weather1:
   print("우산을 챙기세요!") 
if weather==weather2:
    print("선크림을 바르세요!")