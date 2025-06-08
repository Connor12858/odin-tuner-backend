import sys
import csv
import json

# Load arguments
origin_path = sys.argv[1]
new_data_path = sys.argv[2]
output_path = sys.argv[3]

# Load replacement values from JSON
with open(new_data_path, 'r') as f:
    new_data = json.load(f)

file_lines = []

with open(origin_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'AddToWatchWithValue' in line:
            try:
                start = line.index('@::') + 3
                end = line.index('", ', start)
                check = line[start:end]

                if check not in new_data:
                    print(f"Warning: '{check}' not found in the new data. Skipping update for this key.")
                    file_lines.append(line)
                else:
                    new_value = new_data[check]
                    print(f"Updating value for '{check}' to '{new_value}'")
                    file_lines.append(line[:end + 3] + new_value + ');\n')
            except Exception as e:
                print(f"Error processing line: {line.strip()}\n{e}")
                file_lines.append(line)
        else:
            file_lines.append(line)

with open(output_path, 'w') as file:
    file.writelines(file_lines)
