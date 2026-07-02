import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
hidden_inputs = """
                        <input type="hidden" name="_next" value="http://127.0.0.1:5500/thank-you.html">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_subject" value="New Lead from B2BLeadNex Website">
"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "thank-you.html":
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # 1. Update action URL to use secure token
        content = content.replace('action="https://formsubmit.co/dhanushhere30@gmail.com"', 'action="https://formsubmit.co/6a6d46bb93cfee41ac27d50f93651400"')
        
        # 2. Inject hidden inputs right after <form ...>
        # First remove them if they exist to avoid duplicates
        content = re.sub(r'<input type="hidden" name="_next"[^>]*>\s*', '', content)
        content = re.sub(r'<input type="hidden" name="_captcha"[^>]*>\s*', '', content)
        content = re.sub(r'<input type="hidden" name="_subject"[^>]*>\s*', '', content)
        
        # Inject after form
        content = re.sub(r'(<form[^>]*>)', r'\1' + hidden_inputs, content)
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated FormSubmit settings in {filename}")

print(f"Total files updated: {count}")
