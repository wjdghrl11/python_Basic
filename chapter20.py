# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 - 리소스(메모리) 할당
# 람다는 즉시 실행 함수(heap 초기화) - 메모리 초기화
# 남발 시 가독성 오히려 감소ㅓ

# def mul_func(x, y):
    # return x * y

# lambda x, y:x*y

# 일반적함수 - 할당
def mul_func(x, y):
    return x * y

q = mul_func(10, 50)

mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다 함수 - 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y:x * y)