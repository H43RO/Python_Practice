# Tuple DataType
# 리스트와 유사하지만, 튜플은 값을 바꿀 수 없음
t1 = ()
# 요소 하나 가질때 무조건 콤마(,)로 끝남
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3  # 괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
del t1[0]
