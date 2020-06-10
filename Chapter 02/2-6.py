# 집합 자료형
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))  # 교집합 구하는 함수

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))
print(s2.difference(s1))

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
s1.add(3)
print(s1)