# 파이썬 기초
# 파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n)) # 자료형을 알려줌
print()

# 동시 선언 다른 언어 golang처럼
x = y = z = 700
print(x,y,z)
print()

# 선언
var = 75

# 재선언
var = 'change Value' # 덮어씀
print(var)
print(type(var))
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
print()

# 예2)
# n  - 777
n = 777
print(n, type(n))
print()

m = n
# m → 777 ← n
print(m, n) # 콤마뒤에는 띄어쓰기를 하는것이좋음
print(type(m), type(n))
print()

m = 400
print(m, n)
print()