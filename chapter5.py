# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# camel Case : numberOfCoLLegeGraduates → Method 메소드
# Pascal Case : NumberOfCoLLegeGraduates → class 클래스
# snake Case : number_of_callage_graduater → 다 소문자

# 허용하는 변수 선언 법
age = 1
Age = 1
aGe = 1
AGE = 1
a_g_e = 5
_age = 5
age = 7
age_ = 7
_AGE_ = 7

# 예약어는 변수명으로 불가능
