# 값 비교
a = []
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
c[0] = 4
print('c = ', c)
c[2] = 100
print('c = ', c)
c[0:1] = ['a', 'b', 'c'] # 슬라이싱 범위를 지정했을때는 그냥 원소
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 몇번 인덱싱에 리스트를 넣어달라고했을때는 리스트가 통째로 들어감
print('c -', c)
c[1:3] = [] # 삭제 다른방법이있음
print('c -', c)
del c[2] # del 함수
print('c -', c)

# 리스트 함수
a = [5, 2 ,3, 1, 4]
print('a - ', a)
a.append(10) # 끝 부분에다가 데이터를 삽입
print('a - ', a)
a.sort() # 오름차순 정렬
print('a - ', a)
a.reverse()
print('a - ', a) # 들어있는 데이터를 반대로출력
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a) # 7이 2자리로 삽입되고 나머지는 뒤로밀림
a.reverse()
print('a - ', a)
a.remove(10) # 값을쓰면 값이 삭제가된다
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 내가 찾는 값이 몇개가 들어있는지, 확인할때
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)