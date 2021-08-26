# 집합(set) 특징

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14151}

print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)

# 튜플 변환(set  - tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set - list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 -', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2) # intersection

print('s1 | s2 :', s1 | s2) # union

print('s1 - s2 :', s1 - s2) # difference

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2))

# 부분 집합 확인
print(s1.issubset(s2)) # subset
print(s1.issuperset(s2)) # superset

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
# s1.remove(7) 

s1.discard(3)
print('s1 - ', s1)
s1.discard(7)
print('s1 - ', s1)

s1.clear() # 모든걸 삭제
print('s1 - ', s1)