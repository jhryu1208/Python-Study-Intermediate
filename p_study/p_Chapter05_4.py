# Chapter 05_4
# 일급 함수(일급 객체)
# 클로저 기초
# 데코레이터(Decorator)

# Decorator의 사전적 의미는 꾸며주는 사람, 장식
# 파이썬에서는 보통 함수이름 앞에 붙어 사용되며, 기존의 함수의 기능을 수정하지 않고 추가적인 기능을 확장해 주는 역할을 한다.
# 데코레이터는 주로 프로그램의 로깅정보를 남기거나 디버깅 할때, 공통적인 전처리 기능이 필요한 함수들 (ex. 웹페이지 호출)
# 을 호출때 많이 사용된다.

# decorator 형식을 보기에 앞서 파이썬에서는 함수(function)은 일급객체(first- class object)개념이 선행되어야 한다.
# first-class obj란 함수의 매개변수나 반환값이 될 수 있으며, 할당명령과 비교명령이 가능한 객체이다.
# 파이썬에서 함수가 일급객체로 사용될 수 있따는 의미는 함수가 매개변수로 전달될 수도 있고 반환될 수도 있따는 의미이다.
# decorator는 함수를 매개변수로 넘겨주어 기존함수에 부가적인 기능을 덧붙여 사용할 수 있도록 도와준다.

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
        # join을 이용하여 리스트를 문자열로 반환. ', '을 통해 a, b, c, d 이런식으로 문자열을 반환함을 알 수 있다.
        # 또한, join함수 사용시, 목록의 요소가 문자열이 아닌 경우(ex. 실수, 정수) repr 또는 str을 사용하여
        # 문자열로 변환 할 수 있다.
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
