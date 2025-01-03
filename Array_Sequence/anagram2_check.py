def anagram(s1, s2):
    
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
     
    if len(s1) != len(s2):
        return False
    
    count = {}

    for i in s1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for j in s2:
        if j in count:
            count[j] -= 1
        else:
            count[j] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True
    
def main():
    s1 = str(input("enter word or statement : "))
    s2 = str(input("enter word or statement to check anagram : "))
    print(anagram(s1, s2))

if __name__ == "__main__":
    main()