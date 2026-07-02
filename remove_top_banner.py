import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# Regex pattern to match the top bar section
# We match from <div class="hidden lg:flex bg-bgmain h-11 text-xs text-paratext relative w-full">
# up to its closing </div>
# The block looks like this:
# <div class="hidden lg:flex bg-bgmain h-11 text-xs text-paratext relative w-full">
#   ... (inner divs) ...
# </div>

pattern = re.compile(
    r'<div class="hidden lg:flex bg-bgmain h-11 text-xs text-paratext relative w-full">.*?<div class="flex-1 flex justify-end items-center px-8 space-x-8 z-0 font-medium">.*?</div>\s*</div>',
    re.DOTALL
)

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn("", content)
        
        if num_subs > 0:
            # We might have left an empty line, let's clean it up slightly if needed
            new_content = re.sub(r'\n\s*\n\s*<div class="bg-bgmain w-full border-b border-bordercol">', '\n        <div class="bg-bgmain w-full border-b border-bordercol">', new_content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Removed from {filename}")

print(f"Total files updated: {count}")
