# 클래스(class)
# - 데이터와 기능을 하나로 묶는 구조
# - 개념적(기능적)으로 유사한 관계에 있는것들을 묶어줌

# 클래스 기본 문법
# 클래스의 정의
class ClassName : 
    # 생성자(constructor) : 인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의가 가능
    def __init__(self, name):
        # 인스턴스 변수
        # self : 인스턴스 자기 자신을 가리킴
        self.name = name # 입력받은 값
        self.age = 0 # 선언도 가능
    
    #  (인스턴스)메서드
    def method_name(self) :
        print(f"이 인스턴스의 이름은 {self.name}입니다.")

# 인스턴스 생성
my_instance = ClassName("kimwjdhyun")
print(my_instance.name)             # 이 인스턴스의 이름은 kimwjdhyun입니다.
my_instance.method_name()

another_instance = ClassName("wjdhyun") # 이 인스턴스의 이름은 wjdhyun입니다.
another_instance.method_name()

# 실습 1. class 만들기
# 문제 1. 책 클래스 만들기

class Book:
    def __init__(self, title, author, total_pages, my_page):
        self.title = title
        self.author = author
        self.total_pages = int(total_pages)
        self.my_page = int(my_page)
        self.current_page = float((my_page * 100) / total_pages)

    def method_title(self):
        print(f"이 책의 제목은 {self.title}입니다.")

    def method_author(self):
        print(f"이 책의 저자는 {self.author}입니다.")

    def read_page(self):
        print(f"이 책은 총 {self.total_pages}페이지이며, 현재 {self.my_page}페이지 까지 읽었습니다.")

    def progress(self):
        print(f"현재 {self.current_page}% 읽었습니다.")

my_instance = Book("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", 472, 256)
my_instance.method_title()
my_instance.method_author()
my_instance.read_page()
my_instance.progress()

# 해설 


# 문제 2. Rectangle 클래스 구현

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
wid = int(input("가로 : "))
hei = int(input("세로 : "))
Rectangle = Rectangle(wid, hei)
print("넓이는", Rectangle.area())

