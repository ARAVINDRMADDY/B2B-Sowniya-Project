import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
key_input = '<input type="hidden" name="access_key" value="bf9b4d31-592a-4405-9d10-020f99f9fd14">'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # 1. Replace FormSubmit action with Web3Forms action
        content = content.replace('action="https://formsubmit.co/dhanushhere30@gmail.com"', 'action="https://api.web3forms.com/submit"')
        
        # 2. Remove the hidden access_key input if it somehow already exists to avoid duplicates
        content = re.sub(r'<input type="hidden" name="access_key"[^>]*>\s*', '', content)
        
        # 3. Inject it right after every <form ...>
        content = re.sub(r'(<form[^>]*>)', r'\1\n                        ' + key_input, content)
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated Web3Forms key in {filename}")

print(f"Total files updated: {count}")
