# 멀티라인 입력
# 역슬래시 사용 
multi_str = \
'''
String
문자열
멀티라인 입력
'''

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are yoi doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswitj, count, endswith, isalpha....)
print("Capitalize : ", str_o1.capitalize())
print("endswith? : ", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", "Good"))
print("sorted :", sorted(str_o1))
print("split :", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 

# 출력
for i in im_str:
    print(i)