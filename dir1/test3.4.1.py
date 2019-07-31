lists = [1,2,3,'a','1',5]
print(lists)

print(lists[0])
print(lists[-0])
print(lists[-1])

print(lists[3])
print(lists[4])
lists[4] = 4
print(lists[4])

lists.append('c')
print(lists)

lists.pop(0)
print(lists)