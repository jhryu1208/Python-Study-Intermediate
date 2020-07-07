# Chapter 06_03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
# 코루틴(Coroutine)

# 코루틴 : 단일(싱글) 쓰레드, 스텍을 기반으로 동작하는 비동기 작업
# 쓰레드 : os에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield, send: 메인루틴 <-> 서브루틴 (양방향 통신)
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 의 장점 : 쓰레드에 비해 오버헤드가 감소 (단일쓰레드로 진행하기 때문에)
# 쓰레드 : 싱글 쓰레드 -> 멀티 쓰레드 -> 코딩복잡 -> 공유되는 자원 -> DeadLock(교착상태) 발생 가능, 컨텍스트 스위칭(쓰레드끼리의 전환) 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await


# 코루틴 ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()

print(cr1,type(cr1))

# yield 지점까지 서브루틴 수행
# '''
# next(cr1)
# '''
# print('>>> coroutine started.')
# i = yield
# 여기까지 실행

# 서부루틴에서 메인루틴으로 값 전송
# send는 항상 next가 시행된 뒤에 시행되어져야만 한다.
# 왜냐하면, next로 i=yield까지 수행되어져야, send를 통해 보낼 인수가 생긴다.
# 하지만, 처음부터 send를 사용할 경우 보낼 인수가 존재하지 않기 때문에 에러가 생긴다.
# '''
# cr1.send(100)
# '''
# >>> coroutine received : 100


print()
print()


# 코루틴 ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# **GEN_SUSPENDED :  Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x)) # x를 메인 루틴에서 받아서 출력
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate
print(getgeneratorstate(cr3)) # GEN_CREATED

print(next(cr3))
# y = yield x에서 yield x까지 시행되어 x값 10을 반환하였다.
# 따라서, 다음은 y값을 받을 차례이다.
print(getgeneratorstate(cr3)) # GEN_SUSPENDED


cr3.send(100)
# y값이 넘겨졌고,  print('>>> coroutine received : {}'.format(y))이 실행되었다.
# 또한, z = yield x + y 에서 +y에 100이 전달되었다.
# 따라서, 다음은 z값을 받을 차례이다.
print(getgeneratorstate(cr3)) # GEN_SUSPENDED

print()
print()

# 코루틴 ex3
# StopIteration 자동 처리 (python 3.5이상에서는 await으로 자동처리 가능)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2))

print()
print()

# 위를 더욱 간단하게
# yield from : iterable한 데이터를 순차적으로 끝날때 까지 반환하겠다.
def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))
