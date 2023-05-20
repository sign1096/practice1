numbers=[103,52,273,32,77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

list_a=(1,2,3,4,5)
list_reversed=reversed(list_a)
print('#reversed()함수')
print('reversed([1,2,3,4,5]):',list_reversed)
print('list(reversed([1,2,3,4,5]))',list(list_reversed))
print('#reversed() 함수')
print('for in reversed([1,2,3,4,5]):')
for i in reversed(list_a):
    print('-',i)

numbers=[1,2,3,4,5,6]
for i in reversed(numbers):
    print('첫 번째 반복문: {}'.format(i))
for i in reversed(numbers):
    print('두 번째 반복문: {}'.format(i))

example_list=['요소A','요소B','요소C']
i=0
for item in example_list:
    print('{}번째 요소는 {}입니다'.format(i,example_list[i]))
    i+=1

example_list=['요소A','요소B','요소C']
print('#단순 출력')
print(example_list)
print()
print('#enumerate(함수 적용 출력)')
print(enumerate(example_list))
print()
print('#list() 함수로 강제 변환 출력')
print(list(enumerate(example_list)))
print()
print('#반복문과 조합하기')
for i,value in enumerate(example_list):
    print('{}번째 요소는 {}입니다'.format(i,value))

example_dictionary={
    '키A':'값A',
    '키B':'값B',
    '키C':'값C'
}
print('#딕셔너리의 items() 함수')
print('items():',example_dictionary.items())
print()
print('#딕셔너리의 items()함수와 반복문 조합하기')
for key,element in example_dictionary.items():
    print('dictionary[{}]={}'.format(key,element))

array=[]
for i in range(0,20,2):
    array.append(i*i)
print(array)

array=[]
for i in range(0,20,2):
    arry.append(i*i)
print(array)

array=['사과','자두','초콜릿','바나나','체리']
output=[fruit for fruit in array if fruit !='초콜릿']
print(output)

number=int(input('정수입력>'))
if number%2==0:
    print('''\
      입력한 문자열은 {}입니다
      {}는 짝수입니다'''.format(number,number))
else:
    print('''\
      입력한 문자열은{}입니다
      {}는 홀수입니다'''.format(number,number))

number=int(input('정수입력>'))
if number%2==0:
    print('''입력한 문자열은 {}입니다.
    {}은 짝수입니다.'''.format(number,number))
else:
    print('''입력한 문자열은 {}입니다.
    {}는 홀수입니다'''.format(number,number))

number=int(input('정수입력>'))
if number%2==0:
    print('입력한 문자열은{}입니다\n{}는 짝수입니다'.format(number,number))
else:
    print('입력한 문자열은{}입니다\n{}는 홀수입니다'.format(number,number))

test=(
    '이렇게 입력해도'
    '하나의 문자열로 연결되어'
    '생성됩니다'
)
print('test:',test)
print('type:test',type(test))

number=int(input('정수입력>'))
if number%2==0:
    print((
        '입력한 문자열은 {}입니다\n'
        '{}는 짝수입니다'
    ).format(number,number))
else:
    print((
        '입력한 문자열은 {}입니다\n'
        '{}는 홀수입니다'
    ).format(number,number))

print('::'.join(['1','2','3','4','5']))

number=int(input('정수입력>'))
if number%2==0:
    print('\n'.join([
        '입력한 문자열은{}입니다',
        '{}는 짝수입니다'
    ]).format(number,number))
else:
    print('\n'.join([
        '입력한 문자열은 {}입니다',
        '{}는 홀수입니다'
    ]).format(number,number))

numbers=[1,2,3,4,5,6]
r_num=reversed(numbers)
print('reversed_numbers:',r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

