# Chapter  03_3
# NamedTuple

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# [일반적인 튜플]
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt # math패키지로 부터 sqrt모듈을 import

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

# ***[네임드 튜플 사용]
from collections import namedtuple  # collection 패키지로 부터 namedtuple모듈을 import

# [네임드 튜플 선언]
Point = namedtuple('Point', 'x y') # 네임드 튜플을 사용해 dictionary식으로도 접근가능하고, index로도 접근가능하다.
pt3 = Point(1.0, 5.0) # 위의 pt1보다 더 명시적으로 표현가능
pt4 = Point(2.5, 1.5)

print(pt3)
# (결과값)
# Point(x=1.0, y=5.0)

print(pt4)
# (결과값)
# Point(x=2.5, y=1.5)

# 네임드 튜플 - index를 이용한 접근
l_leng_index = sqrt((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2)
# 네임드 튜플 - Key를 이용한 접근 (데이터 관리측면에서는 key를 이용한 접근이 더욱 유용하다.)
l_leng_key = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng_index)
print(l_leng_key)


# [네임드 튜플 선언 방법]
Point1 = namedtuple('Point', 'x y')
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', ['x', 'y'])
# 네임드 튜플 생성시, 중복된 객체나 예약어는 원칙적으로 사용못하지만, rename = True를 통해서 가능하다.  원래 Default값은 False이다.
Point4 = namedtuple('Point', 'x y x class', rename=True)


# [출력]
print(Point1, Point2, Point3, Point4)
# (결과값)
# <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>


# [Dict to Unpacking]
temp_dict = {'x' : 75, 'y' : 55}


# [객체 생성]
p1 = Point1(x = 10, y = 35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40) # Point4는 3개만 값을 넘길시 에러가 발생한다. 왜냐하면 Point4는 4개의 인자를 받기때문이다.
p5 = Point3(**temp_dict)    # (중요) 튜플 언패킹시 *는 하나가 붙지만, 딕셔너리 언패킹시 *는 두개가 붙는다!!!!
print()

print(p1)
# (결과값)
# Point(x=10, y=35)

print(p2)
# (결과값)
# Point(x=20, y=40)

print(p3)
# (결과값)
# Point(x=45, y=20)

print(p4)
# (결과값)
# Point(x=10, y=20, _2=30, _3=40)  -> 중복과 예약어에 관한 key로는 난수 _2와 _3이 배치되었다.
#                                     따라서, 중복,예약어를 사용한 네임드튜플은 자주사용되지 않는다.

print(p5)
# (결과값)
# Point(x=75, y=55)

print()

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# 언패킹
x, y = p2
print(x, y)


# [네임드 튜플 메소드]
temp = [52, 38]
# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)
# (결과값)
# Point(x=52, y=38) -> 리스트를 네임드튜플로 변환!!!!

# _fields : 필드 네임 확인, key값만 조회할때 주로 사용
print(p1._fields, p2._fields, p3._fields)
# (결과값)
# ('x', 'y') ('x', 'y') ('x', 'y')

# _asdict() : OderedDict 반환
print(p1._asdict())
# (결과값)
# OrderedDict([('x', 10), ('y', 35)]) -> 리스트안에 튜플형식으로 반환
