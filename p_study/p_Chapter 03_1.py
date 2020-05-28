# Chapter  03_2
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

#  [기본형]

# int(10)을 출력하면 10이 출력되는 것은 보통이다.
print(int(10))
# 하지만, int를 출력하게되면 <class 'int'> 가 출력된다.
# 따라서, int는 class임을 알 수 있다.
print(int)
# float 또한 <class 'float'>. 즉, class다.
print(float)
# 그러므로, __magic__으로 정의되는 메소드들이 int와 float같은 기본 자료형에도 정의되어 있음을 알 수 있다.


# [모든 속성 및 메소드 출력]
# 아래의 dir을 통해서 int와 float이 가지고있는 메소드를 확인 할 수 있다.
print(dir(int))
print(dir(float))

# 아래의 변수 선언후 type을 출력하면, <class 'int'>임을 확인 할 수 있다.
# 따라서 단순히 선언한 변수도 class이다.
n = 10
print(type(n))

# 아래의 출력에서는 당연히 110이 출력됨을 예측 할 수 있다.
# 이때, 내부적으로는 int class에 속하는 __add__ 메소드가 실행된 것이다.
print(n + 100)
# 표현하면 아래와 같다.
print(n.__add__(100))

# __doc__메소드를 이용해서 int에 관한 내부적인 설명을 확인 할 수 있다.
print(n.__doc__)

# bool 또한 내부적으로는 __bool__메소드를 이용하여 실행되었다.
print(bool(n))
print(n.__bool__())

# 곱하기 또한 내부적으로는 __mul__메소드를 이용하여 실행되었다.
print(n * 100)
print(n.__mul__(100))

print()
print()


# [클래스 예제1]
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    # __le__ 메소드는 대소비교 (<=) 를 의미한다.
    def __le__(self,x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    # __ge__ (>=) 메소드는 __le__ (<=) 메소드와 반대이다.
    def __ge__(self,x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Orage', 7500)
s2 = Fruit('Banana', 3000)

# [일반적인 계산]
print(s1._price + s2._price)
# (결과값)
# 10500

# [매직메소드를 이용한 계산]

# 매직 메소드를 이용하면 다음과 같이 계산이 가능하다.
# 인스턴스 변수끼리의 덧셈이 +를 통해서 이루어졌다.
# 이는 + 에서 내부적으로 위에서 작성한 __add__메소드가 실행되었기 때문이다.
# 그 증거로, Called __add__가 같이 출력됨을 확인 할 수 있다.
# 또한, 순차적으로, 첫번째 인자인 self는 s1이 되고, 두번째 인자인 x는 s2가 된다.
print(s1 + s2)
# (결과값)
# Called __add__
# 10500

print(s1 >= s2)
# (결과값)
# Called >> __ge__
# True

print(s1 <= s2)
# (결과값)
# Called >> __le__
# False

print(s1 - s2)
# (결과값)
# Called >> __sub__
# 4500

print(s2 - s1)
# (결과값)
# Called >> __sub__
# -4500

print(s1)
# (결과값)
# Fruit Class Info : Orage, 7500

print(s2)
# (결과값)
# Fruit Class Info : Banana, 3000
