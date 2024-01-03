import os
import py7zr
import base64

string_to_write = "Hello world"

# File names for the text and zip files
text_filename = ("test.txt")
zip_filename = os.path.join("test.7z")

# Write the review to a text file
with open(text_filename, 'w', encoding='utf-8') as text_file:
    text_file.write(string_to_write)

# Create a zip file containing the text file
with py7zr.SevenZipFile(zip_filename, 'w') as zfile:
    zfile.write(text_filename)

# Read and encode the contents of the zip file in base64
with open(zip_filename, 'rb') as zip_file:
    zip_content_base64 = base64.b64encode(zip_file.read()).decode()
    print(zip_content_base64)


