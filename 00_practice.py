# 연습(11.12)
# print("Hello World!")

# print("Mary's cosmetics")

# print('신씨가 소리질렀다 "도둑이야"')

# print("c:\windows")

# print("안녕하세요. \n만나서\t\t반갑습니다")
#'\t'는 탭을 의미, '\n'은 줄바꿈을 의미
# print("오늘은", "일요일")

# print('naver','kakao','sk','samsung' , sep=';')
# sep= 인자로 출력되는 값들 사이에 공백 대신 출력할 값
# print("naver", "kakao", "sk", "samsung", sep="/")

# print("first", end='');print("second")
# 세미콜론(;)은 한줄에 여러 개의 명령을 작성하기 위해 사용
# print(5/3)
'''
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.70
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

'''
'''
s = "hello"
t = "python"

print(s+'!', t)
'''
'''
a = "132"
# print(type(a))
# typr() 함수는 테이터 타입을 판별
'''
'''
num_str = "720"
num_int=int(num_str)
print(num_int, type(num_int))
'''
# num = 100
# num_str = str(num)
# print(num_str, type(num_str))

# num_str = "15.79"
# num_float = float(num_str)
# print(num_float, type(num_float))

'''
year = "2020"
print(int(year)-3)
print(int(year)-2)
print(int(year)-1)
'''
# month = 48584
# 총금액 = month * 36
# print(총금액)
#=================================================================
# 연습(11.13)
'''
apple = ['pad', 'phone', 'pods', 'max', 'book', 'tag']
print(len(apple))
apple.append('keyboard')
print(apple)
print(len(apple))

apple.extend(['vision', 'mac'])
print(apple)

apple.insert(5, 'pro')
print(apple)

apple.remove('keyboard')
print(apple)
print(apple.pop())
print(apple.pop(3))
print(apple)

apple.sort()
print(apple)
apple.sort(reverse=True)
print(apple)

sorted_apple = sorted(apple)
sorted_apple_r = sorted(apple, reverse=True)
print(sorted_apple)
print(sorted_apple_r)
print(apple)
'''
'''
letters = "python"
print(letters[0], letters[2]) # p t

license_plate = "24가 2210"
print(license_plate[3:]) # 2210

string = "홀짝홀짝홀짝"
print(string[::2]) # 홀홀홀

string = "python"
print(string[::-1]) # nohtyp

phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-", "")
print(phone_number1) # 010 1234 5678

string = 'abcdfe2a354a32a'
string1 = string.replace("a", "A")
print(string1)

a = "3"
b = "4"
print(a + b) # 34

a = '-'
print(a*80)

t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(이름: {name1} 나이: {age1}
 이름: {name2} 나이: {age2})

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
형변환 = int(컴마제거)
print(형변환, type(형변환))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "   삼성전자    "
data1 = data.strip()
print(data1) # 문자열에서 strip() 사용시 좌우 공백 제거
'''

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:]) # [100, 130, 140, 150, 160, 170]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # [1, 3, 5, 7, 9]
print(nums[1::2]) # [2, 4, 6, 8, 10]
print(nums[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2]) # 삼성전자 Naver

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest) # ['삼성전자', 'LG전자', 'Naver']

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) # [1, 2, 3, 4, 5, 9, 10]

my_variable = ()
print(type(my_variable)) # <class 'tuple'>

tuple1 = (1,)
print(tuple1) # (1,)

interest = ('삼성전자', 'LG전자', 'SK Hynix')
list1 = list(interest)
print(type(list1)) # <class 'list'>

interest = ['삼성전자', 'LG전자', 'SK Hynix']
tuple1 = tuple(interest)
print(type(tuple1)) # <class 'tuple'>

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # apple banana cake

data = tuple(range(2, 100, 2))
print( data )


