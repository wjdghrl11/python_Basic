# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError,NameError, IndexError, ValueError, KeyError...
# 문법적으로 예외가 없지만, 코드 실행 프로세스(단계), 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다. 
# 3. 예외는 던져진다.
# 4. 예외 무시

# syntaxerror : 문법 오류
# print('error)
# print('error'))
# if True

# NameError : 참조없음
# a = 10
# b = 15
# print(c)


# zerodivisionerror
# print(100 / 0)

# # indexerror
# x = [50,70,90]
# # print(x[5])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# keyerror

# dic = {'name' : 'lee', 'age' : 41, 'city' : 'busan'}
# print(dic['hobby'])
# print(dic.get)

# 예외 없는 것을 가정하고 프로그램 작성 - 런타임 예외 발생 시 예외 처리 권장(eafp)