import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
healthcare_files = ['cardiologist-list.html', 'hospital-list.html', 'nurses-list.html', 'physician-list.html', 'healthcare-list.html']

for filename in healthcare_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the h2 "Grow Your Graph..." heading color to dark green
        content = re.sub(
            r'(<h2 class="[^"]*?)text-primary([^"]*?">Grow Your Graph)',
            r'\1text-[#0B6B3A]\2',
            content
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated all other pages to use the dark green heading.")
