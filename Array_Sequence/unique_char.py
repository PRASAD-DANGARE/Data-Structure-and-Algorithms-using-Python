def uni_char(s):
    # ======== solution 1 =============

    # return len(set(s)) == len(s)

    # ======== solution 2 ==============

    # sorted_s = ''.join(sorted(s))
    # for i in range(1, len(sorted_s)):
    #     if sorted_s[i] == sorted_s[i-1]:
    #         return False
    #     else:
    #         return True

    # ========== solution 3 =============

    chars = set()
    for i in s:
        if i in chars:
            return False
        else:
            chars.add(i)

    return True

def main():
    s = ('abcde')
    ret = uni_char(s)
    print(ret)

if __name__ == "__main__":
    main()