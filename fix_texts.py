import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

new_filter_text = r"Build precise prospect lists using advanced filters such as industry, revenue, employee count, technology stack, job title, and location—so you can connect with the right decision-makers faster."
new_faq_text = r"Our database is regularly updated and verified to ensure accurate business email addresses, job titles, company details, and contact information. We continuously maintain data quality so you receive reliable, up-to-date records for your sales and marketing campaigns."

count_filter = 0
count_faq = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # 1. Replace Hyper-Targeted Filters text
        # Regex looks for <h3 class="...">Hyper-Targeted Filters</h3>\s*<p class="...">...</p>
        filter_pattern = re.compile(r'(<h3[^>]*>Hyper-Targeted Filters</h3>\s*<p[^>]*>).*?(</p>)', re.IGNORECASE | re.DOTALL)
        content = filter_pattern.sub(r'\g<1>' + new_filter_text + r'\g<2>', content)
        
        # 2. Replace FAQ text
        # Regex looks for <h3 class="...">How frequently is the .*? email list updated\?</h3>\s*<p class="...">...</p>
        faq_pattern = re.compile(r'(<h3[^>]*>How frequently is the .*? email list updated\?</h3>\s*<p[^>]*>).*?(</p>)', re.IGNORECASE | re.DOTALL)
        content = faq_pattern.sub(r'\g<1>' + new_faq_text + r'\g<2>', content)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            if filter_pattern.search(old_content):
                count_filter += 1
            if faq_pattern.search(old_content):
                count_faq += 1
            print(f"Updated {filename}")

print(f"Total files updated for filters: {count_filter}")
print(f"Total files updated for FAQ: {count_faq}")
