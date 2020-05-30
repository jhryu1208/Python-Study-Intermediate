# Chapter 04_4
# 시퀀스 형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 x, Set -> 중복 허용 x
# Dict 및 set 심화

# [immutable dict]
from types import MappingProxyType

d = {'key1' : 'value1'} # d는 수정이 가능

# Read Only
d_frozen = MappingProxyType(d) # d_frozen은 수정이 불가능

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가
# d_frozen['key2'] = 'value2' -> TypeError: 'mappingproxy' object does not support item assignment

print()
print()


s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # not {}, 빈 원소인 set도 왼쪽과 같이 표시해야함, 만약 {}라 할경우 dict로 클레스 표기됨
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# set 추가
s1.add('Melon')
print(s1)

# set 추가 불가
# s5.add('Melon')
# print(s5) -> AttributeError: 'frozenset' object has no attribute 'add'

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5)) # <class 'frozenset'>

# [선언 최적화]
# 바이트 코드 -> 파이썬 인터프리터가 바이트 코드 실행
from dis import dis

print('------------')
print(dis('{10}'))

# ------------
#  1           0 LOAD_CONST               0 (10)
#              2 BUILD_SET                1
#              4 RETURN_VALUE
# None

print('------------')
print(dis('set([10])'))

# ------------
#  1           0 LOAD_NAME                0 (set)
#               2 LOAD_CONST               0 (10)
#               4 BUILD_LIST               1
#               6 CALL_FUNCTION            1
#               8 RETURN_VALUE
# None

# 따라서 set()함수를 이용하는 것보다 {}를 이용한 set선언이 더 효율적임을 알 수 있다.


# [지능형 집합(Comprehending Set)]

print('-----------')
from unicodedata import name
print({name(chr(i), '') for i in range(0,256)})
