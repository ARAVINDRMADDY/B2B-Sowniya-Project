import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# 1. Rename file
old_path = os.path.join(directory, "crm-users-list.html")
new_path = os.path.join(directory, "crm-users-list.html")
if os.path.exists(old_path):
    os.rename(old_path, new_path)

# 2. Update contents of the new CRM file
if os.path.exists(new_path):
    with open(new_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace CRM with CRM
    content = content.replace("CRM", "CRM")
    
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(content)

# 3. Update all links in all files
count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") or filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # Replace filename links
        content = content.replace("crm-users-list.html", "crm-users-list.html")
        # Replace navbar text
        content = content.replace("CRM Users List", "CRM Users List")
        # Replace any other CRM in menus if they exist
        content = content.replace("CRM", "CRM")
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated with CRM link changes: {count}")
