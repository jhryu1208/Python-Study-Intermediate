# Chapter 06_01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text, list, Dict, Set, Tuple, unpacking, *args... : Iterable

# 반복 가능한 이유 -> 내부적으로 iter(x) 함수가 호출되었기 때문에
t = 'ABCD'
print(dir(t)) # __Iter__

for c in t:
     print(c)

# [while]
# Iter는 객체의 __iter__메서드를 호출해준다.
# iterator는 next()함수로 데이터를 순차적으로 호출 할 수 있는 객체이다.
# Iterator를 만드는 방법으로, iterable한 객체에 파이썬 내장함수 iter()를 사용해서 만든다.

w = iter(t)
print(dir(w)) # __Iter__, __next__

print(next(w)) # A
print(next(w)) # B
print(next(w)) # C
print(next(w)) # D
# print(next(w)) # StopIteration

# while 반복문의 조건을 True로 설정 -> 무한반복
# Try에는 오류가 발생할 수있는 코드를 작성
# 해당 Stop Iteration 에러가 발생하면 excpet문이 실행됨

# (복습) else: 는 오류가 발생하지 않았을 때 수행할 코드
#        finally: 는 오류 발생에 상관없이 수행하는 코드
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# [반복형 확인]
# 1. 지금까지 사용한 원시적인 방법
print(dir(t)) # __Iter__

# 2. hasattr : x속성을 가지고있니?
# ussage:
# hasattr(인수,'인수 확인하고자 하는 속성')
print(hasattr(t, '__iter__')) # True

# 3. Iterable class를 상속받았는지 확인하는 방법
# abc는 abstract base classes를 의미한다.
from collections import abc
# isinstace는 해당 값의 자료형을 확인하고, 일치하면 True, 그렇지 않으면 False를 반환한다.
# 또는 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지 판단.
# __iter()__메서드를 구현하고 있다면 abc.Iterable 서브클래스로 판단.

# ussage:
# isinstance(obj, class_or_tuple, /)
print(isinstance(t, abc.Iterable)) # True
print(abc.Iterable) # <class 'collections.abc.Iterable'>

print()
print()

# next
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplitter(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tommorrow')
print(wi)
