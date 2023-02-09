list_name = ["A", "B", "A"]
list_count = []
list_url = []

outer_list = []
inner_list_tmp = []

for index, item in enumerate(list_name):
    for index_inner, item_inner in enumerate(list_name[index]):
        inner_list_tmp = []
        # print(item_inner)
        print(f"index: {index}")
        print(f"item: {item}")
        print(f"index_inner: {index_inner}")
        print(f"item_inner: {item_inner}")
        print(f"outer_list: {outer_list}")

        if item_inner in outer_list:
            print("yes")
            inner_list_tmp.append(item_inner)
            item[index_inner][1] += 1
        else:
            inner_list_tmp.append(item_inner)
            inner_list_tmp.append(0)
            outer_list.append(inner_list_tmp)
        x = input()


print(outer_list)
