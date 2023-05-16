dict_a={}
dict_a['name']='구름'
print(dict_a)

dict_b={
    'name':'구름'
}
del dict_b['name']
print(dict_b)

pets=[
    {'name':'구름','age':'5'},
    {'name':'초코','age':'3'},
    {'name':'아지','age':'1'},
    {'name':'호랑이','age':'1'}
]
for dict_c in pets:
    print(dict_c['name'],dict_c['age'],'살')
        
character={
    'name':'기사',
    'level':12,
    'items':{
        'sword':'불꽃의 검',
        'armor':'풀플레이트'
    },
    'skill':['베기','세게 베기','아주 세게 베기']
}
for key in character:
    for key_a in character[items]:
        for key_b in character[skill]: 
    print(key,':',character[key])

    <pass>
