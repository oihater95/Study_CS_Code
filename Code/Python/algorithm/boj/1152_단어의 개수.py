string = input()
ans = 0
flag = True

for char in string:
    if char == " ":
        flag = True
        continue
    else:
        if flag:
            ans += 1
            flag = False

print(ans)
