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

# while
w = iter(t)
print(dir(w)) # __Iter__, __next__

print(next(w)) # A
print(next(w)) # B
print(next(w)) # C
print(next(w)) # D
# print(next(w)) # StopIteration

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# [반복형 확인]
# 지금까지 사용한 원시적인 방법
print(dir(t)) # __Iter__

# hasattr : x속성을 가지고있니?
# ussage:
# hasattr(인수,'인수 확인하고자 하는 속성')
print(hasattr(t, '__iter__')) # True

# Iterable class를 상속받았는지 확인하는 방법
from collections import abc
print(isinstance(t, abc.Iterable)) # True
