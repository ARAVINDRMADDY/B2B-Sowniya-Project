import os

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

old_filter_text = r"Build precise prospect lists using advanced filters such as industry, revenue, employee count, technology stack, job title, and location—so you can connect with the right decision-makers faster."
new_filter_text = r"Build precise prospect lists using advanced filters such as industry, revenue, employee count, technology stack, job title, and location—so you can connect with the right decision-makers faster."

old_faq_text = r"Our database is regularly updated and verified to ensure accurate business email addresses, job titles, company details, and contact information. We continuously maintain data quality so you receive reliable, up-to-date records for your sales and marketing campaigns."
new_faq_text = r"Our database is regularly updated and verified to ensure accurate business email addresses, job titles, company details, and contact information. We continuously maintain data quality so you receive reliable, up-to-date records for your sales and marketing campaigns."

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") or filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # Replace globally
        content = content.replace(old_filter_text, new_filter_text)
        content = content.replace(old_faq_text, new_faq_text)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
