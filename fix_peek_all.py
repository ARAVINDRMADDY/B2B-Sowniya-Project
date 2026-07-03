import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

new_text = r"Explore verified business contact data, including email addresses, direct phone numbers, job titles, company information, and other essential details—ready to power your sales and marketing efforts."

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # Regex to match the h2 and the following p tag completely
        pattern = re.compile(r'(<h2[^>]*>Peek Inside the <span[^>]*>Database</span></h2>\s*<p[^>]*>).*?(</p>)', re.IGNORECASE | re.DOTALL)
        
        content = pattern.sub(r'\g<1>' + new_text + r'\g<2>', content)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
