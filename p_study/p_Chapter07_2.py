# Chapter 07_2
# AsyncIO
# : 비동기 프로그래밍을 위한 모듈이며 CPU작업과 I/O(입출력)을 병렬로 처리하게 해줌

# 이벤트 루프 (event_loop)
# 이벤트 루프는 작업들을 루프를 돌리면서 하나씩 실행시키는 역할을 한다.
# 만약 실행된 작업이 특정한 데이터를 요청하고 응답을 기다려야 한다면, 이 작업은 다시 이벤트 루프에 통제권을 넘겨준다.
# 통제권을 받은 이벤트 루프는 다음 작업을 실행하게 된다.
# 그리고 응답을 받은 순서대로 멈췄던 부분부터 다시 통제권을 가지고 작업을 마무리한다.

# 코루틴 (coroutine)
# 위와 같은 이벤트 루프 작업은 파이썬에서 코루틴으로 이루어져 있다.
# 코루틴은 응답이 지연되는 부분에서 이벤트 루프에 통제권을 줄 수 있으며,
# 응답이 완료되었을 때 멈추었던 부분부터 기존의 상태를 유지한 채 남은 작업을 완료할 수 있는 함수를 의미한다.
# 파이썬에서 코루틴이 아닌 일반적인 함수는 서브루틴이라고 한다.

# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기
# NonBlocking I/O : 호출된 함수(서브루틴)가 return 후 호출한 함수(메인루틴)에 제어권 전달 -> 타함수는 일 지속

# 쓰레드 단점 : 디버깅, 자원 접근 시 레이스 컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 x -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현이 되어 있어야 하거나, 또는 직접 비동기로 구현해야 한다.


import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#################################################################
# 파이썬에서 비동기를 사용하기 위해서는 asyncio 모듈을 이용한다.#
#################################################################
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup
# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예 : 게시판성 커뮤니티)
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com', 'https://tistory.com', 'https://front.wemakeprice.com/main']

##################################################################################################
# 함수앞에 async를 붙이면 코루틴을 만들 수 있다.                                                 #
# 또한, 병목이 발생해서 다른 작업으로 통제권을 넘겨줄 필요가 있는 부분에서는 await을 써준다.     #
# 이때, await 뒤에 오는 함수도 코루틴으로 작성되어야 한다.                                       #
##################################################################################################
async def fetch(url,executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url) # threading을 import 했기에 가능

    #########################################################################################################
    # 파이썬의 대부분의 라이브러리들은 비동기를 고려하지 않고 만들어졌기 때문에 비동기로 이용할 수 없다.    #
    # 하지만, 이벤트 루프의 run_in_executor함수를 이용하면 가능하다.                                        #
    # run_in_executor(executor, func, *args)                                                                #
    # func에 대해서 지정한 executor에서 실행되도록 조정한다.                                                #
    #########################################################################################################
    # urlopen은 비동기 코루틴이 아닌 일반 함수이므로, HTTP 요청을 보낸 후 응답을 받을 때까지 블럭되는 함수이다.
    # 따라서, run_in_executor를 이용하여 병렬적으로 동작하는 코루틴으로 완전하게 전환시켰다.
    res = await loop.run_in_executor(executor, urlopen, url)

    soup = BeautifulSoup(res.read(), 'html.parser')

    # 전체 페이지 소스 확인
    # print(soup.prettify())
    result_data = soup.title

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)

    # 결과 반환
    return result_data

async def main(): # 다른 제네레이터 와 Closure등과 구분하기위해 def 앞에 async를 붙인다. (비동기 함수임을 나타냄)

    ###############################################################################
    # max_workers에 따라서 실행시간이 달라진다.                                   #
    # (하지만 workers가 많아질수록 컨텍스트 스위칭 비용도 커진다.)                #
    # None으로 하는 경우 디폴트로 설정한 workers수가 작아서 훨씬 더 오래 걸린다.  #
    ###############################################################################
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    #############################################################
    # asyncio.ensure_future함수는 Task를 현재 실행하지 않고,    #
    # 이벤트 루프가 실행될 때 실행할 것을 보증해주는 함수       #
    #############################################################
    # fetch 함수를 실행하지 않고, 이벤트 루프가 실행될 때 실행할 것을 보증하겠다.
    futures = [
        asyncio.ensure_future(fetch(url,executor)) for url in urls
    ]

    ##########################################################################################
    # 비동기로 두 개 이상의 작업(코루틴)을 돌릴 때에는 asyncio.gather함수를 이용해야한다.    #
    # 이때, 각 Task들은 unpacked 형태로 넣어주어야 한다.                                     #
    ##########################################################################################
    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print('result : ', rst)


if __name__=='__main__':
    ##########################################################################################
    # 코루틴으로 태스크를 만들었다면, asyncio.get_event_loop함수를 활용해 이벤트 루프를 정의 #
    ##########################################################################################
    # 루프 초기화
    loop = asyncio.get_event_loop()

    ##################################################
    # run_until_complete 함수를 이용하여 loop를 실행 #
    ##################################################
    # 작업 완료 까지 대기
    loop.run_until_complete(main()) # main함수가 끝날때까지 loop를 돌리겟다.

    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)
