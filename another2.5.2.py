name = input('이름을 입력하세요 : 홍길동')

print('%s님 반갑습니다.' % name)

name = input('이름을 입력하세요: ')

print('%s님 반갑습니다.' %name)


a = input('첫 번째 숫자를 입력하세요:')
b = input('두 번째 숫자를 입력하세요:')

c = a+b

print(c)
print(type(a), type(b), type(c))

a = input('첫 번째 숫자를 입력하세요:')
b = input('두 번째 숫자를 입력하세요:')

c = int(a) + int(b)

print(c)


inch = float(input('인치(inch)를 입력하세요:'))

cm = inch * 2.54

print('센티미터 : %.2f' %cm)

width = 10
height = 3

area = width * height /2

print('삼각형의 밑변 길이:', width)
print('삼각형의 높이:', height)
print('삼각형의 면적:', area)


