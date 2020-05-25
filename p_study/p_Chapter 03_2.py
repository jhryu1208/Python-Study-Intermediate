# Chapter  03_2
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# [클래스 예제2]
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10

class Vector(object):   # object는 있거나 없거나 상관없음, ()도 마찬가지!

    def __init__(self, *arg):   # 패킹&언패킹을 이용하자
                                # 패킹에서 *의 의미 : *을 사용하면 변수 하나당 값 하나를  할당하되 언패킹할 밸류값이 변수보다 많으면 나머지 값은
                                #                     *을 달고 있는 변수에 리스트로 저장이 되는 것이다.
                                #                     예를 들어, arg에 1,2가 전달되면 [1,2]로 저장되는 것이다.
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0        # 언패킹으로 self._x와 self._y에 각각 숫자가 전달된다.
        else:
            self._x, self._y = arg

    def __repr__(self):
        '''Return the vector information.'''
        return 'Vector(%r, %r)' % (self._x, self._y)    # (복습) %를 사용함으로서, self._x을 %r에, self._y를 다음 %r에 전달한다.

    def __add__(self, other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, a):
        '''Return the vector multiply of self and other'''
        return Vector(self._x * a, self._y * a)

    def __bool__(self):
        '''Checking if (0,0) is or is not in a coordinate plane'''
        return bool(max(self._x,self._y))



# [Vector 인스턴스 생성]
v1 = Vector(5, 7)
v2 = Vector(23, 35)
# Class에서 다음을 명시한 이유는 아래와 같은 상황을 예방하기 위해서이다.
# if len(arg) == 0:
#     self._x, self._y = 0, 0
v3 = Vector()


# [설명 출력]
# addition에 있는 설명은 __init__메소드 내부에있으므로,
# 단순히, print(Vector.__doc__)로 입력시 None으로 출력된다.
# 따라서, 다음과같이 입력해줘야 정상적인 내용이 출력된다.
print(Vector.__init__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)
print(Vector.__bool__.__doc__)

# [매직 메소드 출력]
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)

print(bool(v1), bool(v2))
print(bool(v3))
