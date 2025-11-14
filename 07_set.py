'''
set(집합)
- 원소의 중복을 허용하지 않는 여러 데이터의 모음
- 순서가 없는 컬렉션 자료형
'''

# set 만들기
s1 = {1,2,3}
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

s2 = {1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,}
print(s2) # {1, 2, 3, 4}, 중복 허용 x

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict(dictionary)로 인식됨
s3 = {}
print(type(s3)) # <class 'dict'>

# set 함수로 생성
s4 = set()
print(s4, type(s4)) # set() <class 'set'>

# set 함수의 활용 : 원소의 중복 제거
my_list = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4]
s5 = set(my_list)
print(s5, type(s5)) # {1, 2, 3, 4} <class 'set'>

# 인덱싱 x
# s1[1] # TypeError: 'set' object is not subscriptable

##**해시값에 대해 공부하기**

# 자료형 제한
# - 가변 자료형은 원소로 사용할 수 없다.
# s1 = {1,2,3,[1,2,3]} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
'''
# set 연산
# - 집합의 연산 : 합집하브 교집합, 차집합, 대칭차집합
a = {1,2,3}
b = {3,4,5}

# 합집합 (|, .union())
s_union1 = a | b
s_union2 = a.union(b)
print("합집합", s_union1) # 합집합 {1, 2, 3, 4, 5}
print("합집합", s_union2) # 합집합 {1, 2, 3, 4, 5}

# 교집합(&, .intersection())
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합", s_inter1) # 교집합 {3}
print("교집합", s_inter2) # 교집합 {3}

# 차집합 (-, difference())
s_diff1 = a - b
s_diff2 = a.difference(b)
print("차집합", s_diff1) # 차집합 {1, 2}
print("차집합", s_diff2) # 차집합 {1, 2}
print(b-a) # {4, 5}

# 대칭 차집합 (^, symmetric_difference)
s_symm1 = a ^ b
s_symm2 = a.symmetric_difference(b)
print("대칭 차집합", s_symm1) # 대칭 차집합 {1, 2, 4, 5}
print("대칭 차집합", s_symm2) # 대칭 차집합 {1, 2, 4, 5}
'''
# 실습 1. set 종합 연습
# 문제1. 중복 제거 및 개수 세기

submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
submissions1 = set(submissions)
print(submissions1) # {'kim', 'park', 'choi', 'lee'}
print("제출한 학생 수:", len(submissions1)) # 제출한 학생 수: 4
print("제출자 명단:", submissions1) # 제출자 명단: {'kim', 'park', 'choi', 'lee'}

# 문제2. 공통 관심사 찾기
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
print("공통 관심 장르: ",user1&user2) # 공통 관심 장르:  {'Drama', 'Action'}
print("서로 다른 장르: ",user1^user2) # 서로 다른 장르:  {'SF', 'Romance'}
print("전체 장르: ",user1|user2) # 전체 장르:  {'Romance', 'SF', 'Drama', 'Action'}