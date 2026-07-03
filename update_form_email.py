import os
import glob

html_files = glob.glob('*.html')
old_email = 'https://formsubmit.co/6a6d46bb93cfee41ac27d50f93651400'
new_email = 'https://formsubmit.co/lucybrady012@yahoo.com'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_email in content:
        content = content.replace(old_email, new_email)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Successfully updated form email in {count} files.')
