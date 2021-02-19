str1 = 'ABCD'
str2 = "ABCD"
str3 = "AB'CD"
str4 = 'AB\'CD'
str5 = 'AB\nCD'
str6 = ''' abcd
efgh'''
N = 1

print(str1, str2)
print(str3, str4, str5)
print(str6)
print(str1+str2)
print(str1 + str2 + str(N))
print(ord('A'), chr(97))

#################################

line = '안녕하세요'
print(line.replace('세', '시'))  # replace는 원본을 바꾸지 않는다.
print(line)

line = line.replace('세', '시')  # replace한 내용을 저장하여 사용
print(line)

print(line.split('하'))  # '하'를 기준으로 나눔

# 예제) 영문 숫자 조합 비밀번호 확인
print('\n\n예제 비밀번호')
pw = 'abcde'
print('비밀번호 {}'.format(pw))
flag_alpha = False
flag_number = False

for i in pw:
    if i.isalpha():  # 알파벳인지
        flag_alpha = True

    if i.isdigit():  # 숫자인지
        flag_number = True

if not flag_alpha:
    print('비밀번호에 알파벳이 사용되지 않았음')
elif not flag_number:
    print('비밀번호에 숫자가 사용되지 않았음')
else:
    print('조건에 맞는 비밀번호')

######################################
line2 = '안녕하세요'
print(line2.find('녕'))  # 해당 문자의 인덱스 반환
print(line2.index('녕'))  # 해당 문자의 인덱스 반환
print(line2.find('아'))  # find의 경우 없을 경우 -1 반환
# print(line2.index('아'))  # index의 경우 없을 경우 에러 발생

########################################

# == 과 is 차이
a = [1, 2, 3]
b = a  # a와 b는 같은 객체
c = [1, 2, 3]  # c는 새로운 객체 생성

if a == b:
    print(True)
else: print(False)

if a is b:
    print(True)
else: print(False)

if a == c:  # == 은 값 비교
    print(True)
else: print(False)

if b == c:  # == 은 값 비교
    print(True)
else: print(False)

if a is c:  # is는 같은 객체인지 비교
    print(True)
else: print(False)