# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

def generateMatrix(n):
    ans = [[0] * n for _ in range(n)]
    i, j, value = 0, 0, 1
    
    while value <= n * n:
        # Fill the current row to the right
        while j < n and ans[i][j] == 0:
            ans[i][j] = value
            value += 1
            j += 1
        j -= 1  # Adjust to stay in bounds
        i += 1  # Move to the next row

        # Fill the current column downward
        while i < n and ans[i][j] == 0:
            ans[i][j] = value
            value += 1
            i += 1
        i -= 1  # Adjust to stay in bounds
        j -= 1  # Move to the previous column

        # Fill the current row to the left
        while j >= 0 and ans[i][j] == 0:
            ans[i][j] = value
            value += 1
            j -= 1
        j += 1  # Adjust to stay in bounds
        i -= 1  # Move to the previous row

        # Fill the current column upward
        while i >= 0 and ans[i][j] == 0:
            ans[i][j] = value
            value += 1
            i -= 1
        i += 1  # Adjust to stay in bounds
        j += 1  # Move to the next column

    return ans

# Example usage
n =  3
matrix = generateMatrix(n)
for row in matrix:
    print(row)
