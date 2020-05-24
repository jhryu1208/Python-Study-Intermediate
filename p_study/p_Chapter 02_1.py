# Chapter 02_01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color':'White'},
    {'horsepower':400},
    {'price':8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color':'Black'},
    {'horsepower':270},
    {'price':5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color':'Silver'},
    {'horsepower':300},
    {'price':6000}
]

print()
print()


# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
        {'color':'White', 'horsepower':400, 'price':8000},
        {'color':'Black', 'horsepower':270, 'price':5000},
        {'color':'Silver', 'horsepower':300, 'price':6000}
]

# 인덱스 접근 삭제법 (실수가능성 ㅇ)
del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
{'car_company':'Ferrari', 'car_detail':{'color':'White', 'horsepower':400, 'price':8000}},
{'car_company':'Bmw', 'car_detail':{'color':'Black', 'horsepower':270, 'price':5000}},
{'car_company':'Audi', 'car_detail':{'color':'Silver', 'horsepower':300, 'price':6000}}
]

print(car_dicts)

del car_dicts[1]
print(car_dicts)

print()
print()


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

    # [__str__, __repr__정리]
    # __str__(string), __repr__(representation)은 클래스안의 magic method로 문자열을 표현하는 값으로
    # 리턴시켜주는 내장함수이다.

    # *magic method 란? 클래스 내부의 함수명 앞뒤의 언더바 2개씩 있는 것.
    # 시작하기 앞서, str과 repr의 차이를 보여주는 예제는 다음과 같다.

    # (문자열 예제)
    # s = "Hello, World!"
    # print(str(s)) -> 결과값 : Hello, World!
    # print(repr(s)) -> 결과값 : 'Hello, World!'

    # str은 따옴표가 없이 출력되어 나타나지만, repr는 따옴표로 감싸져서 출력이되었다.
    # 이는 repr로 출력하면, '파이썬에서 해당 객체를 만들 수 있는 문자열'로 출력됨을 의미한다.

    # (실수 예제)
    # s = 0.12345678987654321
    # print(str(a)) -> 결과값 : 0.123456789877
    # print(repr(a)) -> 결과값 : 0.12345678987654321

    # str로 출력된 문자열은 a와 같은 객체를 만들 수 없지만,
    # repr를 통해 출력한 문자열로는 다시 기존 객체와 같은 값을 가지는 객체를 생성할 수 있다.

class Car():
    # 객체 초기화 메소드 __init__
    def __init__(self, company,details):
        self._company = company
        self._details = details

    # 클래스의 정보를 디테일하게 출력하게 도와주는 __str__ 메소드
    # 사용자가 보기 쉬운 형태로 보여줄 때 사용
    # str : Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}
    def __str__(self):
        # 문자열 리턴
        return 'str : {} - {}'.format(self._company, self._details)

    # __str__메소드와 유사한 representation 메소드
    # 시스템(python interpreter)이 해당 객체를 인식 할 수 있는 공식적인 문자열로 나태내 줄 때 사용하는 것이다.
    # repr : Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)



car1 = Car('Ferrari',{'color':'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw',{'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi',{'color':'Silver', 'horsepower':300, 'price':6000})


# 이때 print함수에 의해 자동호출되는 __str__, __repr__의 우선순위는
# (1) __str__을 우선 호출해보고
# (2) __str__이 전혀 구현되어 있지 않으면 __repr__함수를 찾게됨
# (3) 둘다 구현되어 있따면 __str__먼저 찾고 종료시켜버림,
#     따라서, __repr__결과값은 단순히 print함수로는 확인이 불가능하다.
print(car1)
print(car2)
print(car3)

# 클래스 안의 속성 정보 확인
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

# 리스트 선언
# 이때는 str이 아니라 representation으로 표현됨
car_list = []
car_list. append(car1)
car_list. append(car2)
car_list. append(car3)

print(car_list)

print()
print()


# 반복(__str__)
for x in car_list:
    print(x)        ## str 호출
    print(repr(x))  ## repr 호출
