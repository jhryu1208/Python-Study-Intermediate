# Chapter 05_1
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

def factorial(n):
    ''' Factorial Function -> n : int '''
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

class A:
    pass

print(factorial(5)) # 120
print(factorial.__doc__)
print(type(factorial), type(A)) # <class 'function'> <class 'type'>
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# {'__name__', '__annotations__', '__get__', '__code__', '__kwdefaults__', '__globals__', '__closure__', '__defaults__', '__qualname__', '__call__'}
print(factorial.__name__) # factorial
print(factorial.__code__) # <code object factorial at 0x0000022F6E11C660, file "F:\Programming\Python\Python-Intermediate\p_study\p_Chapter05_1.py", line 9>

print()
print()

# [변수 할당]
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# [함수]
