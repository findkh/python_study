# 사용자 입력
# -> input
a = input()
print(a)

# 프롬프트 값을 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요: ")
print(number)

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다.
print("life" "is" "too short")
print("life" + "is" + "too short")

# 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')