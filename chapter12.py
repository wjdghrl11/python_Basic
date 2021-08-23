# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언

a = ()
b = (1,) # 튜플은 하나의 원소는 콤마를 써야한다
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1]) # 튜플안에 2자리가 튜플이 들어가있으니 튜플이출력
print('d - ', e[-1][1]) # 튜플안에 1자리인 base가 출력
print('d - ', list(e[-1][1])) # 리스트로 형 변환

# 수정x
# d[0] = 1500

# 슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산 
print('c + d', c + d)
print('c + d', c * 3) # 원소 반복

# 튜플 함수
a = (5, 2, 3, 1, 2)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(packing, and unpacking) 중요함

# 팩킹 
t = ('foo', 'bar', 'baz', 'qux')
print(t)

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)