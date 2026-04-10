#Finding max
def find_max(num):
    if len(num)==1:
        return num[0]
    else:
        max_of_rest=find_max(num[1:])
        return num[0] if num[0]>max_of_rest else max_of_rest
    
my_list=[1,3,5,7,9]
print(find_max(my_list))
print(find_max([2,4,6,8,0]))