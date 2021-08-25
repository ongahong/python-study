import copy

list1 = list()

list1.append(1)
list1.append(2)

list2 = sorted(list1)

print(len(list1))
print(f'原list:{list2}; 新list：{list1}')

list1.reverse()
print(f'原list:{list2}; 新list：{list}')

list1.sort()
print(f'原list:{list2}; 新list：{list1}')


tup = tuple()
print(len(tup))


dict1 = dict()
dict2 = {}

dict1['name'] = '麦芽'
dict1['age'] = '30'
dict1['sex'] = '女'
dict1['books'] = ['历史','数学']
print(dict1)
print(len(dict1))


set1 = set()
set1.add(123)
print(set1)


dict2 = copy.deepcopy(dict1)
dict3 = dict1.copy()
dict1['birth'] = '1999'
dict1['books'] = ['历史','数学','政治']
dict1['books'].append('音乐')


print(f'dict1: {dict1}')
print(f'dict2: {dict2}')
print(f'dict3: {dict3}')

