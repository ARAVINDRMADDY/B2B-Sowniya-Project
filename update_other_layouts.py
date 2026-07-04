import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
files = ['cardiologist-list.html', 'physician-list.html', 'nurses-list.html']

for filename in files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the profession (Cardiologists, Physicians, Nurses)
        profession = ""
        if "Cardiologist" in filename:
            profession = "Cardiologists"
        elif "physician" in filename:
            profession = "Physicians"
        elif "nurses" in filename:
            profession = "Nurses"

        # Regex to match the centered section
        pattern = r'<!-- Grow Your Graph Section -->\s*<section class="bg-gray-50 py-16">\s*<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">\s*<h2 class="text-3xl lg:text-4xl font-extrabold text-\[#0B6B3A\] mb-4 leading-tight">Grow Your Graph by Reaching Targeted ' + profession + r' with Our Sales Leads</h2>\s*<h3 class="text-2xl font-bold text-\[#0B6B3A\] mb-6 leading-tight">\s*Verified [a-zA-Z\s]+ Database\s*</h3>\s*<p class="text-base sm:text-lg mb-6 leading-relaxed font-light text-paratext max-w-4xl mx-auto">\s*(.*?)\s*</p>\s*<p class="text-base sm:text-lg leading-relaxed font-light text-paratext max-w-4xl mx-auto">\s*(.*?)\s*</p>\s*</div>'
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            p1 = match.group(1).strip()
            p2 = match.group(2).strip()

            replacement = f'''<!-- Grow Your Graph Section -->
    <section class="py-20 bg-bgmain border-t border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="lg:grid lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-5 mb-8 lg:mb-0">
                    <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#0B6B3A] tracking-tight leading-tight mb-2">Grow Your Graph by Reaching Targeted {profession} with Our Sales Leads</h2>
                </div>
                <div class="lg:col-span-7 space-y-6 text-paratext leading-relaxed">
                    <p>{p1}</p>
                    <p>{p2}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Customize List Section -->
    <section class="py-16 bg-white relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'''
            
            content = content.replace(match.group(0), replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"Could not match pattern in {filename}")
