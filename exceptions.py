t = int(input())

while t > 0:
    try:
        a, b = map(int, input().split())
        ans = a // b
        print(ans)

    except Exception as e:
        print("Error Code:", e)
    t -= 1