import glob
import re

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We match the flag emoji, followed by optional spaces, +1, and the entire <svg>...</svg>
    pattern = re.compile(r'🇺🇸\s*\+1\s*<svg[^>]*>.*?</svg>', re.DOTALL)
    new_text = '<img src="https://flagcdn.com/w20/us.png" alt="US" class="h-3 w-4 mr-1 inline"> +1 <span class="text-[10px] ml-1">▼</span>'
    
    new_content, num_subs = pattern.subn(new_text, content)
    
    if num_subs > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f} with {num_subs} replacements.")

print(f"Total files updated: {count}")
