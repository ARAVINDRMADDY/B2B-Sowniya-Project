import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
healthcare_files = ['dentist-list.html', 'cardiologist-list.html', 'hospital-list.html', 'nurses-list.html', 'physician-list.html', 'healthcare-list.html', 'healthcare-more.html']

for filename in healthcare_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content

        if filename == 'healthcare-list.html':
            # Grow Your Graph: text-2xl font-bold text-primary mb-2
            # Verified: text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#0B6B3A] tracking-tight leading-tight
            new_content = re.sub(
                r'<h2 class="text-2xl font-bold text-primary mb-2">(Grow Your Graph[^<]+)</h2>\s*<h3 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-\[#0B6B3A\] tracking-tight leading-tight">\s*(.*?)\s*</h3>',
                r'<h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-primary tracking-tight leading-tight mb-2">\1</h2>\n                    <h3 class="text-2xl font-bold text-[#0B6B3A] mb-6">\n                        \2\n                    </h3>',
                new_content, flags=re.IGNORECASE | re.DOTALL)
        else:
            # Grow Your Graph: text-2xl font-bold text-primary mb-2
            # Verified: text-3xl lg:text-4xl font-extrabold text-[something] mb-6 leading-tight
            # Wait, in the files other than healthcare-list.html, the classes are:
            # <h3 class="text-3xl lg:text-4xl font-extrabold text-secondary mb-6 leading-tight"> ... OR
            # <h3 class="text-4xl font-extrabold text-secondary leading-tight"> ... OR
            # <h3 class="text-3xl font-extrabold text-headtext mb-6"> ...

            # To do it safely, I will just match both lines and swap their font size and weight classes.
            def replacer(m):
                grow_text = m.group(1)
                verified_text = m.group(2)
                
                # I'll manually set the classes
                return f'<h2 class="text-3xl lg:text-4xl font-extrabold text-primary mb-4 leading-tight">{grow_text}</h2>\n                    <h3 class="text-2xl font-bold text-secondary mb-6 leading-tight">\n                        {verified_text}\n                    </h3>'
                
            new_content = re.sub(
                r'<h2 class="text-2xl font-bold text-primary mb-2">(Grow Your Graph[^<]+)</h2>\s*<h3 class="[^"]+">\s*(.*?)\s*</h3>',
                replacer,
                new_content, flags=re.IGNORECASE | re.DOTALL)

        if filename == 'nurses-list.html':
            # reduce padding and margins to make it fit viewport
            new_content = new_content.replace('min-h-[calc(100vh-124px)] flex items-center py-10 lg:py-12', 'min-h-[calc(100vh-124px)] flex items-center py-6 lg:py-8')
            new_content = new_content.replace('p-5 sm:p-8 w-full', 'p-4 sm:p-6 w-full')
            new_content = new_content.replace('mb-6">We have got you covered', 'mb-4">We have got you covered')
            new_content = new_content.replace('<form class="space-y-4">', '<form class="space-y-3">')
            new_content = new_content.replace('py-3 bg-gray-50/80', 'py-2 bg-gray-50/80')
            new_content = new_content.replace('py-3 bg-transparent', 'py-2 bg-transparent')
            new_content = new_content.replace('rows="3"', 'rows="2"')
            new_content = new_content.replace('py-4 px-4 border', 'py-3 px-4 border')
            new_content = new_content.replace('mb-8 leading-relaxed', 'mb-6 leading-relaxed')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated text sizes in {filename}')
        else:
            print(f'No changes for {filename}')
