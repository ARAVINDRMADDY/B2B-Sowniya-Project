import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
healthcare_files = ['dentist-list.html', 'cardiologist-list.html', 'hospital-list.html', 'nurses-list.html', 'physician-list.html', 'healthcare-list.html', 'healthcare-more.html']

for filename in healthcare_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(r'advanced targeting options', 'advanced targeting capabilities', content, flags=re.IGNORECASE)
        new_content = re.sub(r'opt-out mechanisms', 'unsubscribe mechanisms', new_content, flags=re.IGNORECASE)
        new_content = re.sub(r'\bOpt-in\b', 'Verified', new_content, flags=re.IGNORECASE)
        new_content = re.sub(r'\bopt\b', '', new_content, flags=re.IGNORECASE) # just in case there's an exact word 'opt'
        
        # fix cardiologist heading
        if filename == 'cardiologist-list.html':
             old_cardio = r'<h2 class="text-4xl font-extrabold text-secondary leading-tight">\s*Grow Your Graph by <br> Reaching Targeted <br> Cardiologists with Our <br> Sales Leads\s*</h2>'
             new_cardio = '<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Cardiologists with Our Sales Leads</h2>\n                    <h3 class="text-4xl font-extrabold text-secondary leading-tight">\n                        Verified Cardiologists Contact Database\n                    </h3>'
             new_content = re.sub(old_cardio, new_cardio, new_content, flags=re.IGNORECASE)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
