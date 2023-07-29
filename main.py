'''A palindrome is a word which is the same when read forwards as it is when read backwards. For
example, mom and anna are two palindromes.
A word which has just one letter, such as a, is also a palindrome.
Given a word, what is the longest palindrome that is contained in the word? That is, what is the
longest palindrome that we can obtain, if we are allowed to delete characters from the beginning
and/or the end of the string?
Input Specification
The input will consist of one line, containing a sequence of at least 1 and at most 40 lowercase
letters'''

def longest_palindrome(word):
    n = len(word)
    dp = [[0] * n for _ in range(n)]  # Initialize the matrix

    # Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    max_length = 1  # Initialize the maximum length

    # Check for palindromes of length 2
    for i in range(n - 1):
        if word[i] == word[i + 1]:
            dp[i][i + 1] = 2
            max_length = 2

    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if word[i] == word[j] and dp[i + 1][j - 1] == length - 2:
                dp[i][j] = length
                max_length = length

    return max_length


# Read input
word = input().strip()

# Find the longest palindrome
result = longest_palindrome(word)

# Print the result
print(result)