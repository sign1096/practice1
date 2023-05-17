a=range(5)
print(a)
print(list(range(5)))

print(list(range(0,10,2)))
print(list(range(0,10,3)))

a=range(0,10+1)
print(list(range(0,10+1)))

n=10
a=range(0,n//2)
print(list(a))

for i in range(5):
    print(str(i)+'=반복 변수')
print()
for i in range(5,10):
    print(str(i)+'=반복 변수')
for i in range(0,10,3):
    print(str(i)+'=반복 변수')

arry=[273,32,103,57,52]
for i in range(len(arry)):
    print('{}번째 반복:{}'.format(i,arry[i]))

for i in range(4,0-1,-1):
    print('현재 반복 변수:{}'.format(i))

for i in reversed(range(5)):
    print('현재 반복변수:{}'.format(i))

height=10
for i in range(1,10+1):
    print("*"*i)

i=0
while i<10:
    print("{}번째 반복합니다".format(i))
    i+=1

list_test=[1,2,1,2]
value=2
while value in list_test:
    list_test.remove(value)
print(list_test)

import time
print(time.time())

import time
number=0
target_tick=time.time()+5
while time.time()<target_tick:
    number+=1
print('5초동안 {}번 반복했습니다'.format(number))

i=0
while True:
    print('{}번째 반복문입니다'.format(i))
    i=i+1
    input_text=input('>종료하시겠습니까?(y/n):')
    if input_text in ['y','Y']:
        print('반복을 종료합니다')
        break

numbers=[5,15,6,20,7,25]
for number in numbers:
    if number<10:
        continue
    print(number)

key_list=['name','hp','mp','level']
value_list=['기사',200,30,5]
character={}
for i in range(0,len(key_list)):
         character[key_list[i]]=value_list[i]
print(character)

limit=10000
i=1
sum_value=0
while sum_value<=limit:
    sum_value+=i
    i+=1
print('{}를 더할때 {}을 넘으며 그때의 값은 {}입니다'.format(i,limit,sum_value))

a=[27,53,103,273,32]
현재최대값=a[0]
for i in a:
     if 현재최대값<i:
      현재최대값=i
print(현재최대값)
    

