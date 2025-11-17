'''
딕셔너리(dictionary)
- 키 -값 쌍으로 묶어서 데이터를 저장하는 자료형
- 키는 유일해야함. 값은 중복이 가능
- 변경가능한 자료형
- 순서가 보장되지 않았다가, 파이썬 3.7 이후 순서가 보장됨.
'''

# dict 만들기
d1 = {} # 빈 dict 만들기
print(type(d1)) # <class 'dict'>

person = {"name" : "홍길동", "age" : 25}
print(person) # {'name': '홍길동', 'age': 25}

d2 = dict()
print(d2, type(d2)) # {} <class 'dict'>

# 키가 문자열일 때 가능한 방법
movie = dict(title="inter", director="nolan")
print(movie, movie["director"]) # {'title': 'inter', 'director': 'nolan'} nolan
# 대괄호 사용으로 해당 부분만 출력 가능

# 리스트나 튜플로 만들기
pairs = [("name", "wjdhyun"), ("age", 28), ("job", "none")]
person2 = dict(pairs)
print(person2) # {'name': 'wjdhyun', 'age': 28, 'job': 'none'}

# zip() 함수 활용
keys = ["title", "director", "year"]
value = ["기생충", "봉준호", "2019"]
movie2 = dict(zip(keys, value))

print(movie2) # {'title': '기생충', 'director': '봉준호', 'year': '2019'}

# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야 한다.
d1 = {(1, 2, 3) : (1, 2, 3)} # 튜플은 불변자료형 => 사용 가능
d2 = {1 : 10} # 숫자 사용 가능
# d3 = {[1, 2, 3] : "리스트 값을 키로?"} # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# print(d3) # 리스트는 사용 불가 !



# dict 데이터 조회
print(person2["name"]) # wjdhyun
print(person2["age"]) # 28
# print(person2["city"]) # KeyError: 'city' 존재하지 않는 키는 에러 발생!
print(person2.get("city")) # None # get() 함수는 키가 없을 경우 None을 반환함.(default값이 None)

print(person2.get("email", "이메일이 존재하지 않습니다.")) # 이메일이 존재하지 않습니다.

# get() 사용 예제
user_data = {
    "username" : "wjdhyun",
    "email" : "wjdhyun@naver.com",
    "password" : "123456789"
}

key = input("조회할 정보를 입력하세요(username, email, password):")
result = user_data.get(key, "존재하지 않는 데이터 입니다.")
print(result)