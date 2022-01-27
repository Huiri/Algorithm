a, b = input().split()
a = int(a)
b = int(b)
if(b-45 < 0):
    b = b - 45 + 60
    if(a - 1 < 0):
        a = a -1 + 24
    else :
        a = a-1
else :
    b = b -45
print(a, b)

      #숏코딩
a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)