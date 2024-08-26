def parse_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip any extra whitespace and split by comma
            row = line.strip().split(',')
            matrix.append([int(row) for row in row])
    return matrix

# Example usage
filename = './0081_matrix.txt'  # Replace with your file path
matrix = parse_matrix(filename)

def min_path_sum(matrix):
    n = len(matrix)
    for i in range(n - 2, -1, -1):
        matrix[n - 1][i] += matrix[n - 1][i + 1]
        matrix[i][n - 1] += matrix[i + 1][n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

    return matrix[0][0]

print(min_path_sum(matrix))  