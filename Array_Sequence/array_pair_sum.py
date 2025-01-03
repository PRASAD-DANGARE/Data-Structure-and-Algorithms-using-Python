def array_pair_sum(arr, k):
    
    if len(arr) < 2:
        return
    
    seen = set()
    output = set()

    for num in arr: # 1, 3, 2, 2, 1
        target = k - num # 4-1 = 3, 4-3 = 1, 4-2 = 2, 4-2 = 2, 4-1 = 3

        if target not in seen:
            seen.add(num) # 3, 1, 2

        else:
            output.add(((min(num, target)), max(num, target))) #((2,2), (2,2)), ((1,3), (1,3)) 

    print('\n'.join(map(str, list(output)))) #(1,3), (2,2)

def main():
    array_pair_sum([1,3,2,2,1], 4)

if __name__ == "__main__":
    main()