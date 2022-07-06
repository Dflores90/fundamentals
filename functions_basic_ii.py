count = 5
while count> -1:
    print(count)
    count = count-1


def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,2]))


def first_plus_length(list):
    print(list[0])
    return len(list)
print first_plus_length([1,2,3,4,5,6]))


def values_greater_than_second(list):
    if len(list)<2:
        return false
    newList=[]
    for i in list:
        if i>list[1]:
            newList.append(i)
    print(len(newList))    
    return newList
print (values_greater_than_second([5,2,3,2,1,4]))


def this_length_that_value(size,value):
    List=[]
    for i in range(size):
            List.append(value) 
    return List
print (this_length_that_value(4,7))