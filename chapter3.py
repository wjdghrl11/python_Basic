# %s
print('%10s' % ('nice111')) # 총 자릿수가 10자리이다 숫자가오면
print('{:>10}'.format('nice')) # 부등호가 왼쪽 위에 코드와 똑같다

print('%-10s' % ('nice111'))  # 음수가 왔을때는 왼쪽부터채운다
print('{:10}'.format('nice')) # 그냥 생략을 할떈 오른쪽을 공백으로 채운다

print('{:_>10}'.format('nice')) # 원하는 걸로 쓰면 공백이 입력값으로 출력된다.
print("{:^10}".format('nice')) # 10개 공간중에서 중앙 정렬 ^

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # 점을 붙이면 절삭을한다
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%1.18f' % (3.14))
print('{:f}'.format(3.14))

print('%06.2f' % (3.1415926589793))
print('{:06.2f}'.format(3.1415926589793))


