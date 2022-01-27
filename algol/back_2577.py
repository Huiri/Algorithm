# num_list=[]
# for i in range(3):
#     num_list.append(int(input()))
# x= 1
# for i in range(3):
#     x = num_list[i] * x
# x=str(x)
#
# unique_list = list(set(x))
# cnt_list=[]
# for i in unique_list:
#     count = unique_list.count(i)
#     cnt_list.append(count)
#     print(count)
# print(cnt_list)
# cnt_list.sort()
# print(cnt_list)

a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i)))