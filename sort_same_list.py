import random

VAR = 10


#Create Data
my_list = []
for i in range(VAR):
    my_list.append(i + 1)

print(my_list)


#Randomize Data for Testing
random.shuffle(my_list)
print(my_list)

x = 0
while x < len(my_list):
    for i in range(len(my_list)):
        if i == 0:
            continue
        else:
            if my_list[i] > my_list[i - 1]:
                continue
            else:
                tmp_var = my_list[i]
                my_list[i] = my_list[i - 1]
                my_list[i - 1] = tmp_var

    x+=1
print(my_list)
