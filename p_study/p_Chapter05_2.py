# Chapter 05_2
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# [ex1]
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) -> 인자 b가 없으므로 에러

# [ex2]
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# ex2를 통해 알 수 있는 것은 파이썬에서 선언된 함수는 지역변수말고도,
# 파이썬 내부 인터프리터를 통해서,
# 글로벌 변수 또한 함수내에서 받아들인다는 것을 알 수 있다.

# [ex3-1]
c = 30

def func_v3(a):
    c = 40      # print()위에 지역변수 c를 선언할 경우 정상 출력되는 것을 확인 할 수 있다.
    print(a)
    print(c)
#   c = 40 -> c변수가 하단에서 선언된 경우,
#             UnboundLocalError: local variable 'c' referenced before assignment
#             의 에러 문구에서 global 변수보다 local변수가 먼저 참조되는 것을 알 수있다.

print('global ', c) # 이때는 glbal 변수 c = 30이 출력됨을 확인 할 수 있다.
func_v3(10) # 10 40

# 하지만, 함수내에서 지역변수가 선언되어있어도, 글로벌 변수를 사용 할 수 없는 것은 아니다.
# 다음 예제를 참조하자.

# [ex3-2]
c = 30

def func_v4(a):
    global c # global 변수 c 호출
    print(a)
    print(c)
    c = 40  # local 변수를 하단에 선언

print('global ', c) # 30
func_v4(10) # 10 30 -> local 변수가 선언되어 있음에도 불구하고, global 변수 c가 쓰였음을 확인 할 수있다.

# 하지만, global 변수 c를 다시 출력해보면 40이 출력됨을 확인 할 수있다.
# 글로벌 변수 c의 값이 지역변수 c의값으로 바뀌었다.
print('local -> global ', c)

# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착 상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경하지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그램에 강점
# 더 간단하게, 클로저는 불변인 상태를 기억한다.

a = 100

print(a + 100)  # 200
print(a + 1000) # 1100

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

# 클래스 이용
class Averager():
    def __init__(self):    # __init__은 인스턴스 초기화 할때 사용.
        self._series = []

    def __call__(self, v): # __call__은 인스턴스가 호출됐을때 실행된다.
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager() # 클로저 함수는 변수를 한번 거쳐야한다.

# 누적

print(averager_cls(10)) # 클래스를 함수처럼 사용하는 것에 한번 주목
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
print(averager_cls(90))

# inner >> [10] / 1
# 10.0
# inner >> [10, 30] / 2
# 20.0
# inner >> [10, 30, 50] / 3
# 30.0
# inner >> [10, 30, 50, 70] / 4
# 40.0
# inner >> [10, 30, 50, 70, 90] / 5
# 50.0

# 상태를 누적하고 있음을 확인 할 수 있다.
