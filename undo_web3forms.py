import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Revert Web3Forms action to FormSubmit
        content = content.replace('action="https://api.web3forms.com/submit"', 'action="https://formsubmit.co/dhanushhere30@gmail.com"')
        
        # Remove the hidden access_key input
        content = re.sub(r'<input type="hidden" name="access_key"[^>]*>\s*', '', content)
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Reverted Web3Forms in {filename}")

print(f"Total files reverted: {count}")
