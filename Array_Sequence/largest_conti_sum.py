def large_conti_sum(arr):

    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

def main():

    arr = [1,2,-1,3,4,10,10,-10,-1]
    ret = large_conti_sum(arr)
    print(ret)

if __name__ == "__main__":
    main()