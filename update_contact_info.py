import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

footer_loc_replacement = r'''<span class="flex items-center text-paratext transition group"><div class="flex-shrink-0 w-8 h-8 rounded-full bg-bgmain flex items-center justify-center border border-bordercol group-hover:border-primary transition-colors mr-3"><svg class="w-4 h-4 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg></div><span class="text-sm">Texas, USA</span></span>'''

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        old_content = content
        
        # 1. Replace email
        content = content.replace("info@b2bleadnex.com", "lucybrady012@yahoo.com")
        
        # 2. Replace footer phone with location
        # Regex matches the <a> tag that has the phone number and is inside the footer section (has class text-paratext)
        content = re.sub(
            r'<a href="tel:\+917760747212"\s*class="flex items-center text-paratext[^>]*>.*?</a>', 
            footer_loc_replacement, 
            content, 
            flags=re.DOTALL
        )
        
        # 3. Remove any remaining phone link (e.g. from the header)
        content = re.sub(
            r'<a href="tel:\+917760747212"[^>]*>.*?</a>', 
            '', 
            content, 
            flags=re.DOTALL
        )
        
        # 4. Remove form phone block (found in as400-users-list.html, aws-users-list.html)
        content = re.sub(
            r'<div class="flex items-center">\s*<svg[^>]*>.*?</svg>\s*<span class="text-sm font-medium">\+91 7760747212</span>\s*</div>',
            '', 
            content,
            flags=re.DOTALL
        )
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
