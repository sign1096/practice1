number=input('정수 입력>')
number=int(number)
if number%2==0:
    print('정수는 짝수입니다')
else:
    print('정수는 홀수입니다')

import datetime
now=datetime.datetime.now()
month=now.month
if 3<=month<=5:
    print('현재는 봄입니다')
elif 6<month<=8:
    print('현재는 여름입니다')
elif 8<month<=11:
    print('현재는 가을입니다')
else:
    print('현재는 겨울입니다')

score=float(input('학점 입력>'))
if score==4.5:
    print('신')
elif 4.2<=score:
    print('교수님의 사람')
elif 3.5<=score:
    print('현 체제의 수호자')
elif 2.8<=score:
    print('일반인')
elif 2.3<=score:
    print('일탈을 꿈꾸는 소시민')
elif 1.75<=score:
    print('오락문화의 선구자')
elif 1.0<=score:
    print('불가촉천민')
elif 0.5<=score:
    print('자벌레')
elif 0<score:
    print('플랑크톤')
else:
    print('시대를 앞서가는 혁명의 씨앗')

str_input=input("태어난 해를 입력해 주세요>")
birth_year=int(str_input)%12
if birth_year==0:
    print('원숭이 띠입니다')
elif birth_year==1:
    print('닭 띠입니다')
elif birth_year==6:
    print('범 띠입니다')

import datetime
now=datetime.datetime.now()
input=input('입력:')
if '안녕'in input:
    print('안녕하세요')
elif '몇시'in input:
    print('지금은 {}시입니다'.format(now.hour))
else:
    print(input)

입력=int(input('정수를 입력해주세요:'))
if 입력%2==0:
    print(f'{입력}은 2로 나누어떨어지는 숫자 입니다')
else:
    print(f'{입력}은 2로 나누어 떨어지는 숫자가 아닙니다')
if 입력%3==0:
    print(f'{입력}는 3으로 나누어 떨어지는 숫자입니다')
else:
    print(f'{입력}는 3으로 나누어 떨어지지 않습니다')
if 입력%4==0:
    print(f'{입력}는 4로 나누어 떨어집니다')
else:
    print(f'{입력}는 4로 나누어 떨어지지 않습니다')
if 입력%5==0:
    print(f'{입력}는 5로 나누어 떨어집니다')
else:
    print(f'{입력}는 5로 나누어 떨어지지 않습니다')

number=input('정수 입력>')
number_a=int(number)
if number_a>0:
    raise NotImplementedError
else:
    raise NotImplementedError