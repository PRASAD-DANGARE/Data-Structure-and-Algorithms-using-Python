def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

    # for i in arr1:
    #     if i in arr2:
    #         arr2.remove(i)
    #     else:
    #         missing_ele.append(i)

    # print(missing_ele)


def main():
    arr1 = [5,5,7,7] # [1,2,3,4,5,6,7,8,9], [5,5,7,7]
    arr2 = [5,7,7] # [3,7,2,1,4,6], [5,7,7]
    ret = finder(arr1, arr2)
    print(ret)

if __name__ == "__main__":
    main()