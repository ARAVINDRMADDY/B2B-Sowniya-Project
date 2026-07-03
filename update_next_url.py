import os
import glob

html_files = glob.glob('*.html')
old_next = 'value="http://127.0.0.1:5500/thank-you.html"'
new_next = 'value="https://b2-b-sowniya-project.vercel.app/thank-you.html"'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_next in content:
        content = content.replace(old_next, new_next)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Successfully updated _next redirect URL in {count} files.')
