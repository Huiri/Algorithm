# a = input()
# b = input()
# c = input()
# d = input()
# e = input()
# f = input()
# g = input()
# h = input()
# i = input()
# list = [a, b, c, d, e, f, g, h, i]
# print(max(list))
# print(list.index(max(list))+1)

num_list = []
for i in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(num_list.index(max(num_list))+1)