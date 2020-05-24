# Chapter 02_02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Ryu
    Date : 2020.5.24
    """
    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company,details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('DEL OK')
        Car.car_count -= 1

    def detail_info(self):
        # 인스턴스 변수의 ID는 각자 고유의 값을 가진다.
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# self 의미
# 아래의 ID확인을 통해 self의 의미를 알 수 있다.
# Therefore, 각자 고유의 값을 가지고 있도록 해줌.
car1 = Car('Ferrari',{'color':'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw',{'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi',{'color':'Silver', 'horsepower':300, 'price':6000})

# ID 확인
# 3개의 identity가 모두 다름을 확인 할 수 있다 -> 각자 고유의 값을 가지고 있다.
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2) ## car1이랑 car2가 같니? NO

# dir & __dict__ 확인
# attribute들을 list 형태로 보여준다.
print(dir(car1))
print(dir(car2))
print(dir(car3))

print()
print()

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# Doctring (쌍따옴표 주석)\
# 해당 코드의 사용법 또는 저자를 설명할 때 사용한다.
#   Car class
#   Author : Ryu
#   Date : 2020.5.24
print(car1.__doc__)
print()

# 실행
Car.detail_info(car1) # = car1.detail_info
Car.detail_info(car2) # = car2.detail_info
Car.detail_info(car3) # = car3.detail_info

# 에러
# Car.detail_info() -> TypeError: detail_info() missing 1 required positional argument: 'self' -> 인자를 넘기지 않아서 생기는 문제
# Car.detail_info(car1) -> car1이라는 self인자를 수동으로 넘겨주면 성립


# 비교
#  car1, 2, 3의 class는 모두  __main__.car이다.
print(car1.__class__, car2.__class__)
# 아래의 id값은 같다. 왜냐하면, 부모 class가 car로 똑같기 떄문이다.
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
# 하지만, 각 인스턴스는 고유의 ID값을 가진다.
print(id(car1), id(car2), id(car3))
# True
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

print()
print()

# 공유확인
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))  # 클래스변수가 공유되는 것을 속성값을 통해서 확인 할 수 있다. [...,'car_count']

print()
print()


# 접근
print(car1.car_count)
print(Car.car_count)

print()
print()

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

print()
print()


# 인스턴스 네임스페이스에 없으면 상위에서 검색

# class Car():
#     """
#     Car class
#     Author : Ryu
#     Date : 2020.5.24
#     """
#     # 클래스 변수 (모든 인스턴스가 공유)
#     car_count = 0
#
#     def __init__(self, company,details):
#         self.car_count = 10  =================================> 인스턴스 네임스페이스에 있음
#         self._company = company
#         self._details = details
#         Car.car_count += 1
#
#     def __str__(self):
#         return 'str : {} - {}'.format(self._company, self._details)
#
#     def __repr__(self):
#         return 'repr : {} - {}'.format(self._company, self._details)
#
#     def __del__(self):
#         print('DEL OK')
#         Car.car_count -= 1
#
#     def detail_info(self):
#         # 인스턴스 변수의 ID는 각자 고유의 값을 가진다.
#         print('Current ID : {}'.format(id(self)))
#         print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
#
#     print(Car.car_count)  =======================================================================>>> 클래스 변수에 있는 값이 출력됨 (2)
#     print(car1.car_count) =======================================================================>>> 인스턴스 네임스페이스에 있으므로, 10이 출력됨. 또한, 두 변수는 이름이 같다!!
#                                                                                                      이떄, 본문 처럼 인스턴스 네임스페이스에 없으면 상위에서 검색한다. 즉, 클래스 변수의 값을 끌어온다.
#                                                                                                      따라서, 동일한 이름으로 변수 생성 가능하다. (인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
