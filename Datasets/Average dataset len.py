import csv
import re

def calculate_average_deflate_length(file_path):
    total_length = 0
    count = 0

    with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding as UTF-8
        reader = csv.DictReader(file)
        for row in reader:
            deflate_hex = row['deflate_hex']
            # Remove non-ASCII characters
            deflate_hex = re.sub(r'[^\x00-\x7F]', '', deflate_hex)
            length = len(deflate_hex) # Convert hex string length to byte length
            total_length += length
            count += 1

    if count == 0:
        return 0  # To handle empty file case

    average_length = total_length / count
    return average_length

file_path = 'randomized_shorthex2hex.csv'
average_deflate_length = calculate_average_deflate_length(file_path)
print("Average length of deflate_hex values after removing non-ASCII characters:", average_deflate_length)
