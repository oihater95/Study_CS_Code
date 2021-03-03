# key존재하면 해당 value 반환, 없으면 key 새로 추가
temp = {1: 'a', 2: 'b', 3: 'c'}
print(temp.setdefault(1))
temp.setdefault(4)
print(temp)

# key없으면 아무것도 반환안함
print(temp.get(1))
print(temp.get(5))

# 읽기
print(temp.items())
print(temp.keys())
print(temp.values())

# 정렬
tmp = {1: 20, 2: 10, 3: 30}
print(sorted(tmp.keys()))
print(sorted(tmp.values()))
print(sorted(tmp.items()))

# 삭제
print(temp.popitem())
print(temp.popitem())
print(temp)

temp.clear()
print(temp)