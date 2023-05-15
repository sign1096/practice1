list_a=[273,32,103,'문자열','True']
print(list_a[3:5])
list_a[0]=33
print(list_a)

list_a=[1,2,3]
list_a.extend([4,5,6])
print(list_a)

numbers=[1,2,3,4,5,6,7,8]
numbers[::1]
print(numbers)

for character in '278378':
    print('-',character)

list_of_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in list_of_list:
    for m in i:
        print(m)

numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number%2==0:
      print(f'{number}는 짝수입니다')
    else:
        print(f'{number}는 홀수입니다')

numbers=[273,103,5,32,65,9,72,800,99]
for i in numbers:
     print(i,'는', len(str(i)),'이다')
       
