lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)


word = "Beautiful"

for s in word:
    print('word : ', s)

my_info = {
    "name": 'Lee',
    "Age": 33,
    "City": "Seoul"
}

for k in my_info:
    print('key :', my_info)

for v in my_info.values():
    print('value :', v)

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break       

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not Found :', num)


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
    print("multiplt by 2", v * 3)