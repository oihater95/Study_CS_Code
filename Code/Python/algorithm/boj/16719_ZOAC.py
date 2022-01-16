def dfs(arr, start):
    if not arr:
        return

    min_alpha = min(arr)
    idx = arr.index(min_alpha)
    # 가장 작은 알파벳 ans에 추가
    ans[start+idx] = min_alpha
    print(''.join(ans))

    # 가장 작은 알파벳 처리 후 가장 작은 알파벳 기준 뒤부터 처리
    dfs(arr[idx+1:], start+idx+1)
    # 가장 작은 알파벳 기준 뒤쪽 처리 끝낸 후 앞쪽 처리
    dfs(arr[:idx], start)


string = list(input())
ans = [''] * len(string)

dfs(string, 0)