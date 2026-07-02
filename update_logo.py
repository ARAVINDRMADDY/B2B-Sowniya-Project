import os
import glob

# The directory to search
directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# Find all HTML files
html_files = glob.glob(os.path.join(directory, "*.html"))

new_logo_nav = '''                        <a href="index.html" class="flex items-center group">
                            <div class="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-tr from-primary to-hovercol shadow-lg shadow-primary/30 mr-3 transform group-hover:-translate-y-1 transition-all duration-300">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path>
                                </svg>
                            </div>
                            <div class="flex flex-col leading-none">
                                <span class="text-2xl font-extrabold tracking-tight">
                                    <span class="text-headtext">B2B</span><span class="text-primary">Lead</span><span class="text-headtext">Nex</span>
                                </span>
                                <span class="text-[0.6rem] font-semibold text-paratext uppercase tracking-[0.2em] mt-1">Global Data Solutions</span>
                            </div>
                        </a>'''

new_logo_footer = '''                    <a href="index.html" class="flex items-center group mb-4">
                        <div class="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-tr from-primary to-hovercol shadow-lg shadow-primary/30 mr-3 transform group-hover:-translate-y-1 transition-all duration-300">
                            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path>
                            </svg>
                        </div>
                        <div class="flex flex-col leading-none">
                            <span class="text-2xl font-extrabold tracking-tight">
                                <span class="text-headtext">B2B</span><span class="text-primary">Lead</span><span class="text-headtext">Nex</span>
                            </span>
                            <span class="text-[0.6rem] font-semibold text-paratext uppercase tracking-[0.2em] mt-1">Global Data Solutions</span>
                        </div>
                    </a>'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace nav
    if "index.html" not in filepath:
        # For non-index files, search and replace the nav logo
        import re
        content = re.sub(r'                        <a href="index\.html" class="text-3xl font-extrabold tracking-tight flex items-center">\s*<span class="text-primary">B2BLead</span><span class="text-primary">Nex</span>\s*</a>', new_logo_nav, content)
    
    # replace footer in all files (including index)
    import re
    content = re.sub(r'                    <a href="index\.html" class="text-3xl font-extrabold tracking-tight flex items-center mb-2">\s*<span class="text-primary">B2BLead</span><span class="text-primary">Nex</span>\s*</a>', new_logo_footer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print("Logo replacement complete")
