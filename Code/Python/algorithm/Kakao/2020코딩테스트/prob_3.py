# 정확성 25 효율성 30

words= ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

answer = []

for query in queries:
    length = len(query)
    cnt = 0
    temp = ''
    start = False
    for i in range(length):
        if query[i] != '?':
            temp += query[i]
        else:
            if i == 0:
                start = True

    for word in words:
        if length == len(word):
            if start == False and temp == word[:len(temp)]:
                cnt += 1
            elif start == True and temp == word[len(word) - len(temp):]:
                cnt += 1

    answer.append(cnt)

print(answer)
