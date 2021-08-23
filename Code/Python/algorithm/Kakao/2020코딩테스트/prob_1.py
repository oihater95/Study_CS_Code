s = "aabbaccc"
# s= "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
answer = 0
word_length = 1
min_length = 1000

while word_length <= len(s)//2+1:  # 문자열이 한개일 때를 고려해서 +1 해줌
    temp = ''
    cnt = 1
    word = ''
    idx = 0

    # word => 이전에 슬라이싱한 단어
    while idx+word_length <= len(s):
        if word == s[idx:idx+word_length]:
            cnt += 1
        else:
            if cnt > 1:
                temp += str(cnt) + word
            else:
                temp += word
            word = s[idx:idx+word_length]
            cnt = 1

        idx += word_length

    # 마지막 슬라이싱 단어
    if cnt > 1:
        temp += str(cnt) + word
    else:
        temp += word

    # 슬라이싱하고 남은 문자열 추가(나누어 떨어지지 않을 때)
    if len(s[idx:]) < word_length:
        temp += s[idx:]

    if len(temp) < min_length:
        min_length = len(temp)

    word_length += 1

print(min_length)



