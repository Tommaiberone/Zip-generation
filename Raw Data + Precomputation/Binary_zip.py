import pandas as pd
import os
import zlib
import shutil

# Load the CSV file
df = pd.read_csv('IMDB Dataset.csv')

# Create directories for the text files and deflate files if they don't exist
text_dir = 'text_files'
deflate_dir = 'deflate_files'
os.makedirs(text_dir, exist_ok=True)
os.makedirs(deflate_dir, exist_ok=True)

# New dataset
new_dataset = []

for i, row in df.iterrows():
    # File names for the text and deflate files
    text_filename = os.path.join(text_dir, f"review_{i}.txt")
    deflate_filename = os.path.join(deflate_dir, f"review_{i}.zip")

    # Truncate the review text to 20 words
    review_words = row['review'].split()[:20]
    truncated_review = ' '.join(review_words)

    # Write the truncated review to a text file
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(truncated_review)

    # Compress the text file content using zlib (deflate)
    with open(text_filename, 'rb') as text_file:
        text_content = text_file.read()
        compressed_content = zlib.compress(text_content)
        with open(deflate_filename, 'wb') as deflate_file:
            deflate_file.write(compressed_content)

    # Read and encode the contents of the deflate file as a binary string
    with open(deflate_filename, 'rb') as deflate_file:
        deflate_content_binary = ''.join([format(byte, '08b') for byte in deflate_file.read()])

    # Decompression test on the binary encoded string
    deflate_content = int(deflate_content_binary, 2)
    deflate_content_bytes = deflate_content.to_bytes((deflate_content.bit_length() + 7) // 8, 'big')
    decompressed_content = zlib.decompress(deflate_content_bytes)

    # Check if the decompressed content matches the original content
    assert decompressed_content.decode('utf-8') == truncated_review, "Decompression test failed"

    # Append to the new dataset
    new_dataset.append({'text': truncated_review, 'deflate_binary': deflate_content_binary})

# Convert the new dataset to a DataFrame
new_df = pd.DataFrame(new_dataset)

# Save the new DataFrame to a CSV file
new_df.to_csv('new_dataset_deflate_binary.csv', index=False)

# Force removing of the directories
shutil.rmtree(text_dir)
shutil.rmtree(deflate_dir)

print("All decompression tests passed successfully.")
