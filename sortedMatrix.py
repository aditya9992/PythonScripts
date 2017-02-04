# Program for searching in a Column and Row wise sorted matrix

def searchMatrix(matrix, n, x):
    i, j = 0, n - 1

    while i < n and j >= 0:
        if matrix[i][j] == x:
            print("Element found at %d %d"%(i, j))
            return True
        if matrix[i][j] < x:
            j -= 1
        else:
            i += 1
        print("Element not found")
    return False