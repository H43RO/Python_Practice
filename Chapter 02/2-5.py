# 딕셔너리 자료형
# Key-Value 형식으로 되어있는 Hash자료형

dic = {'name': 'haero', 'phone': '01012345678', 'birth': '0922'}
print(dic["name"])

a = {1: 'hi'}
print(a[1])
a = {'a': [1, 2, 3]}
print(a['a'])

# 기억해야할 것 :
# 딕셔너리에서는 index가 아닌 key값으로 요소를 참조한다

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'H43RO'
print(a)

a[3] = [1, 2, 3]
print(a)
del a[1]
print(a)
del a['name']
print(a)

grade = {'pey': 10, 'juliet': 90}
print(grade['juliet'])

a = {1: 'a', 2: 'b'}
print(a[1])

# 딕셔너리의 key값에 리스트는 올 수 없다
# -> key값은 '변하지 않는 요소'여야 하기 때문이다
# a = {[1, 2]: 'hi'}

a = {'name': 'pey', 'phone': '01012345678', 'birth': '0922'}
print(a.keys())
# 파이썬 3.0 이후, a.keys(), a.values()에 의해 반환되는 객체는 리스트가 아니다.
# 리스트로 사용하려면 list(a.keys()) 와 같이 사용해야 한다.
# 근데 리스트로 변환하지 않아도 기본적인 iterate 구문은 사용할 수 있다.
for i in a.keys():
    print(i)

print(a.values())  # a.keys() 와 같은 타입의 객체 반환
print(a.items())  # Key, Value 쌍을 튜플로 묶은 값 반환
a.clear()  # 모든 요소 삭제
print(a)
