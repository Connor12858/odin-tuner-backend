import sys
input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'r') as f:
    lines = f.readlines()

# Basic transformation logic
modified = [line.upper() for line in lines]

with open(output_path, 'w') as f:
    f.writelines(modified)
