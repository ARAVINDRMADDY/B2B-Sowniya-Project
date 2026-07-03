import os
import glob

html_files = glob.glob('*.html')
old_email = 'https://formsubmit.co/lucybrady012@yahoo.com'
new_email = 'https://formsubmit.co/92bc52dd5b9811169d0d5b50c735950e'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_email in content:
        content = content.replace(old_email, new_email)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Successfully updated form token in {count} files.')
