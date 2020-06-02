# Chapter 05_4
# 일급 함수(일급 객체)
# 클로저 기초
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용 용이

# 단점
# 1. 데코레이터남발시 가독성 감소
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편


# [데코레이터 실습]
import time

# 데코레이터 perf_clock 함수
# func는 변수인자가 아니라 함수인자를 받음을 의미한다.
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st # 걸린시간 = 종료 시간 - 시작 시간
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

# perf_clock함수에 넣기 위한 구현하고 싶은 함수 구현1
@perf_clock # 데코레이터
def time_func(seconds):
    time.sleep(seconds)

# perf_clock함수에 넣기 위한 구현하고 싶은 함수 구현2
@perf_clock # 데코레이터
def sum_func(*numbers):
    return sum(numbers)

# [데코레이터 미사용 (Closure 이용됨) ]
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
# <function perf_clock.<locals>.perf_clocked at 0x0000027F3D145048> ('func',)
print(none_deco2, none_deco2.__code__.co_freevars)
# <function perf_clock.<locals>.perf_clocked at 0x0000027F3D1450D8> ('func',)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
# ---------------------------------------- Called None Decorator -> time_func
#
# [1.50012s] time_func(1.5) -> None

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco2(100, 200, 300, 400, 500)
# ---------------------------------------- Called None Decorator -> time_func
#
# [0.00000s] sum_func(100, 200, 300, 400, 500) -> 1500
# [Finished in 1.588s]

print()
print()

# [데코레이터 사용]
print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
# ---------------------------------------- Called Decorator -> time_func
#
# [1.50023s] time_func(1.5) -> None

print('-' * 40, 'Called Decorator -> time_func')
print()
sum_func(100, 200, 300, 400, 500)
# ---------------------------------------- Called Decorator -> time_func
#
# [0.00000s] sum_func(100, 200, 300, 400, 500) -> 1500
