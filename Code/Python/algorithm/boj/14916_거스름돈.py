total = int(input())
coin_5 = total // 5

if total % 5 == 0:
    print(coin_5)

else:
    while coin_5 >= 0:
        temp = total - coin_5 * 5
        if temp % 2 == 0:
            coin_2 = temp // 2
            print(coin_5 + coin_2)
            exit()
            break

        else:
            coin_5 -= 1

    print(-1)