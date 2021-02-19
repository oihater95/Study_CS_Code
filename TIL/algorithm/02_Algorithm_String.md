# Algorithm String

## Python에서의 String

- Sequence, Immutable: 인덱싱, 슬라이싱 연산가능, 데이터 값 바꿀 때 메모리에 저장된 데이터 전체를 없애고 새로 생성
- char 타입 없음 => 텍스트 데이터 취급 통일
- 문자열 기호: `''`, `""`, `'''`, `"""`
- +연결(Concatenation): 문자열 + 문자열 이어 붙이기
- *반복: 문자열 * 수 만큼 문자열 반복

## 문자표현

### 아스키코드

- string to integer => ord('문자')
- integer to string => chr('숫자')
- ord('A') = 65, ord('a') = 97, ord('0') = 48
- chr(48) = '0', chr(65) = 'A', chr(97) = 'a'

```python
print(ord('A'), chr(97))
>>> 65 a
```

```python
def atoi(num_str):
    # 최종 값을 담을 변수
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')

    return value

num_str = '1234'
num_int = atoi(num_str)
print(num_int, type(num_int))
>>> 1234 'int'
```

```python
def itoa(int_num):
    str_num = ''
    char_num = []  # 정수를 한 자리씩 string으로 변환한 데이터넣음(역순)

    if int_num < 0:  # 음수일 경우 - 추가
        str_num += '-'
        int_num *= -1

    while int_num:  # 일의 자리부터 한 자리씩 변환
        num = int_num % 10
        char_num.append(chr(ord('0') + num))
        int_num //= 10

    for i in range(len(char_num)-1, -1, -1):  # char_num에 역순으로 들어갔기 때문에 뒤에서부터 순회
        str_num += char_num[i]

    print(str_num, type(str_num))  # 반환 없음

itoa(1234)
itoa(-1234)
>>> '1234' 'string' 
'-1234' 'string'
```



## 문자열 뒤집기

- 새로운 문자열 역순으로 읽어서 쓰기

```python
for i in range(len(string)-1, -1, -1):
    str2 += string[i]
print(str2)
```



- reversed() 내장함수

```python
print(''.join(reversed(string)))
```



- 자기 문자열에서 바꾸기 (길이의 절반만 for문 순회)

```python
for i in range(len(string)//2):
    string[i], strring[len(string) - 1 - i] = string[len(string4) - 1 - i],  string[i]
print(''.join(string), type(string))
```



- 슬라이싱

```python
str2 = string[::-1]
print(str2)
```



## 패턴매칭

### BruteForce

>  본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

- 시간복잡도 O(MN) => (M: 찾을 패턴의 길이, N: 전체 텍스트의 길이)



```python
p = 'is'  # 찾을 패턴
t = 'This is a book'  # 전체 텍스트
M, N = len(p), len(t)  # 찾을 패턴의 길이, 전체 텍스트 길이

def BruteForce(p, t):
    i = 0  # t 인덱스
    j = 0  # p 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M : 
        return i - M  # 검색 성공
    else:
        return -1  # 검색 실패
```



### KMP 알고리즘

>  불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로 
>
> 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭 수행

- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화
  - next[M]: 불일치 발생 시 이동할 다음 위치
- 시간 복잡도 O(M+N)



### 보이어-무어 알고리즘

> 오른쪽에서 왼쪽 비교
>

- 패턴의 오른쪽 끝에 있는 문자가 일치할 경우 오른쪽에서 왼쪽으로 비교

- 패턴의 오른쪽 끝에 있는 문자가 불일치 하고 해당 문자가 패턴 내에 존재하지 않는 경우, 패턴의 길이만큼 이동

- 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재할 경우, 패턴에서 일치하는 문자를 찾아서 점프
- 시간 복잡도 O(N) ~ O(MN)

