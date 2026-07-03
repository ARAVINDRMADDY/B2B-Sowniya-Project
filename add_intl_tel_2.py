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

# Find the entire flex div that contains the flag and phone input
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'name="phone"' not in content:
        return False
        
    old_content = content

    # Regex to match the button containing the flag
    button_regex = re.compile(r'<button[^>]*>\s*<img src="https://flagcdn\.com/w20/us\.png"[^>]*>.*?</button>', re.DOTALL | re.IGNORECASE)
    
    # We will search for all <div class="flex"> or <div class="flex "> blocks containing the button
    # Wait, simpler: just remove the button, and replace "rounded-r-md" with "rounded-md" on the input.
    # And change `<div class="flex">` to `<div class="w-full">` or keep it but the button is gone.
    # The input is inside a `<div class="relative w-full">` which is inside the `<div class="flex">`.
    # Let's just remove the button.
    
    content = button_regex.sub('', content)
    
    # Also fix rounded-r-md to rounded-md
    content = content.replace('rounded-r-md', 'rounded-md')
    
    if content != old_content:
        # We modified something, so let's add CSS/JS if not already there
        if 'intlTelInput.css' not in content:
            content = content.replace('</head>', css_link)
            content = content.replace('</body>', js_script)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        if process_file(filepath):
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
