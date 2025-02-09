list1 = [8, 4, 2, 4, 5, 6,1]
list2 = [4, 5, 6, 0, 8, 9,2]
common_elements = set(list1) & set(list2)
common_list = list(common_elements)
print("Common elements:", common_list)