rectangles = [[5,8],[3,9],[5,12],[16,5]]
max_len = 0
cnt = 0

for rectangle in rectangles:
    square_len = min(rectangle[0], rectangle[1])
    if max_len < square_len:
        cnt = 1
        max_len = square_len
    elif max_len == square_len:
        cnt += 1

print(cnt)