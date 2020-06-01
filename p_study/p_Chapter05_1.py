# Chapter 05_1
# 일급 함수(일급 객체)
# 파이썬 함수 특징

# 일급 함수(first class)는 객체 지향 프로그래밍(OOP)중에서 파이썬을 포함한
# 몇몇 프로그래밍 언어에서 발견할 수 있는 개념이다. 아래는 이를 잘드러내는 파이썬의 철학이다.
#
# '모든 것은 객체(object)이다.'
#
# 객체는 숫자, 문자열, 튜플, 리스트, 딕셔너리, 그리고 함수를 포함한다.
# 함수는 그 중에서도 일급 시민(first-class citizen)이다. 이 뜻은 다음과 같다.
#
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)
#
# 보통은 변수를 객체라고 생각한다. 하지만 함수(function)도, 클래스(class)등도 객체가
# 될 수 있다. 파이썬의 다른 기타 자료구조를 포함한 모든것의 객체이기 때문에 무엇이든
# 함수의 인자(argument)로 전달 가능하다.

def factorial(n):
    ''' Factorial Function -> n : int '''
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

class A:
    pass

print(factorial(5)) # 120
print(factorial.__doc__)
print(type(factorial), type(A)) # <class 'function'> <class 'type'>
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# {'__name__', '__annotations__', '__get__', '__code__', '__kwdefaults__', '__globals__', '__closure__', '__defaults__', '__qualname__', '__call__'}
print(factorial.__name__) # factorial
print(factorial.__code__) # <code object factorial at 0x0000022F6E11C660, file "F:\Programming\Python\Python-Intermediate\p_study\p_Chapter05_1.py", line 9>

print()
print()

# [변수 할당]
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# [함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)]
# map, filter, reduce
print(filter(lambda x: x % 2, range(1,6))) # <filter object at 0x000001F5AF609F88>
print(map(var_func, filter(lambda x : x % 2, range(1,6)))) # <map object at 0x000001F5AF609FC8>
print(list(map(var_func, filter(lambda x: x % 2, range(1,6))))) # [1, 6, 120]
print([var_func(i) for i in range(1, 6) if i % 2]) # [1, 6, 120]

print()
print()

# [reduce]
# usage:
# from functools import reduce
# reduce(함수, 반복가능한객체)

from functools import reduce
from operator import add, sub

print(reduce(add, range(1,11))) # 누적계산 : 55
print(reduce(sub, range(1,11))) # 누적계산 : -53
print(sum(range(1,11))) # 누적계산 (더간단)


# [익명함수(lambda)]
# 가급적 주석 작성
# 가급적 익명함수보다는 일반적인 함수 권장
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t : x + t, range(1,11)))

print()
print()

# [callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인]

# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(factorial), callable(3.14))
# (결과값)
# True True True True False
# 3.14는 호출가능한 '함수'가 아니므로, False.

# [partial 사용법 : 인수 고정 -> 콜백 함수 사용]
from operator import mul
from functools import partial

# mul()함수는 2개의 인자를 받아서 반환한다.
print(mul(10,10))

# 인수 고정
five = partial(mul, 5) # 함수를 인수로 전달 가능, five(a) = 5*a
                       # 따라서, mul 함수의 인자중 하나가 5로 고정되었다.
# 고정 추가
six = partial(five, 6) # six() = 5*6
                       # 따라서, mul 함수의 나머지 인자가 6으로 고정되었다.

print(five(10)) # 50
print(six()) # 30
# print(six(10)) -> TypeError: mul expected 2 arguments, got 3, 인자가 총 3개 들어와서 overflow되어 오류가 발생했다.
print([five(i) for i in range(1,11)]) # 5의 배수 형성 : [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five, range(1,11)))) # 좀더 복잡한 5의 배수 형성
