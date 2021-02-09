# 입력
# input() => 문자열로 입력 받음
tmp = input()
print(tmp, type(tmp))

# 정수 하나 입력
N = int(input())

# 4 5 6 split() => split default는 공백, ","로 쓰면 ,기준으로 분리
# 가,나,다 => split("나") = '가', ',', ',다'
a, b, c = map(int, input().split())  # input().split()만 하면 str형으로 받음
arr = list(map(int, input().split()))  # 리스트로 받기

# 가나다라  list()는 요소 하나씩 나눠 문자열!로 저장
tmp = list(input())  # list()를 사용하면 알아서 나눠 받음 ['가', '나', '다', '라']

# 12312412 int형으로 요소 하나씩 나누기
tmp = list(map(int, input()))

# sys 라이브러리
import sys
sys.stdin = open("input.txt","r")