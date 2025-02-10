class Solution:
    def sortMatrix(self, matrix):
        # Dictionary to store diagonals, where key is the difference of row and column index
        diagonal_map = {}
        rows, cols = len(matrix), len(matrix[0])

        # Traverse the matrix and group elements by their diagonal (row - col)
        for i in range(rows):
            for j in range(cols):
                key = i - j
                if key not in diagonal_map:
                    diagonal_map[key] = []
                diagonal_map[key].append(matrix[i][j])

        # Sort each diagonal: negative keys (upper diagonals) in ascending order,
        # positive keys (lower diagonals) in descending order
        for key in diagonal_map:
            if key < 0:
                diagonal_map[key].sort()
            else:
                diagonal_map[key].sort(reverse=True)

        # Populate the sorted values back into the matrix
        for i in range(rows):
            for j in range(cols):
                key = i - j
                matrix[i][j] = diagonal_map[key].pop(0)


