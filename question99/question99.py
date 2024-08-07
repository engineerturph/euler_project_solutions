import math

def find_max_base_exp(file_path):
    max_value = -float('inf')
    max_line_number = -1

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            base, exponent = map(int, line.split(','))
            value = exponent * math.log(base)
            if value > max_value:
                max_value = value
                max_line_number = line_number

    return max_line_number

file_path = './input.txt'
max_line_number = find_max_base_exp(file_path)

print(max_line_number)
