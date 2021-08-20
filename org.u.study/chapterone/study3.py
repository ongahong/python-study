
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
print(dict1)
print(len(dict1))


set1 = set()
set1.add(123)
print(set1)