# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e- ', list(e[-1][1]))

# 슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('e -', e[-1][1:3])

# 리스트 연산
print('c + d', c + d) # 합쳐짐
print('c * 3', c * 3)
print("'Test' + c[0]" 'Test' + str(c[0]))