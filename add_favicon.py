import os

directory = '.'
favicon_tag = '<link rel="icon" type="image/png" href="image/icon png 2.png">\n</head>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<link rel="icon"' not in content:
            new_content = content.replace('</head>', favicon_tag)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f'Added favicon to {filename}')

print(f'Total files updated: {count}')
