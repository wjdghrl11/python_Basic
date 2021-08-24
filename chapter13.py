# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name':'kim', 'phone' : '01033337777', 'birth' : '870561'} # 키와 밸류값으로 이뤄져있음
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b- ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('f - ', type(f), f)

# 출력
print('a - ', a['name']) # 키가 존재하지않으면 에러가발생
print('a - ', a.get('name1')) # 키가 존재하지않으면 none으로 처리해줌
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 추가
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print()
print('a - ', a.pop('name'))
print('c - ', c.pop('arr'))
print('c - ', c)
print()
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

# in 연산자
print('a - ', 'birth' in a)
print('a - ', 'phone' in a)

# 수정
a['test'] = 'test_dice'

print('a -', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

