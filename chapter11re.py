# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1,2,3...], (1,2,3...)
print(type(False)) #0, "", [], (), {}

# 예1
if True:
    print('Good')

if False:
    print('Bad')

if False:
    print('Bad')
else:
    print('Good')

# 관계 연사
# >, >=, <, <=, == !=

x = 15
y = 10
# 양변이 같은 경우 참
print(x == y)
# 양 변이 다를 때 참
print(x != y)
# 왼쪽이 클 때 참
print(x > y)
# 왼쪽이 크거나 같을 때 참
print(x >= y)
# 오른쪽이 클 때 참
print(x < y)
# 오른쪽이 크거나 같을 때 참
print(x <= y)

city = ""
if city:
    print("you are in:", city)
else:
    print("please enter your city")


city2 = "Seoul"
if city2:
    print("you are in:", city2)
else:
    print("please enter your city")

# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c)
print('or:', a > b > c)
print('not:', not a > b)
print('not:', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
print('e1 :', 3+12 > 7+3)
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'
# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('축하드립니다 합격입니다.')
else:
    print('불합격입니다.')

id1 = 'vip'
id2 = 'admin'
grade = 'Gold'

if id1 == 'vip' or id2 == 'admin':
    print('관리자입니다.')

if id2 == 'admin' and grade == 'Gold':
    print('회장님 등장')

# 다중조건문
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('불합격입니다')

# 중첩 조건문
grade = 'B'
total = 55

if grade == 'A':
    if total >= 90:
        print("장학금 100%")
    elif total >= 80:
        print("장학금 80%")
    else:
        print("장학금 70%")
else:
    print("장학금 50%")

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("Seoul" in e.values())  # value 검색