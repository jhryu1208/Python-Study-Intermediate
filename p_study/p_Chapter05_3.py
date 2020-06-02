# Chapter 05_3
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가ㅓ능

# [Closure 사용]
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []
    def averager(v):
        # (의문1) 리스트는 가변이 가능하기 때문에 nonlocal을 사용하지않았는가?
        series.append(v)
        print('inner >>> {} / {}'.format(series,len(series)))
        return sum(series) /  len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))

print()
print()

# [function inspection(증명)]
print(dir(avg_closure1)) # __closure__확인가능
print()
print(dir(avg_closure1.__code__)) # co_freevars 확인가능
print()
print(avg_closure1.__code__.co_freevars)  # free variable 'series' 확인 가능
print(avg_closure1.__closure__[0].cell_contents) # [10, 20 , 30] 확인 가능

print()
print()

# [잘못된 클로저 사용]
def closure_ex2():
    # Closure_ex2()에 관한 local var인 cnt, total
    # 이때, averager 함수 입장에서는 cnt와 total이 Free variable이다.
    cnt = 0
    total = 0
    def averager(v):
        # averager()에 관한 local var인 cnt와 total
        # 이때 cnt와 total은 closure_ex2()함수에 있는 변수와 이름이 같을뿐이지 새로운 변수에 해당한다.
        # 따라서, 아래와 같이 cnt가 선언에 관하여 에러가 발생한다.
        cnt += 1
        total += v
        return total / cnt

    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(10)) -> UnboundLocalError: local variable 'cnt' referenced before assignment

# [잘못된 클로저 수정]
def closure_ex3():
    cnt = 0
    total = 0
    def averager(v):
        # 현재 함수의 바깥쪽에 있는 지역변수의 값을 변경하려면 nonlocal 키워드를 사용해야한다.
        # 따라서, 다음과 같이 함수 안에서 nonlocal 에 지역 변수의 이름을 지정해준다.
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure1(10))
print(avg_closure1(25))
print(avg_closure1(40))
