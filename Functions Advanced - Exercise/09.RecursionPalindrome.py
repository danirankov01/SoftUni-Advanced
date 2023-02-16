def palindrome(word, index):
    if(index == len(word) // 2):
        return f"{word} is а palindrome"
    if(word[index] == word[-index - 1]):
        return palindrome(word, index + 1)
    else:
        return f"{word} is not а palindrome"


print(palindrome("abcba", 0))