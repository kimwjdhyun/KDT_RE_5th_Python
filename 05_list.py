'''
리스트(list)
- 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스(index) : 각 값에 부여된 순서(0부터 시작)
- 가변 자료형(mutable) : 원소의 추가/수정/삭제 가능
'''

# 리스트 만들기
# list1 = [] # 빈 리스트
# list2 = ["안녕하세요", "반갑습니다"]
# list3 = [10, "좋아요.", 3.14, [1,2,3,4,]]

# print(list1, list2, list3)

# list4 = list()
# list5 = list("코딩온")
# print(list4, list5)


# ===============
# 인덱싱과 슬라이싱
# my_list = [1,2,3,4,5]
# print(my_list[0]) # 1
# print(my_list[-1]) # 5
# my_list[3] = -1
# print(my_list) # 리스트는 수정이 가능하다.

# number = input("네 자릿수 정수를 입력하세요 :")
# 천 = number[0]
# 백 = number[1]
# 십 = number[2]
# 일 = number[3]
# print(천, 백, 십, 일)

# -----------
# 슬라이싱
# my_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(my_numbers[1:4]) # [20, 30, 40]
# print(my_numbers[3:]) # [40, 50, 60, 70, 80, 90, 100]
# print(my_numbers[:4]) # [10, 20, 30, 40]
# my_numbers[2:4] = [300, 400]
# print(my_numbers)

# 실습 1.
# 문제1. 첫 번째 요소와 마지막 요소 출력하기
# nums = [10, 20, 30, 40, 50]
# print(nums[0], nums[-1])
# 문제 2. 가운데 세 개의 요소 추출하기
# nums = [100, 200, 300, 400
# 문제 3. 리스트의 원소 두배 하기
# nums = [1, 2, 3, 4, 5]
# nums[:] = [2, 4, 6, 8, 10] 
# print(nums[:])
# 문제 4. 리스트 뒤집어서 출력하기
# items = ["a", "b", "c", "d", "e"]
# print(items[::-1])
# 문제 5. 짝수 인덱스 요소만 출력하기
# data = ["zero", "one", "two", "three", "four", "five"]
# print(data[0],data[2],data[4])
# 문제 6. 슬라이싱으로 리스트 수정하기
# movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
# movies[2:4] = ["매트릭스", "타이타닉"]
# print(movies)
# 문제 7. 특정 규칙에 따라 요소 추출
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
print(subjects[3::2])
# 문제 8. 리스트를 3개 구간으로 나누어 역순 병합
data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
x = data[:3]
y = data[4:7]
z = data[6:]
print(x[::-1], y[::-1], z[::-1])