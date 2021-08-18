
list = []

list.append(1)
list.append(2)

list2 = sorted(list)

print(len(list))
print(f'原list:{list2}; 新list：{list}')

#list.reverse()
#print(f'原list:{list2}; 新list：{list}')

list.sort()
print(f'原list:{list2}; 新list：{list}')