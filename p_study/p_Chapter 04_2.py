# Chapter 04_2
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# [Tuple Advanced]
# [unpacking - 중요!!!!!!!!!!!]

# c/c++에서는 temp알고리즘을 이용하여  서로의 자리값을 바꾸지만,
# 파이썬의 경우는 다음과 같이 간단하다.
# b, a = a, b

# divmod 함수는 몫과 나머지를 반환한다.
print(divmod(100, 9)) # (11, 1)
# 만약 divmod에 튜플을 넣게 된다면, *를 이용하여 unpacking해줘야한다.
# *없이 튜플을 대입한다면 error가 발생한다.
print(divmod(*(100, 9))) # (11, 1)
# 또한, divmod에 *을 붙여주면 divmod로 반환된 튜플 값이 unpacking되어 출력된다.
print(*(divmod(100,9))) # 11 1

print()

x, y, *rest = range(10)
print(x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest) # 0 1 []
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3, 4, 5]

print()
print()

# [Mutable (가변), Immutable (불변)]

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l)) # (15, 20, 25) 2454764034072
print(m, id(m)) # [15, 20, 25] 2454764001032

l = l * 2
m = m * 2

# 이때, l(튜플)과 m(리스트)의 id값이 달라진 것을 확인 할 수 있다.
# 왜냐하면, 두배로 반환된 l 과 m은 새로운 변수로 취급하는 l 과 m에 들어갔기 떄문이다.
# 쉽게말하자면, 같은 아파트의 다른 방호수에 들어간 것이다.
print(l, id(l)) # (15, 20, 25, 15, 20, 25) 2454763937512
print(m, id(m)) # [15, 20, 25, 15, 20, 25] 2454764051528

l *= 2
m *= 2

# 위에서와 달리, l(튜플)은 id값이 변경된 것에 비해서, m(리스트)는 id값이 변경되지않았다.
# 왜냐하면, 위의 방식에서는 같은 변수에 저장되는 방식이기 때문이다.
# 따라서, 가변형인 리스트는 같은 id값에 반환값이 저장된 것이다.
# 하지만, 튜플은 불변형이기 때문에 새로운 id값에 저장된 것이다.
print(l, id(l)) # (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 2454762600056
print(m, id(m)) # [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 2454764051528

print()
print()

# [sort vs sorted]
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본에 훼손 x)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list)) # sorted -  ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry'] -> abc순서대로 정렬됨
print(f_list) # ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut'] -> 원본은 그대로!!

print('sorted - ', sorted(f_list, reverse=True))                       # sorted -  ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple'] -> abc거꾸로!
print('sorted - ', sorted(f_list, key=len))                            # sorted -  ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry'] -> 글자길이 순서대로!
print('sorted - ', sorted(f_list, key=lambda x : x[-1]))               # sorted -  ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry'] -> 끝에 글자를 기준으로 abc정렬!
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse=True)) # sorted -  ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya'] -> 위의 결과를 리버스!


# sort : 정렬 후 객체 직접 변경 (원본이 변경됨)

# 반환 값 확인(None)
print('sort - ', f_list.sort()) # sort -  None
# 여기서 f_list.sort()의 출력값인 None은 순서대로 정렬되었음을 의미한다.
# 따라서 f_list를 출력하면 다음과 같이, 원본이 정렬되어 저장되어있음을 확인 할 수 있다.
print(f_list) # ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']

print('sort - ', f_list.sort(reverse=True), f_list)                         # sort -  None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple'] * abc정렬 리버스
print('sort - ', f_list.sort(key=len), f_list)                              # sort -  None ['mango', 'lemon', 'apple', 'papaya', 'orange', 'coconut', 'strawberry'] * 길이순
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)                 # sort -  None ['papaya', 'apple', 'orange', 'lemon', 'mango', 'coconut', 'strawberry'] * 맨끝자리 abc정렬
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse = True), f_list) # sort -  None ['strawberry', 'coconut', 'mango', 'lemon', 'apple', 'orange', 'papaya']

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환), 숫자로만 되어있는 정보를 처리하는 경우 유용!
