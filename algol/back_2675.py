num = int(input())
for _ in range(num):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt), end="")
    print()