#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#full_list = []
#for i in range(max(len(list1), len(list2))):
#    full_list.append(list1[i] + list2[i])
#print(full_list)
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly" , "."]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)