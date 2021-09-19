# os : 환경 변수, 디렉토리(파일) 처리 관련 , 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제6
import os
print(os.environ)
print(os.environ["USERNAME"])

# 예제7(현재 경로)
print(os.getcwd())

# time : 시간 관련 처리
import time
print(time.time())

# 예제8(형태 변환)
print(time.localtime(time.time()))

# 예제10(간단 표현)
print(time.ctime())

# 예제11(형식 표현)
print(time.strftime('%H-%M-%S %Y:%m:%d', time.localtime(time.time())))

# 예제12(시간 간격 발생)
for i in range(5):
    print(i)
    time.sleep(1)

# random : 난수 리턴
import random

# 예제13
print(random.random()) # 0 ~ 1 실수

# 예제14
print(random.randint(1,45))
print(random.randrange(1,45))

# 예제15(섞기)
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 예제16(무작위 선택)
c = random.choice(d)
print(c)

# webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open("http://google.com")

webbrowser.open_new("http://google.com")
