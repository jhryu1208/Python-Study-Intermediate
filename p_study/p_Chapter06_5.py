# Chapter 06_5
# Future 동시성
# 비동기 작업 실행

# A->B->C->D
# cf) 동기
# A를 끝내고 B를 시작, B를 끝내고 C를 시작, ...
# cf) 비동기
# A를 시작하면서 B를 시작, B를 시작하면서 C를 시작, ...

# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념


# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed
# wait -> 인스턴스가 완료될때 까지 기다린다. (기다리는 시간 제어 가능)
# as_completed -> 먼저 끝나는 대로 반환

# GIL(Global Interface Lock) : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#                              GIL 실행, 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)
#                              하지만 GIL로 인해 동기적으로 시행하는것 보다 시스템이 느려질 수 있다.

#                              따라서, 이를 우회하기 위해서 다음과 같은 우회 방법을 사용한다. ***멀티프로세싱 사용, Cpython (GIL우회 방법)

# 따라서, 쓰레드를 많이 쓴다고 좋은 것이 아니다.
# 적합한 프로그램의 로직을 보고 그것에 적합하게 멀티프로세싱을 사용하는 것이 중요.

import os    # 운영체제와의 상호작용을 돕는 다양한 기능을 제공
import time  # 시간측정을 위해서
#from concurrent import futures, wait, as_completed
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait, as_completed

WORK_LIST = [1000000, 10000000, 100000000, 1000000000] # 동시에 1~10000, 1~100000, 1~1000000, 1~10000000 까지의 합을 구해보자.

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST)) # Worker의 갯수가 미정이지만 10이하인 경우

    # 시작 시간
    start_tm = time.time()
    futures_list = []
    #
    # 결과 건수
    # 스레드 -> ProcessPoolExecutor
    # 프로세스 -> ThreadPoolExecutor
    with ProcessPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        for work in WORK_LIST:
            future = excutor.submit(sum_generator, work) # 미래의 할 일 들을 반환
            # 스케쥴링
            futures_list.append(future) # futures_list에 일을 추가
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # result = wait(futures_list, timeout=7) # (****)wait의 옵션중 timeout을 이용하면, 어떤 업무가 지정된 시간안에 결과를 반환못하면, 그 업무를 실패한 것으로 간주하고 중단한다
        #
        # # 성공
        # print('Completed Tasks : ' + str(result.done))
        #
        # # 4 가지 업무 모두 성공했을 경우
        #
        # # Completed Tasks : {<Future at 0x22235dff408 state=finished returned int>,
        # # <Future at 0x22235e50948 state=finished returned int>,
        # # <Future at 0x22235e50848 state=finished returned int>,
        # # <Future at 0x22235e50a08 state=finished returned int>}
        #
        # # 모두 state=finished 상태로 표시된다.
        #
        # # 1 가지 업무를 실패 했을 경우
        #
        # # Completed Tasks : {<Future at 0x26fce970908 state=finished returned int>,
        # # <Future at 0x26fce91e448 state=finished returned int>,
        # # <Future at 0x26fce970a08 state=finished returned int>}
        #
        # # 실패된 한가지의 일이 표시가 안된다.
        #
        #
        # # 실패
        # print('Pending ones after waiting for 7seconds : ' + str(result.not_done))
        #
        # # 실패된 결과 값 표시
        # # Pending ones after waiting for 7seconds : {<Future at 0x1f3b6220b08 state=running>}
        #
        # # 결과값 출력
        # print([future.result() for futur in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result,done))
            print('Future Cancelled : {}'.format(cancelled))

            # Future Result : 500000500000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x1b7420fe448 state=finished returned int>>
            # Future Result : 50000005000000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x1b742150788 state=finished returned int>>
            # Future Result : 5000000050000000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x1b742150888 state=finished returned int>>
            # Future Result : 500000000500000000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x1b742150948 state=finished returned int>>

            # True -> 완료되었음, state=finished -> 캔슬된게 없음

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포멧
    msg = '\n Time : {:.2f}s'

    # 최종 결과 출력
    print(msg.format(end_tm))


# 실행
# 멀티프로세싱의 시작점
if __name__ == '__main__':
    main()

# if __name__ == '__main__':
# 은 로컬파일과 외부파일을 구분해서 사용할 때 유용하다.
# 예를들어 아래와 같은 caculation.py가 있다 가정하자.

# def plus(a,b):
#     return a+b
#
# def minus(a,b):
#     return a-b
#
# def multiply(a,b):
#     return a*b
#
# def divide(a,b):
#     return a/b
#
# print(divide(33,3))
# print(plus(10,4))
#
# 이때 이 파일은 print문도 기록되어있다.
# 따라서, 4칙연산이 필요한 외부에서 import calculation 할 경우 불필요한 print문까지 출력되어진다.
#
# 그러므로, print문을 제외한 나머지 함수를 사용하기 위해서
# 다음과 같이 if __name__ == '__main__':을 이용하는 것이다.
#
# def plus(a,b):
#     return a+b
#
# def minus(a,b):
#     return a-b
#
# def multiply(a,b):
#     return a*b
#
# def divide(a,b):
#     return a/b
#
# if __name__ == '__main__':
# print(divide(33,3))
# print(plus(10,4))

# if __name__ == '__main__':는 로컬파일에서 사용할경우 파이썬은 자동으로 __name__ 을 __main__이라고 할당한다.
# 그러므로, 로컬파일에서는 print문까지 출력이된다.

# 하지만 외부파일에서 import되서 사용되어질 경우 __name__은 해당파일의 이름으로 할당된다.
# 예를들어 위의 calculation.py가 외부에서 호출되면 __name__은 calculation으로 할당된다.
# 따라서,  __name__과 __main__은 불일치하게되어, print문은 출력이 되지 않는다.

# 결론적으로, 이렇듯, __name__ 을 활용하여 직접 돌리는 코드와 import 하는 코드를 구분하여 원하는 코드 플로우가 될 수 있도록 설정할 수 있겠다.
