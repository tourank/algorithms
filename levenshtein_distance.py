# create 2d array with each char making up a row and col, the final row and col will be the answer 
# empty string at row and col 0
# outer loop row, inner loop col
# 

def levenshtein_distance(str1, str2):

    row_length = len(str1)
    col_length = len(str2)

    edits = [[0 for col in range(col_length)] for row in range(row_length)]

    print(edits)


print(levenshtein_distance("abc", "yabd"))

