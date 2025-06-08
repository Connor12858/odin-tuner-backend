import sys

new_data = sys.argv[1]
output_path = sys.argv[2]

with open(output_path, 'w') as f:
    f.write("This is a test")