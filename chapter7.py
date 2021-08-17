# 형 변환 실습
a = 3.
b = 6
c = .7 
d = 12.7
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 타입 출력
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # true : 1 , false : 0 외워야함
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 → 숫자형
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 많이쓰인다

print(x,y)
print(pow(5,3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)