import os

directory = '.'

style_tag = '    <style>.iti { width: 100%; display: block; }</style>\n</head>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'intlTelInput' in content and '<style>.iti' not in content:
            new_content = content.replace('</head>', style_tag)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Fixed styling in {filename}")

print(f"Total styling fixed: {count}")
