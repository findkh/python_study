# 숫자의 종류
print(type(14)) # <class 'int'>
print(type(14.2)) # <class 'float'>
print(type(0)) # <class 'int'>
print(type(0.0)) # <class 'float'>

print("5 + 7 = ", 5+7)
print("5 - 7 = ", 5-7)
print("5 * 7 = ", 5*7)
print("5 / 7 = ", 5/7)

# 정수 나누기 연산자 : 숫자를 나누고 소수점 이하의 자릿수를 떼어 버린 후 정수 부분만 남기는 연산자
print("3 / 2 = ", 3/2) # 1.5
print("3 // 2 = ", 3//2) # 1

# 나머지 연산자 : %
print("5 % 2 = ", 5%2)

# 제곱 연산자 : **
print("2 ** 1 = ", 2**1)
print("2 ** 2 = ", 2**2)
print("2 ** 3 = ", 2**3)

# 연산자의 우선 순위
# 곱셈과 나눗셈이 덧셈과 뺄셈보다 우선한다.
# 곱셈/나눗셈과 덧셈/빨셈처럼 같은 우선순위를 가지는 연산자는 왼쪽에서 오른쪽 순서로 계산한다.
print(2 + 2 - 2 * 2 / 2 * 2) # 0.0
# 괄호로 감싸줄 것....

# TypeError 예외
# 서로 다른 자료를 연산하면 TypeError 예외가 발생한다.

# 문자열 연산자의 우선순위
# 문자열에 적용하는 연산자도 우선순위를 갖는다.
print("안녕", "하세요 " * 3) # 안녕 하세요 하세요 하세요
print(("안녕" + "하세요 ") * 3) # 안녕하세요 안녕하세요 안녕하세요

print(2 - 2 + 2 / 2 * 2 + 2) # 4.0