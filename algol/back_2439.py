num = int(input())
# for i in range(num):
#     for j in range(num-i):
#         print("*", end="")
#     print("")
for i in range(num, 0-1, -1):
    print("*" * i)

    #왼쪽에 쏠린 삼각형

# for i in range(1, num+1):
#     print(" " * (num-i) + "*" * i)