import re
with open('contact-us.html', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'<div class="flex">\s*<button.*?name="phone".*?</div>\s*</div>', content, re.DOTALL)
if match:
    print("contact-us.html matches pattern!")
    print(match.group(0))
else:
    print("No match in contact-us.html")
