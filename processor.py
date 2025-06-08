import sys
import csv
input_path = sys.argv[1]
output_path = sys.argv[2]
    
data = {}
with open(input_path, mode='r') as csvfile:
    lines = csvfile.readlines()
    
for line in lines:
    if 'AddToWatchWithValue' in line:
        start = line.index('@::') + 3
        end = line.index('", ', start)
        check = line[start:end]
        
        value = line[end + 3:len(line) - 3]
        print(f"Value for {check}: {value.strip()}")
        data[check] = value.strip()

with open(output_path, 'w') as f:
    for key, value in data.items():
        f.write(f"{value},{key}\n")