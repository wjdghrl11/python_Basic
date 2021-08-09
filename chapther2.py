# end 옵션 하나의 라인으로 이어줄수있다.
print('Welcome to', end=' ')
print('IT News', end='')
print('Web Site')

# file 옵션
import sys
print('Learn Python', file=sys.stdout) 
print()

# format 사용(d, s, f) 정수 문자열 실수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two')) # 이 포맷을 좀 더 많이 사용하긴함
print('{1}, {0}'.format('one','two')) # 암묵적으로 원래 순서는 0, 1
