food = "Python's favorite food is perl"
print(food)  # 큰 따옴표로 감싸면 내부의 작은 따옴표를 문자열 처리해줌

say = '"Python is very easy." he said.'
print(say)  # 작은 따옴표로 감싸면 내부의 큰 따옴표를 문자열 처리해줌

# 물론, Escape Sequence도 작동함 ( 백슬래시 \ )

multiline = '''
Life is too short
You need Python
'''
print(multiline)

a = "python"
print(a * 2)
print(len(a))
print("=" * 50)
print(a[2])
print(a[2:4])  # 끝 번호는 포함하지 않은 슬라이싱 기법

a = "Life is too short, You need Python"
print(a[19: -7])
print(a[:17])
print(a[19:])

a = "20200606Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "Pithon"
print(a[:1] + 'y' + a[2:])
print("I eat %d apple." % 3)
print("I eat %s apple." % "five")

print("I ate %d apples. so I was sick for %s days" % (5, "five"))
print("Error is %d%%" % 98)  # 포맷코드인 %을 문자열에 사용하고 싶은 경우

print("%10s" % "hi")  # 왼쪽으로 공백 생성
print("%-10sjane." % "hi")  # 오른쪽으로 공백 생성

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

# format()을 활용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples for {1} days".format("five", "three"))
print("I eat {how} apples for {day} days".format(day="five", how="three"))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^20}".format("hi"))

name = "김현준"
age = 21
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')

d = {'name': '김현준', 'age': 22}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

a = "hobby"
print(a.count('b'))
print(a.find('b'))
print(a.find('k'))

print(",".join('abcd'))

print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())

a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

print(a.split())