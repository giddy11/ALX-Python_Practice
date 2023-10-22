'''BINARY SEARCH'''

def Bin_Search(list, target):
    start = 0
    end = len(list)
    middle = 0
    steps = 0

    while (start <= end):
        print("step(s): {}, list: {}, target: {}".format(steps, list[start:end+1], target))


        steps = steps + 1
        middle = (start + end) // 2
        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return -1


list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 2

rtn = Bin_Search(list1, target)
if rtn != -1:
    print("target {} has been found at index {}".format(target, rtn))
else:
    print("target {} was not found".format(target))