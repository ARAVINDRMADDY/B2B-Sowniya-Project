import os
import glob
import re

# The directory to search
directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# Find all HTML files
html_files = glob.glob(os.path.join(directory, "*.html"))

original_logo_nav = '''                        <a href="index.html" class="text-3xl font-extrabold tracking-tight flex items-center">
                            <span class="text-primary">B2BLead</span><span class="text-primary">Nex</span>
                        </a>'''

original_logo_footer = '''                    <a href="index.html" class="text-3xl font-extrabold tracking-tight flex items-center mb-2">
                        <span class="text-primary">B2BLead</span><span class="text-primary">Nex</span>
                    </a>'''

# We will use regex to find the huge block of new_logo and replace it with the original text.
# Nav block regex: starts with '<a href="index.html" class="flex items-center group">' 
# and ends with the first '</a>' that follows 'Global Data Solutions</span>\n                            </div>'

pattern_nav = r'                        <a href="index\.html" class="flex items-center group">.*?Global Data Solutions</span>\s*</div>\s*</a>'
pattern_footer = r'                    <a href="index\.html" class="flex items-center group mb-4">.*?Global Data Solutions</span>\s*</div>\s*</a>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # normalize line endings
    content = content.replace('\r\n', '\n')
    
    # undo nav
    content = re.sub(pattern_nav, original_logo_nav, content, flags=re.DOTALL)
    
    # undo footer
    content = re.sub(pattern_footer, original_logo_footer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Undo complete")
