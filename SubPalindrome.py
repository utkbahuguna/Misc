def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    l = len(text)
    mid = 1
    j = 0
    longest = 1
    s = 0
    end = 0
    for i in range(1, l):
        if longest<2 and text[mid-longest]==text[mid]:
            s=mid-longest
            end=mid+1
            longest+=1
            mid+=1
        elif mid-longest >=0 and mid +longest<l and text[mid - longest] == text[mid+longest]:
            s= mid - longest
            end = mid+longest+1
            longest +=1
        else:
            mid +=1
    return (s, end)
    # Your code here

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()