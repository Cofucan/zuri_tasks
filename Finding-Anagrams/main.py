# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = ''.join(sorted(word))
    anagram = ''.join(sorted(anagram))
    if len(word) != len(anagram):
        return False
    elif word == anagram:
        return True
    else:
        return False



opt = find_anagram("below", "elbow")
print(opt)
