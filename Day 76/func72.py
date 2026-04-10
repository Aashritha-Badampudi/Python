def sum_list(num):
    if len(num)==0:
        return 0
    else:
        return num[0] + sum_list(num[1:])
    
my_list = [1,2,3,4,5,6]
print(sum_list(my_list))
print(sum_list([1,2,3,4,5,6]))