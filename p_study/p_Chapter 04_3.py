# Chapter 04_3
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# [해쉬 테이블 **중요**]
# key에 value를 저장하는 구조
# 파이썬 dict -> 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key 에 대한 value 참조

# [Dict 구조]
# print(__builtins__.__dict__)

# [Hash 값 확인]
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) -> TypeError: unhashable type: 'list' -> 리스트는 가변이기 때문에

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# [No Use Setdefault]
for k, v in source:                                      # source의 Tuple 객체들이 k, v에 언패킹
    if k in new_dict1:                                   # new_dict1 딕셔너리에 k가 있니?
        print('before addition value?', new_dict1[k])    # (2) 해당 k가 있을경우
        new_dict1[k].append(v)                           # 해당 k라는 key의 value로 v를 추가시킨다.
        print('after addition value', new_dict1[k])
        print()

    else:                               # (1) 해당 k가 없으면
        new_dict1[k] = [v]              # new_dict1[k]는 key가 k인 value값을 반환한다.
                                        # k라는 key에 [v]라는 list value를 가지는 딕셔너리 쌍을 추가시킨다는 의미이다.
        print('key {}\'s value addition is completed :'.format(k), new_dict1[k])
        print()

print(new_dict1)
# (결과값)
# k addition
# key k1's value addition is completed : ['val1']
#
# before addition value? ['val1']
# after addition value ['val1', 'val2']
#
# k addition
# key k2's value addition is completed : ['val3']
#
# before addition value? ['val3']
# after addition value ['val3', 'val4']
#
# before addition value? ['val3', 'val4']
# after addition value ['val3', 'val4', 'val5']
#
# {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}


# [Use Setdefault]
for k, v in source:
    # setdefault(키, 디폴트값) : 키가 있는 경우 그냥 값을 리턴, 키가 없으면 디폴트값으로 새로운 요소를 추가
    new_dict2.setdefault(k, []).append(v)
    print(new_dict2)

print(new_dict2)
# (결과값)
# {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}


# [주의]
new_dict3 = { k : v for k, v in source}
print(new_dict3)
# (결과값)
# {'k1': 'val2', 'k2': 'val5'} -> 같은 key에 다른 value가 계속 덮어쓰기 되어 이런 결과가 나타남.
