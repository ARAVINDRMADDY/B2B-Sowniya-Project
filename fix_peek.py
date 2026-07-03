import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

old_text = r"From your prospect's email address to their direct calling number, you will find all legal and genuine information at your disposal."
new_text = r"Explore verified business contact data, including email addresses, direct phone numbers, job titles, company information, and other essential details—ready to power your sales and marketing efforts."

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        content = content.replace(old_text, new_text)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
