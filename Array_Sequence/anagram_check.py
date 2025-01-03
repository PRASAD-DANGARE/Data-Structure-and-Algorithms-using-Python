def anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    return sorted(s1) == sorted(s2)
    
def main():
    s1 = str(input("enter word or statement : "))
    s2 = str(input("enter word or statement to check anagram : "))
    print(anagram(s1, s2))

if __name__ == "__main__":
    main()

# anagram('clint eastwood','old west action')
# anagram('dog','god')
# anagram('aa','bb')
