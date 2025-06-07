# Write a program that checks if a given list is sorted in ascending order.

def is_ascending_order(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


num_list= [False,True,2,3.5,4,5]
print(is_ascending_order(num_list))