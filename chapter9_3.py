# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:11]) # [5:11]
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[:len(str_s1)-1]) # str_sl[:10]
print(str_s1[1:9:2]) # 세번째 인수는 몇개 단위로 스킵할건지 의미
print(str_s1[-2:])
print(str_s1[1:-2])
print(str_s1[::2]) # 처음부터 끝까지 2칸씩 가져온다
print(str_s1[::-1])

#  아스키 코드
a = 'z'
print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로