# 1 새로운 문자열에 역순으로 읽어서 쓰기
str1 = '안녕하세요'
str2 = ''
str3 = ''
for i in range(len(str1)-1, -1, -1):
    str2 += str1[i]
print(str2)

for char in reversed(str1):  # 역으로 읽기 reversed()
    str3 += char
print(str3)

# 2 자기 문자열에서 바꾸기(임시변수 사용) => 리스트로 변환 후 사용, string은 immutable
# for문은 절반만 수행 (홀수의 경우 소수가 나오므로 //2사용, 홀수의 중간 인덱스는 바꾸지 않아도 됨)
str4 = '안녕하세요'
str4 = list(str4)

for i in range(len(str4)//2):
    str4[i], str4[len(str4) - 1 - i] = str4[len(str4) - 1 - i],  str4[i]
print(''.join(str4), type(str4))
str4 = str(str4)
print(str4, type(str4))

# 3 슬라이싱 이용
str5 = '안녕하세요'
str6 = str5[::-1]
print(str6)

# 4 reversed 이용
print(''.join(reversed(str5)))