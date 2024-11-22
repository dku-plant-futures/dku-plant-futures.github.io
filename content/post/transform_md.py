import os
import re

# Function to transform the <center> block into the desired format
def transform_center_block(match):
    img_src = match.group("src")
    alt_text = match.group("alt").strip()
    title = match.group("title")

    # Handle missing title
    if not title or title.strip() == "":
        title = ""  # Default to an empty string or use a placeholder, e.g., "Untitled"

    return f"""{{{{< 
    figure 
    src="{img_src}"
    title="{title.strip()}"
    alt="{alt_text}"
    class="medium"
>}}}}"""

# Updated Regular expression to handle optional width attribute and <p> tag
center_block_pattern = re.compile(
    r"""<center>\s*<img\s+src=["'](?P<src>[^"']+)["']\s+(?:width=["']\d+["']\s+)?alt=["'](?P<alt>[^"']+)["'][^>]*>\s*(?:<p>(?P<title>.*?)</p>)?\s*</center>""",
    re.DOTALL  # Allows the regex to span multiple lines
)

# Iterate through all .md files in the current directory
for filename in os.listdir("."):
    if filename.endswith(".md"):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Replace matches with the desired format
        new_content = center_block_pattern.sub(transform_center_block, content)

        # Check if there were any changes before overwriting the file
        if content != new_content:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(new_content)
            print(f"Updated: {filename}")

print("Transformation complete.")
