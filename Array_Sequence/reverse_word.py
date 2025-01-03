def rev_sting(str1):
    # return " ".join(reversed(str1.split()))
    # return " ".join(str1.split()[::-1])

    words = str1.split()
    reversed_words = []

    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])

    return ' '.join(reversed_words)

def main():
    string_input = "    Hello    Prasad    "
    ret = rev_sting(string_input)
    print(ret)

if __name__ == "__main__":
    main()

"""
input_text = "hello prasad"
output = ' '.join(word[::-1] for word in input_text.split()[::-1])
print(output) # dasarp olleh


input_text = "hello prasad"
output = ' '.join(word[::-1] for word in input_text.split())
print(output) # olleh dasarp
"""