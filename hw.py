#below the arithmetical mean

def below_am(arr):
    am = sum(arr)/len(arr)
    result_final = []
    for x in arr:
        if x < am:
            result_final.append(x)
    return result_final

test_list = [1, 3, 5, 6, 4, 10, 2, 3]
test_result = below_am(test_list)
print(test_result)

#test lowest element
def find_two_lowest(arr):
    arr.sort()
    return arr[:2]

list_test = [198, 3, 4, 9, 10, 2, 0]
result = find_two_lowest(list_test)
print(result)