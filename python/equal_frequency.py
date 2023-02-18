# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
# Note:
# * The frequency of a letter x is the number of times it occurs in the string.
# * You must remove exactly one letter and cannot chose to do nothing.

def main(word):
    alphabet = {} 
    for i in list(word):
        if i in alphabet:
            alphabet[i] = alphabet[i] + 1
        else:
            alphabet[i] = 1

    frequency = sorted(alphabet.values())
    frequency_set = sorted(list(set(frequency)))
    first = frequency[0]
    last = frequency[-1]


    if len(frequency) == 1:
        return True

    if len(frequency_set) > 2:
        return False

    if len(frequency_set) == 1 and first == 1:
        return True

   
    print(frequency)
    print(first)
    print(frequency[-1])

    # "cccd"
    if len(frequency) == 2:
        # "cccd"
        if first == 1:
            return True
        return (last - first) == 1
    

    # "ddaccb"
    # [1, 1, 2, 2]
    
    #if (frequency_set[1] - frequency_set[0]) != 1:
    #    return False

    # "abbcc"
    # [1, 2, 2]
    if (first == 1 and frequency[-1] == 2):
        return True

    # "ddaccb"
    # [1, 1, 2, 2]
    count = 0
    for i in frequency:
        count = count + (i-first)
    if count > 1:
        return False

    # "aaaabbbbccc"
    # [3, 4, 4]
    if (last - frequency[-2]) == 1:
        return True

    #if (count != 1 and count != (len(frequency) - 1)):
    #    return False
    
    #if (first == 1 and len(frequency) == 2):
    #    return True

    #if ((frequency[-1] - first) == 1 and len(frequency) == 2):
    #    return True

    #if first == 1 and frequency[-1] == 2:
    #    return True

    return False


if __name__ == "__main__":
    # "abcc"
    # "aazz"
    # "cccd"
    # "aaaabbbbccc"
    # "abbcc"
    # "ddaccb"

    word = "abccddb"
    print (main(word))