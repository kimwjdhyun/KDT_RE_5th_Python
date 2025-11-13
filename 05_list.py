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

# # print(list1, list2, list3)

# list4 = list()
# list5 = list("코딩온")
# print(list4, list5)


# # ===============
# # 인덱싱과 슬라이싱
# my_list = [1,2,3,4,5]
# print(my_list[0]) # 1
# print(my_list[-1]) # 5
# my_list[3] = -1
# print(my_list) # 리스트는 수정이 가능하다.

# # number = input("네 자릿수 정수를 입력하세요 :")
# number = [0, 1, 2, 3]
# 천 = number[0]
# 백 = number[1]
# 십 = number[2]
# 일 = number[3]
# print(천, 백, 십, 일)

# # -----------
# # 슬라이싱
# my_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # print(my_numbers[1:4]) # [20, 30, 40]
# # print(my_numbers[3:]) # [40, 50, 60, 70, 80, 90, 100]
# # print(my_numbers[:4]) # [10, 20, 30, 40]
# # my_numbers[2:4] = [300, 400]
# # print(my_numbers)

# # 실습 1.
# # 문제1. 첫 번째 요소와 마지막 요소 출력하기
# nums = [10, 20, 30, 40, 50]
# print(nums[0], nums[-1])

# # 문제 2. 가운데 세 개의 요소 추출하기
# nums = [100, 200, 300, 400, 500, 600, 700]
# print(nums[2:5])

# # 문제 3. 리스트의 원소 두배 하기
# nums = [1, 2, 3, 4, 5]
# nums[:] = [2, 4, 6, 8, 10] 
# print(nums[:])

# # 문제 4. 리스트 뒤집어서 출력하기
# items = ["a", "b", "c", "d", "e"]
# print(items[::-1])

# # 문제 5. 짝수 인덱스 요소만 출력하기
# data = ["zero", "one", "two", "three", "four", "five"]
# print(data[0],data[2],data[4])
# # print(data[::2]) <- 두칸 간격으로 슬라이싱

# # 문제 6. 슬라이싱으로 리스트 수정하기
# movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
# movies[2:4] = ["매트릭스", "타이타닉"]
# print(movies)

# # 문제 7. 특정 규칙에 따라 요소 추출
# subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
# print(subjects[3::2])
# # print(subjects[3:8:2]) <- 3번 인덱스부터 2칸씩 추출

# # # 문제 8. 리스트를 3개 구간으로 나누어 역순 병합
# data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
# x = data[:3]
# y = data[4:7]
# z = data[6:]
# print(x[::-1], y[::-1], z[::-1])
# # print(data[0:3][::-1], end=" ")
# print(data[3:6][::-1], end=" ")
# print(data[6:][::-1]) <- 줄바꿈 없애기 활용!

# 인덱싱, 슬라이싱 주의 사항
# my_list = [1, 2, 3, 4]
# my_list[5]
# my_list[5] # IndexError: list index out of range

# my_list = [1, 2, 3, 4, 5]
# print(my_list[4:1:2]) # []
# print(my_list[1:3:-1]) # []

#================
# 리스트 연산 - del
'''
my_list = [10, 20, 30, 40, 50]
del my_list[2] # 특정 요소 삭제
print(my_list)
del my_list[1:3] # 슬라이스 범위 삭제
print(my_list)
del my_list # 리스트 삭제
print(my_list) # NameError: name 'my_list' is not defined
'''

# 리스트 연산 - +
'''
list1 = ["가", "나", "다"]
list2 = ["라", "마", "바"]
new_list = list1 + list2
print(list1, list2, new_list, sep="/")
'''

# 리스트 반복 - *
'''
medal = ["금", "은", "동"]
new_list = medal * 3
print(medal, new_list, sep=" / ")

'''
# 포함 여부 (in, not in)
'''
fruits = ["토마토", "사과", "수박", "바나나", "포도"]
print("포도" in fruits)
print("참외" not in fruits)
'''

'''
# 실습 2.
# 문제 1. 부분 삭제 후 연결
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print("result", fruits) # 해설 result = fruits[:1] + fruits[1:]


# 문제 2. 반복 리스트 내부 요소 삭제
letters = ["A", "B"]
new_letters = letters * 3
del new_letters[2]
print(new_letters)
'''
#====================
# 리스트 주요 메서드
#====================

# 길이
numbers = [1,2,3,4,5]
print("1.len()", len(numbers), len("codingon"))

# 삽입
numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers)

numbers. insert(2, 2.5)
numbers. insert(4, 3.5)
print("3. insert()", numbers)

numbers.extend([9, 10])
print("4. extend()", numbers)

# 삭제
numbers.append(2.5)
numbers.remove(2.5)
print("5. remove()", numbers)

a = numbers.pop(1)
print("6. pop()삭제한 요소", a)
print(numbers)
b = numbers.pop()
print("6. pop()삭제한 요소", b)
print(numbers)

# 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()", numbers1)
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1)

numbers2 = [50, 52, 53, 51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True) # desc : 내림차순
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc)

#실습(혼자)

apple = ['pad', 'phone', 'pods', 'max', 'book', 'tag']
print(len(apple))
apple.append('keyboard')
print(apple)
print(len(apple))

apple.extend(['vision', 'mac'])
print(apple)

apple.insert(5, 'pro')
print(apple)