import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

count = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 1. Update form tags to include action and method
        # Match <form ...> that doesn't already have action
        content = re.sub(r'<form\b(?![^>]*\baction=)([^>]*)>', r'<form action="https://formsubmit.co/dhanushhere30@gmail.com" method="POST"\1>', content)

        # 2. Add name="email" to <input type="email"> if not present
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\btype="email"[^>]*)>', r'<input name="email"\1>', content)

        # 3. Add name="phone" to <input type="tel"> if not present
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\btype="tel"[^>]*)>', r'<input name="phone"\1>', content)

        # 4. Add name="message" to <textarea> if not present
        content = re.sub(r'<textarea\b(?![^>]*\bname=)([^>]*)>', r'<textarea name="message"\1>', content)

        # 5. Add name to <select> if not present (pricing.html and others)
        content = re.sub(r'<select\b(?![^>]*\bname=)([^>]*)>', r'<select name="selection"\1>', content)

        # 6. Add name to <input type="text"> based on placeholder
        # Full Name
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="Full Name\*?"[^>]*)>', r'<input name="name"\1>', content)
        # First Name
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="John"[^>]*)>', r'<input name="first_name"\1>', content)
        # Last Name
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="Doe"[^>]*)>', r'<input name="last_name"\1>', content)
        # Company
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="Company Name"[^>]*)>', r'<input name="company"\1>', content)
        # Job Title
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="e.g\. CEOs, CTOs"[^>]*)>', r'<input name="job_title"\1>', content)
        # Location
        content = re.sub(r'<input\b(?![^>]*\bname=)([^>]*\bplaceholder="e.g\. USA, UK"[^>]*)>', r'<input name="location"\1>', content)

        # 7. Change button type="button" to type="submit" for Subscribe and Submit Request
        content = re.sub(r'<button\b[^>]*\btype="button"[^>]*>(?:\s*Subscribe\s*)</button>', lambda m: m.group(0).replace('type="button"', 'type="submit"'), content)
        content = re.sub(r'<button\b[^>]*\btype="button"[^>]*>(?:\s*Submit Request\s*)</button>', lambda m: m.group(0).replace('type="button"', 'type="submit"'), content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated forms in {filename}")

print(f"Total files updated: {count}")
