list_1=[273,32,'문자열',True,False]
print(list_1[0])
print(list_1[1:3])
print(list_1[-2])
print(list_1[2][1])

list_2=[[1,2,3,],[4,5,6],[7,8,9]]
print(list_2[1])
print(list_2[2][2])

list_a=[1,2,3]
list_b=[4,5,6]
print('# 리스트')
print('list_a=[1,2,3]')
print('list_b=[4,5,6]')
print('#리스트 기본 연산자')
print('list_a+list_b=',list_a+list_b)
print('lsit_a*3=',list_a*3)
print('#길이 구하기')
print('len(list_a)=',len(list_a))

list_a=[1,2,3]
print('#리스트 뒤에 요소 추가하기')
list_a.append(4)
list_a.append(5)
print(list_a)
print()
print('#리스트 중간에 요소 추가하기')
list_a.insert(2,10)
print(list_a)

list_a=[0,1,2,3,4,5]
print('#리스트의 요소 하나 제거하기')
del list_a[1]
print('del list_a[1]=',list_a)
list_a.pop(2)
print('pop(2):',list_a)

list_b=[0,1,2,3,4,5,6]
del list_b[3:6]
print(list_b)

list_c=[0,1,2,3,4,5,6]
del list_c[:3]
print(list_c)

list_d=[1,2,1,2]
list_d.remove(2)
print(list_d)

list_e=[0,1,2,3,4,5]
list_e.clear()
print(list_e)

list_f=[52,264,103,43,56,6,1]
list_f.sort()
print(list_f)
list_f.sort(reverse=True)
print(list_f)

list_a=[273,43,156,45,76]
print(273 in list_a)
print(50 in list_a)

list_a=[273,43,156,45,76]
print(273 not in list_a)
print(50 not in list_a)

array=[273,54,103,5,7]
for element in array:
    print(element)

list_of_list=[
    [1,2,3],
    [4,5,6,7],
    [8,9]
]
for itmes in list_of_list:
    for itme in itmes:
        print(itme)

a=[1,2,3,4]
b=[*a,*a]
print(b)

a=[1,2,3,4]
a.append(5)
print(a)

b=[1,2,3,4]
c=[*b,5]
print(b)
print(c)

numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number>=100:
        print('-100이상의 수',number)

numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number%2==1:
        print(number,'홀수 입니다')
    else:
        print(number,'은 짝수입니다')

numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    print(number,'는',len(str(number)),'자릿수이다')

numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]
for number in numbers:
    output[(number-1)%3].append(number)
print(output)


               