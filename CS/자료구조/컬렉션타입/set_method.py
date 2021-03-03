temp = {'a', 'b', 'c', 'd', 'e'}
temp2 = {'a', 'b', 'c'}

# 추가
temp.add('f')
print(temp)

# 합집합
temp.update({'g', 'h', 'i'})
print(temp)
temp |= {'A', 'B'}
print(temp)

# update와 동일, 원본을 바꾸지 않음
print(temp.union({'C', 'D'}))
print(temp)

# 교집합, 원본을 바꾸지 않음 (= &)
print(temp.intersection(temp2))
print(temp)

# 차집합, 원본을 바꾸지 않음
print(temp.difference({'c','d','e'}))
print(temp)

# 삭제
temp.discard('A')  # 반환없고 해당 원소 없어도 됨
print(temp)
temp.remove('h')  # 해당원소 없으면 keyError
print(temp)
temp.pop()  # 무작위 제거, 빈 set일 경우 Error
print(temp)

temp.clear
print(temp)