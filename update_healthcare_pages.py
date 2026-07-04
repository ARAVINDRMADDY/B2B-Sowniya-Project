import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

replacements = [
    {
        "file": "dentist-list.html",
        "old": r'<h2 class="text-3xl lg:text-4xl font-extrabold text-primary mb-6 leading-tight">\s*Verified Dentist Contact Database\s*</h2>',
        "new": r'<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Dentists with Our Sales Leads</h2>\n                    <h3 class="text-3xl lg:text-4xl font-extrabold text-secondary mb-6 leading-tight">\n                        Verified Dentist Contact Database\n                    </h3>'
    },
    {
        "file": "hospital-list.html",
        "old": r'<h2 class="text-4xl font-extrabold text-secondary leading-tight">\s*Verified Hospital Contact Database\s*</h2>',
        "new": r'<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Hospitals with Our Sales Leads</h2>\n                    <h3 class="text-4xl font-extrabold text-secondary leading-tight">\n                        Verified Hospital Contact Database\n                    </h3>'
    },
    {
        "file": "nurses-list.html",
        "old": r'<h2 class="text-3xl font-extrabold text-headtext mb-6">Nurses Contact Intelligence</h2>',
        "new": r'<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Nurses with Our Sales Leads</h2>\n            <h3 class="text-3xl font-extrabold text-headtext mb-6">Nurses Contact Intelligence</h3>'
    },
    {
        "file": "physician-list.html",
        "old": r'<h2 class="text-4xl font-extrabold text-secondary leading-tight">\s*Verified Physicians Contact Database\s*</h2>',
        "new": r'<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Physicians with Our Sales Leads</h2>\n                    <h3 class="text-4xl font-extrabold text-secondary leading-tight">\n                        Verified Physicians Contact Database\n                    </h3>'
    },
    {
        "file": "healthcare-list.html",
        "old": r'<h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-\[#0B6B3A\] tracking-tight leading-tight">\s*Our Professional Email List Is the Key to Engaging Influential Leads\s*</h2>',
        "new": r'<h2 class="text-2xl font-bold text-primary mb-2">Grow Your Graph by Reaching Targeted Healthcare Professionals with Our Sales Leads</h2>\n                    <h3 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#0B6B3A] tracking-tight leading-tight">\n                        Our Professional Email List Is the Key to Engaging Influential Leads\n                    </h3>'
    }
]

for rep in replacements:
    filepath = os.path.join(directory, rep["file"])
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = re.sub(rep["old"], rep["new"], content, flags=re.IGNORECASE)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated headings in {rep['file']}")
        else:
            print(f"Heading not found or already replaced in {rep['file']}")

# Now replace opt-out / opt-in
healthcare_files = [
    "dentist-list.html", "cardiologist-list.html", "hospital-list.html",
    "nurses-list.html", "physician-list.html", "healthcare-list.html",
    "healthcare-more.html"
]

for filename in healthcare_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = content
        # we don't want to replace "options", "optometrists"
        new_content = re.sub(r'\bopt-out\b', 'unsubscribe', new_content, flags=re.IGNORECASE)
        new_content = re.sub(r'\bopt-in\b', 'verified', new_content, flags=re.IGNORECASE)
        new_content = re.sub(r'\bopt\b', 'select', new_content, flags=re.IGNORECASE)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Removed 'opt' from {filename}")
