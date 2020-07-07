# Chapter 06_02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# 제네레이터(Generator)?
# 파이썬의 제네레이터는 yield라는 키워드를 이용하여 함수 안에서 반복자(iterator)를 생성해 주는 함수 입니다.
# 제네레이터 함수는 return 값이 없다.
# 제네레이터 함수에서 가장 중요한 예약어는 yield이다.
# yield는 반복자를 생성해주는 구문이며 yield를 호출하면 반복자가 생성되면서
# 해당 제네레이터를 호출한 문장으로 반복자가 반환된다.
# 명시적인 return은 없지만 yield가 생산된 반복자 객체를 반환하는 형식으로 동작한다.


# Generator ex1
def generator_ex1():
    print('Start')
    yield 'A point'
    print('Continue')
    yield 'B point'
    print('End')

temp = generator_ex1()

# print(temp)
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

# Generator ex2
temp2 = [x*3 for x in generator_ex1()]
temp3 = (x*3 for x in generator_ex1())

print(temp2)

print(temp3)
for i in temp3:
    print(i)

print()
print()

# Generator_ex3(중요함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)


print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n<3, [1,2,3,4,5])
for v in gen3:
    print(v)


print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,101)])

for v in gen4:
    print(v)


print()

# 연결1
gent5 = itertools.chain('ABCDE', range(1,11,2))

print(list(gent5))


print()

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))


print()

# 개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=4)

print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AABBCCCDDDEEEEE')

# print(list(gen9))
for chr, group in gen9:
    print(chr, ':', list(group))
