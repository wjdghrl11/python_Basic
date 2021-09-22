# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제1 
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Header Skip

    # 객체 확인
    print(reader)
    print(type(reader))
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))
    print()

    for c in reader:
        # print(c)
        print(''.join(c))

# 예제2
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    
    for c in reader:
        print(c)