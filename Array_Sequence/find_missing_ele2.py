import collections

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def main():
    arr1 = [5,5,7,7] # [1,2,3,4,5,6,7,8,9], [5,5,7,7]
    arr2 = [5,7,7] # [3,7,2,1,4,6], [5,7,7]
    ret = finder(arr1, arr2)
    print(ret)

if __name__ == "__main__":
    main()