#pow : 제곱값반환
print(pow(2,10))

# range : 반복가능한 객체(iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림

print(round(6.5781, 2))
print(round(5.6))

# sorted : 반복가능한 객체(iterable) 정렬 후 반호나
print(sorted([6,7,4,3,1,2]))

a = (sorted([6,7,4,3,1,2]))
print(a)
print(sorted(['P','Y','T','H','O','N']))

# sum : 반복가능한 객체(iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1, 101)))

# type : 자료형 확인
print(type(3))
print(type({}))
print(type({3,4}))
print(type(()))
print(type([]))

# zip : 반복가능한(iterable) 의 요소를 묶어서 반환

print(list(zip([10,20,30],[40,50,60])))
print(type(list(zip([10,20,30],[40,50,777]))[0]))