import os
import re

directory = '.'

css_link = '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/css/intlTelInput.css"/>\n</head>'

js_script = '''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/intlTelInput.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            var phoneInputs = document.querySelectorAll('input[name="phone"]');
            phoneInputs.forEach(function(input) {
                window.intlTelInput(input, {
                    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
                    initialCountry: "us",
                    separateDialCode: true,
                });
            });
        });
    </script>
</body>'''

phone_regex = re.compile(
    r'<div class="flex">\s*<button type="button"[^>]*>.*?<img src="https://flagcdn\.com/w20/us\.png"[^>]*>.*?<span[^>]*>.*?</span>\s*</button>\s*<div class="relative w-full">\s*<input name="phone" type="tel" placeholder="Business Phone\*" required class="block w-full pl-3 pr-4 py-2\.5 bg-bgsec border border-transparent rounded-r-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">\s*</div>\s*</div>',
    re.DOTALL
)

new_phone_input = '''<div class="relative w-full">
                                <input name="phone" type="tel" placeholder="Business Phone*" required class="block w-full pr-4 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">
                            </div>'''

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'name="phone"' in content and 'intlTelInput.css' not in content:
            new_content = phone_regex.sub(new_phone_input, content)
            
            # If replacement happened, add CSS and JS
            if new_content != content:
                new_content = new_content.replace('</head>', css_link)
                new_content = new_content.replace('</body>', js_script)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {filename}")
            else:
                print(f"Regex didn't match in {filename}")

print(f"Total files updated: {count}")
