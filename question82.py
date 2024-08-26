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
matrix = [
    [131, 673, 234, 103,  18],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331]
]
matrix2 = parse_matrix(filename)
matrix = matrix2
branch_states = {} # (row, col): cost
start = 1
end = len(matrix) - 1

# (row,col)
branch_states[(start, 0)]  = matrix[start][0]


banned_branches = {} # (row, col): cost

def switch_smaller_branch(row, col, cost):
    if (row, col) in branch_states:
        if branch_states[(row, col)] > cost:
            return True
        return False
    return True

def find_smallest_way(branch_states):
    while branch_states:
        # Find the minimum value
        cost = min(branch_states.values())
        (row, col) = [key for key in branch_states if branch_states[key] == cost][0]
        banned_branches[(row, col)] = cost
        del branch_states[(row, col)]
        if col == end:
            return cost
        if row < end and (row + 1, col) not in banned_branches:
            if switch_smaller_branch(row + 1, col, cost + matrix[row + 1][col]):
                branch_states[(row + 1, col)] = cost + matrix[row + 1][col]
        if col < end and (row, col + 1) not in banned_branches:
            if switch_smaller_branch(row, col + 1, cost + matrix[row][col + 1]):
                branch_states[(row, col + 1)] = cost + matrix[row][col + 1]
        if row > 0 and (row - 1, col) not in banned_branches:
            if switch_smaller_branch(row - 1, col, cost + matrix[row - 1][col]):
                branch_states[(row - 1, col)] = cost + matrix[row - 1][col]

total_array = []
for i in range(0, len(matrix[0])):
    branch_states = {}
    banned_branches = {}
    branch_states[(i, 0)] = matrix[i][0]
    total_array.append(find_smallest_way(branch_states))

print(min(total_array))
    
