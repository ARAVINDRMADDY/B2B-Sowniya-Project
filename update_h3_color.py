import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
healthcare_files = ['dentist-list.html', 'cardiologist-list.html', 'hospital-list.html', 'nurses-list.html', 'physician-list.html']

for filename in healthcare_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # replace text-secondary with text-[#0B6B3A] for the Verified [Profession] Contact Database heading
        new_content = re.sub(
            r'<h3 class="text-2xl font-bold text-secondary mb-6 leading-tight">',
            r'<h3 class="text-2xl font-bold text-[#0B6B3A] mb-6 leading-tight">',
            content
        )

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated h3 color in {filename}')
        else:
            print(f'No changes for {filename}')
