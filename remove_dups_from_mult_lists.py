# def array_diff(a, b):
#     for number in a:
#         if number in b:
#             a.remove(number)
#     return a
#
#
# print(array_diff([1, 2, 2], [2]))

a = [1, 2, 2]
b= [2]
c = []

for i in range(len(a)):
    print(a[i])
    if a[i] in b:
        pass
    else:
        c.append(a[i])
print(c)
