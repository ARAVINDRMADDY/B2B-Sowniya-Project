import os
import glob
import re

# The directory to search
directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# Find all HTML files
html_files = glob.glob(os.path.join(directory, "*.html"))

# Desktop Nav Replacement
old_desktop = r'                        <a href="technology-list\.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors">Technology</a>'
new_desktop = '''                        <div class="group relative flex items-center h-full cursor-pointer">
                            <a href="technology-list.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors flex items-center">Technology <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                            <div class="hidden group-hover:block absolute top-[calc(100%-0.5rem)] left-0 w-48 pt-2 z-50">
                                <div class="bg-bgmain shadow-xl rounded-md border border-bordercol overflow-hidden py-1">
                                    <a href="aws-users-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">AWS Users List</a>
                                    <a href="as400-users-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">AS/400 Users List</a>
                                </div>
                            </div>
                        </div>'''

# Mobile Nav Replacement
old_mobile = r'                <a href="technology-list\.html" class="block px-3 py-3 rounded-md text-base font-bold text-btntext hover:text-btntext hover:bg-btnbg transition-colors">Technology</a>'
new_mobile = '''                <details class="group">
                    <summary class="flex justify-between items-center px-3 py-3 rounded-md text-base font-bold text-btntext hover:text-btntext hover:bg-btnbg transition-colors cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                        <a href="technology-list.html" class="flex-1">Technology</a>
                        <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <div class="pl-6 pb-2 space-y-1">
                        <a href="aws-users-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-btntext hover:bg-btnbg/80 transition-colors">AWS Users List</a>
                        <a href="as400-users-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-btntext hover:bg-btnbg/80 transition-colors">AS/400 Users List</a>
                    </div>
                </details>'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # normalize line endings
    content = content.replace('\r\n', '\n')
    
    # replace nav
    content = re.sub(old_desktop, new_desktop, content)
    content = re.sub(old_mobile, new_mobile, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Tech dropdown added globally.")
