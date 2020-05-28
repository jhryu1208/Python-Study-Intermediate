# Chapter 04_1
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# [지능형 리스트(Comprehending lists)]

# 아래의 str형을 list의 객체처럼 바꿀려고 하면 에러가 생긴다. ex) chars[2] = 'h'
# 왜냐하면 str 자료형은 '플랫', '불변'이기 때문이다.
# 만약 시도하게 되면 다음의 오류가 출력된다. -> TypeError: 'str' object does not support item assignment
chars = '+_C$%%$&(*@#('

code_list1 = []
for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)
# (결과값)
# [43, 95, 67, 36, 37, 37, 36, 38, 40, 42, 64, 35, 40]

# compreshending lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# [comprehending lists + Map, Filter]
# filter?
# filter 함수는 첫번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈
# 반복 가능한 자료형을 받는다. 그리고 두번째 인수인 반복 가능한 자료형 요소가 첫 번쨰
# 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.

# map?
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력 받는다.
# map은 입력받은 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려주는 함수이다.
# 또한 map또 반복가능한 결과물을 산출한다.

# 따라서  code_list4에서는,
# map(ord, chars)에서 반복가능한 str 자료형인 chars를 ord함수가 입력받아서 생긴 유니코드 묶음이
# filter의 두번째 인수로 들어간다. 그리고, 그 인수들은 lambda함수에서 True인값만 출력된다.
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)
# (결과값)
# [43, 95, 67, 42, 64]

# 전체 출력
print(code_list1)
print(code_list2)
# (결과값)
# [43, 95, 67, 36, 37, 37, 36, 38, 40, 42, 64, 35, 40]
print(code_list3)
print(code_list4)
# (결과값)
# [43, 95, 67, 42, 64]
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
# (결과값)
# ['+', '_', 'C', '$', '%', '%', '$', '&', '(', '*', '@', '#', '(']
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
# (결과값)
# ['+', '_', 'C', '*', '@']

print()
print()


# [Generator 생성]
# arry는 '플랫','가변'이다.
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 x)

# comprehending list[]에서는 이미 메모리를 소진하여 tuple_g의 값을 출력하였다.
tuple_g = [ord(s) for s in chars]
print(tuple_g)
# (결과값)
# [43, 95, 67, 36, 37, 37, 36, 38, 40, 42, 64, 35, 40]

# 하지만, generator()에서는 print로 tuple_g의 값을 출력하여도, 변환값들을 출력하지않고, 첫번째 객체부터 출력할 준비인 상태가 된다.
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)
# (결과값)
# <generator object <genexpr> at 0x000001AEE4F5FE48>
print(array_g)
# (결과값)
# array('I', [43, 95, 67, 36, 37, 37, 36, 38, 40, 42, 64, 35, 40])

print(type(tuple_g))
# (결과값)
# <class 'generator'>
print(type(array_g))
# (결과값)
# <class 'array.array'>

print(next(tuple_g)) # 43
print(next(tuple_g)) # 95
print(next(tuple_g)) # 67
print(next(tuple_g)) # 36
print(next(tuple_g)) # 37
print(next(tuple_g)) # 37
print(next(tuple_g)) # 36
print(next(tuple_g)) # 38
print(next(tuple_g)) # 40
print(next(tuple_g)) # 42
print(next(tuple_g)) # 64
print(next(tuple_g)) # 35
print(next(tuple_g)) # 40
# print(next(tuple_g)) -> StopIteration (값을 모두 출력했기 때문이다)

print(array_g.tolist()) # .tolist() : array를 list로 만들어주는 함수
# (결과값)
# [43, 95, 67, 36, 37, 37, 36, 38, 40, 42, 64, 35, 40]

print()
print()


# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))
# (결과값)
# <generator object <genexpr> at 0x000001C92BA2FE48>

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)
# (결과값)
# A1 ~ D20

print()
print()


# [리스트 주의]
marks1 = [['~'] * 3 for _ in range(4) ]
marks2 = [['~'] * 3] * 4 # 이때 * 4 는 id를 고대로 복사함.

print(marks1)
# (결과값)
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

print(marks2)
# (결과값)
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]


marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
# (결과값)
# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

print(marks2)
# (결과값)
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']] -> 4 객체의 id가 모두같기 때문에

# 증명
print([id(i) for i in marks1])
# [2627982040584, 2627982040520, 2627982040392, 2627982040328]
# 아이디가 모두 다름

print([id(i) for i in marks2])
# [2627982040200, 2627982040200, 2627982040200, 2627982040200]
# 아이디가 모두 같음
