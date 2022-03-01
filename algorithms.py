# Original code accessed on: 2/22/22; from:
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
# CHANGELOG:
# - added main function and if name == main clause
# - deleted driver code to test program code
# - added my own comments for self teaching purposes
# - added editDistDP function accessed on 2/22/22 from:
#   https://www.geeksforgeeks.org/edit-distance-dp-5/
#   this code is contributed by Bhavya Jain

# Dynamic Programming implementation of LCS problem

# takes 2 strings, returns a list of the length of the lowest common subsequence between the 2 strings
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# A Dynamic Programming based Python program for edit
# distance problem

# checks each character in both strings and fills a table to say how
# many operations need to be performed at each change, if none needed, copy
# however many operations needed in the last step
# parameters are: first word, second word, length of first word, length of second word
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]  # sets the first index of each string in the table to 0

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]