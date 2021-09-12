# #attributeerror : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# # valueerror

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# fileNotFoundError

# f = open('test.txt')

# TypeError : 자료형에 맞지않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y)) 형 변환을 통해서 실행가능
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# name =  ['Kim', 'Lee', 'Park']

# # 예제1
# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()    

# print('pass')

# 예제2

# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()    


# # 예제3
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finally!')

# print()    

# print('pass')

# 예제4
# 예외 발생 : raise
# raise  키워드로 예외 직접 발생

# try : 
#     a = 'Park'
#     if a == 'Park':
#         print('OK Pass!')
#     else:
#         raise ValueError
# except ValueError:
#     print('Occurred! Exception!')
# else:
#     print('OK! else!')