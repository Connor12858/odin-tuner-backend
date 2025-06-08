import sys
import csv

new_data = sys.argv[2]
output_path = sys.argv[3]
origin_path = sys.argv[1]
    
file_lines = []

with open(origin_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'AddToWatchWithValue' in line:
            start = line.index('@::') + 3
            end = line.index('", ', start)
            check = line[start:end]
            
            if check not in new_data:
                print(f"Warning: '{check}' not found in the new data. Skipping update for this key.")
                file_lines.append(line)
                continue
            else:
                new_value = new_data[check]
                print(f"Updating value for '{check}' to '{new_value}'")
                file_lines.append(line[:end + 3] + new_value + ');\n')
            
        else:
            file_lines.append(line)
            continue

with open(output_path, 'w') as file:
    for line in file_lines:
        file.write(line)    
    
# import csv

# def get_values(filename):
#     data = {}
#     with open(filename, mode='r') as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader:
#             key = row['Name']
#             value = row['Value']
#             data[key] = value

#     return data

# def update_values(filename, new_data, new_file_name):
#     file_lines = []
    
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             if 'AddToWatchWithValue' in line:
#                 start = line.index('@::') + 3
#                 end = line.index('", ', start)
#                 check = line[start:end]
                
#                 if check not in new_data:
#                     print(f"Warning: '{check}' not found in the new data. Skipping update for this key.")
#                     file_lines.append(line)
#                     continue
#                 else:
#                     new_value = new_data[check]
#                     print(f"Updating value for '{check}' to '{new_value}'")
#                     file_lines.append(line[:end + 3] + new_value + ');\n')
                
#             else:
#                 file_lines.append(line)
#                 continue
    
#     with open(new_file_name, 'w') as file:
#         for line in file_lines:
#             file.write(line)
        
# if __name__ == "__main__":
#     csv_file = 'test.csv'
#     odin_file = 'default.odni'
#     cal_name = input("Enter the name of the calibration: ")
    
#     data = get_values(csv_file)
#     print("Values have been read from the file.")
#     update_values(odin_file, data, cal_name + '.odni')
    