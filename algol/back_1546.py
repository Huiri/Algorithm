n = int(input())
list = input().split()
value = []
for i in range(n):
    value.append(int(list[i]))
m = max(value)
temps = []
for j in value:
    temps.append(int(j)/m*100)
new = 0
for temp in temps:
    new = temp + new
print(new / n)
