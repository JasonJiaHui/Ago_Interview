
#### 12.13

def reverseString(string):

    if not string:
        return

    low = 0
    high = len(string) - 1

    while low < high:
        string[low], string[high] = string[high], string[low]
        low += 1
        high -= 1
    print string


def bruteForce(string, pattern):

    string_len = len(string)
    pattern_len = len(pattern)

    for i in range(string_len - pattern_len + 1):
        save = i
        flag = True
        for j in range(pattern_len):
            if string[save] != pattern[j]:
                flag = False
                break
            else:
                save += 1
        if flag:
            print "Matching..."
            return
    print "No"


# O(mn)
def BM(string, pattern):
    string_len = len(string)
    pattern_len = len(pattern)

    last = {}
    for char in string:
        last[char] = -1

    for i in range(pattern_len):
        last[pattern[i]] = i

    i = pattern_len - 1
    k = pattern_len - 1

    while i < string_len:
        if string[i] == pattern[k]:
            if k == 0:
                print "Matching..."
                return
            k -= 1
            i -= 1
        else:
            i += pattern_len - min(1 + last[string[i]], k)
            k = pattern_len - 1
    print "No"







if __name__ == '__main__':
    string = "hello world"
    pattern = "world"

    BM(string, pattern)

