H, W = map(int, input().split())
blocks = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):  # 양 끝은 물 안고이니까 카운트 안함
    max_left = max(blocks[:i])  # 현재 블록 기준 왼쪽 블록 중 가장 높은 블록
    max_right = max(blocks[i+1:])  # 현재 블록 기준 오른쪽 블록 중 가장 높은 블록
    # 현재 블록 기준 왼쪽 오른쪽에서 가장 높은 블록 중 낮은 블록 - 현재 블록
    water = min(max_left, max_right) - blocks[i]

    # 물 높이가 음수이면 0으로 처리(현재 블록이 가장 높을 경우)
    if water < 0:
        water = 0

    ans += water

print(ans)
