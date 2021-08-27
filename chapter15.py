# 파이썬 반복문
# FOR 실습

# 코딩의 핵식
# for in <collection>
#     <loop body>

for v1 in range(10): # n - 1
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1~10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

print()

# 1~1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1~1000 sum :', sum1)

print('1~1000 sum :', sum(range(1, 1001)))

print('1~1000 sum :', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)