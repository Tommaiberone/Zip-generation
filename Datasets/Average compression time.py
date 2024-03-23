import os
import time
import zipfile

# Define the text content
text_content = """
In the depths of the lush forest, where the sunlight trickles through the intricate canopy, a symphony of life unfolds. Vibrant hues of green mingle with the earthy scent of moss, creating an enchanting atmosphere that beckons explorers and dreamers alike. The gentle rustling of leaves whispers untold secrets, as if the trees themselves hold ancient wisdom. Birds gracefully soar overhead, their melodious songs weaving through the air, adding to the harmonious chorus of nature's orchestra. Small creatures scurry across the forest floor, their delicate footprints leaving imprints in the soft soil. The delicate dance of sunlight and shadow creates a mesmerizing interplay, casting ethereal patterns on the forest floor. Amidst the tranquility, one can't help but feel a sense of connection to something greater—a reminder that we are but a small part of this vast tapestry of life. The forest, a sanctuary for both solitude and camaraderie, invites us to pause, to breathe, and to marvel at the beauty that surrounds us.
"""

# Define the filename
filename = "forest.txt"

# Write the content to the file
with open(filename, "w") as file:
    file.write(text_content)

# Number of iterations
num_iterations = 10000
total_time = 0

for i in range(num_iterations):
    # Delete the zip file if it exists
    if os.path.exists("forest.zip"):
        os.remove("forest.zip")

    # Measure the time taken for compression
    start_time = time.time()

    # Create a zip file with deflate compression
    with zipfile.ZipFile("forest.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filename)

    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    total_time += elapsed_time

# Calculate the average time
average_time = total_time / num_iterations

print(f"Average compression time over {num_iterations} iterations: {average_time:.4f} seconds.")
