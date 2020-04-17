odd = [1, 3, 5, 7, 9]
print(odd)

a = [1, 2, 3]
print(a[0])

print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
b = a[:2]
print(b)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))

print(str(a[2]) + " h i")
a[2] = 5
print(a)
del a[1]
print(a)
a = [1, 2, 3, 4, 5]
del a[:3]
print(a)

a = [1, 2, 3, 4, 5]
a.append(4)
print(a)
a.sort()
print(a)
a = ['a', 'd', 'c']
a.sort()
print(a)
a.reverse()
print(a)
a = [1, 2, 3]
print(a.index(3))
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(2, 5)
print(a)
a.remove(1)
a.remove(2)
print(a)

a = [1, 2, 3, 4, 5, 1, 2, 3]
a.remove(3)
print(a)
print(a.pop())
print(a)

print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))
