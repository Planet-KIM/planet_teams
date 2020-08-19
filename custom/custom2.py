
content = [3, 5, 7]
content.insert(0, 2)
print(content)


array = [9, 1, 2]
k = content + array
print(k)


content.extend(array)
print(content)

content.remove(1)
print(content)


del content[5]
print(content)