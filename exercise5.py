def first_last(list):
    if list[0] == list[len(list) - 1]:
        return True
    else:
        return False
list_1 = [10,20,30,45,10]
print(first_last(list_1))