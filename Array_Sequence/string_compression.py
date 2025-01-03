def compress(s):
    # ==========solution 1 ==============

    # result = {}
    
    # for i in s:
    #     if i not in result:
    #         result[i] = 1
    #     else:
    #         result[i] += 1

    # output = ''.join(f"{key}{value}" for key, value in result.items())
    # return output

    # ========== solution 2 =================

    # r = ""
    # l = len(s)

    # if l == 0:
    #     return ""
    
    # if l == 1:
    #     return s + "1"
    
    # last = s[0]
    # cnt = 1
    # i = 1

    # while i < l:
    #     if s[i] == s[i-1]:
    #         cnt += 1
    #     else:
    #         r = r + s[i-1] + str(cnt)
    #         cnt = 1
    #     i += 1

    # r = r + s[i-1] + str(cnt)

    # return r

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    # Add the last character and its count
    result += s[-1] + str(count)

    return result

def main():
    
    s = ('AAAaa')
    ret = compress(s)
    print(ret)

if __name__ == "__main__":
    main()