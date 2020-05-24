# Chapter 02_03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Ryu
    Date : 2020.5.24
    Description : Class, Static, Instance Method
    """

    price_per_raise = 1.0

    def __init__(self, company,details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company {}, price {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company {}, price {}'.format(self._company, self._details.get('price')*Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):   # cls는 Car Class의 클래스명 Car를 의미한다.
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        else:
            cls.price_per_raise = per
            print('Succeed! price increased.')

    # Static Method
    @staticmethod # staticmethod는 특정 파라미터를 받지 않는다.
    def is_bmw(inst): # 이때 가로안에는 inst말고 다른 명을 적어도된다. 일단 인스턴스를 받기 때문에 inst라 명시한다.
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        else:
            return 'Oops! This car is not Bmw......'



car1 = Car('Ferrari',{'color':'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw',{'color':'Black', 'horsepower':270, 'price':5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보(직접 접근) 비효율!! BAD
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용) GOOD!!
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스로 호출(static)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 호출(static)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
