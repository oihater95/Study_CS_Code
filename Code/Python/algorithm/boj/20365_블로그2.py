N = int(input())
colors = list(input())
# 파란색 블럭 수와 빨간색 블럭 수
cnt_b = 0
cnt_r = 0
ans = 0
prev_color = colors[0]

for i in range(1, N):
    if prev_color != colors[i]:
        if colors[i] == 'B':
            cnt_r += 1
            # 마지막 요소 처리
            if i == N - 1:
                cnt_b += 1
        else:
            cnt_b += 1
            # 마지막 요소 처리
            if i == N - 1:
                cnt_r += 1
        # 이전 색 갱신
        prev_color = colors[i]
    else:
        # 이전색과 현재 색이 같을 경우 마지막에는 카운트 안되는 예외 처리
        if i == N - 1:
            if colors[i] == 'B':
                cnt_b += 1
            else:
                cnt_r += 1

ans = min(cnt_b, cnt_r) + 1
print(ans)
