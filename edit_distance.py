# edit_distance.py
# Afnan Enayet
# A dynamic programming solution to finding the edit distance between two
# strings


def edit_distance(str1, str2):
    """ calculates the edit distance between 2 strings
    uses a DP approach with a table that calculates the edit distance between
    2 substrings
    dp[i][j] = edit distance between str1[i] and str2[j]
    :type str1: string
    :type str2: string
    :rtype int: """

    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # base case is just to add letters, which we know
    for i in range(len(str1)):
        dp[i][0] = i

    for i in range(len(str2)):
        dp[0][i] = i

    # now iterate through strings, working on the table each row at a time
    # for each iteration, we have 3 cases:
    #   - an element is removed from x
    #   - an element is added to x
    #   - an element is changed from x
    #   - nothing changes bc current element is the same
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # if the characters are different, we know we will have to at least
            # change one thing
            if str1[i - 1] == str2[j - 1]:
                c = 0
            else:
                c = 1

            # take the minimum case
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # remove one char from str1
                dp[i][j - 1] + 1,  # remove one char from str2
                # change one letter or don't change a letter (lengths stay the
                # same)
                dp[i - 1][j - 1] + c)

    # print min edit distance between str1[:len(str1)-1], str2[:len(str2)-1]
    return dp[len(str1) - 1][len(str2) - 1]


# test
pairs = [
    ["hi", "hi"],
    ["hello", "hi"],
    ["movie", "love"],
]

for pair in pairs:
    edit_dist = edit_distance(pair[0], pair[1])
    print("Edit distance between " + pair[0] + " and " + pair[1] + " is " +
          str(edit_dist))
