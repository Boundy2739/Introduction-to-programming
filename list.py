def print_list(int_list):
    print(int_list)
def listsum(int_list):
    print(sum(int_list))
def highest(int_list):
    print(max(int_list))
def lowest(int_list):
    print(min(int_list))
def backward(int_list):
    int_list.reverse()
    print(int_list)


int_list  = [101,4,53,27,89,92,75,60,36,18,40]

print_list(int_list)
listsum(int_list)
highest(int_list)
lowest(int_list)
backward(int_list)