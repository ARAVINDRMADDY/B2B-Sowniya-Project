import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
files_to_update = ['dentist-list.html', 'cardiologist-list.html', 'hospital-list.html', 'physician-list.html']

for filename in files_to_update:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if filename == 'dentist-list.html':
            # Dentist regex
            pattern = re.compile(
                r'<section class="py-20 bg-white relative overflow-hidden">\s*<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">\s*<div class="flex flex-col lg:flex-row gap-12 lg:gap-24 items-start">\s*<div class="w-full lg:w-5/12">\s*(<h2 class="text-3xl lg:text-4xl font-extrabold text-primary mb-4 leading-tight">.*?</h2>)\s*(<h3 class="text-2xl font-bold text-\[#0B6B3A\] mb-6 leading-tight">.*?</h3>)\s*</div>\s*<div class="w-full lg:w-7/12">\s*<div class="space-y-6 text-paratext leading-relaxed text-lg">\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>',
                re.IGNORECASE | re.DOTALL
            )
        else:
            # Cardiologist, Hospital, Physician regex
            pattern = re.compile(
                r'<section class="bg-white py-16">\s*<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">\s*<div class="lg:grid lg:grid-cols-2 lg:gap-12 items-center mb-16">\s*<div>\s*(<h2 class="text-3xl lg:text-4xl font-extrabold text-primary mb-4 leading-tight">.*?</h2>)\s*(<h3 class="text-2xl font-bold text-\[#0B6B3A\] mb-6 leading-tight">.*?</h3>)\s*</div>\s*<div class="mt-6 lg:mt-0">\s*<p class="text-sm text-headtext leading-relaxed mb-4">\s*(.*?)\s*</p>\s*<p class="text-sm text-headtext leading-relaxed mb-4">\s*(.*?)\s*</p>.*?</div>\s*</div>',
                re.IGNORECASE | re.DOTALL
            )

        match = pattern.search(content)
        if match:
            h2 = match.group(1).strip()
            h3 = match.group(2).strip()
            p1 = match.group(3).strip()
            p2 = match.group(4).strip()

            new_section = f'''<section class="bg-gray-50 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            {h2}
            {h3}
            <p class="text-base sm:text-lg mb-6 leading-relaxed font-light text-paratext max-w-4xl mx-auto">
                {p1}
            </p>
            <p class="text-base sm:text-lg leading-relaxed font-light text-paratext max-w-4xl mx-auto">
                {p2}
            </p>
        </div>'''
            
            # Note for dentist, the regex includes the closing </section> so we add it back.
            # For the others, it only goes up to </div>\s*</div>, so we add </div>\s*</section> or whatever was captured.
            if filename == 'dentist-list.html':
                new_section += '\n    </section>'
                
            new_content = content[:match.start()] + new_section + content[match.end():]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Successfully updated layout in {filename}')
        else:
            print(f'Regex did not match for {filename}')
